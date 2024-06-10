import time
import requests
from picamera2 import Picamera2, Preview
from datetime import datetime
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Raspberry Pi Camera Script")
    parser.add_argument('--ttc', type=int, default=5, help='Time interval between captures in seconds')
    parser.add_argument('--max-photos', type=int, default=12, help='Maximum number of photos to capture (0 for no limit)')
    return parser.parse_args()

# camera config init
camera = Picamera2()
config = camera.create_still_configuration(main={"size": (1024, 768)})
camera.configure(config)
camera.start_preview(Preview.QTGL)
camera.start()

args = parse_arguments()
time_to_capture = args.ttc
max_photos = args.max_photos

# API URL
api_url = "https://api.platerecognizer.com/v1/plate-reader/"
api_token = ""  # put your API token here

def capture_image(image_path):
    """--image capture--"""
    camera.capture_file(image_path)
    print(f"Image taken and stored here: {image_path}")

def send_to_plate_recognizer(image_path):
    """Sending image to platerecognizer...."""
    with open(image_path, 'rb') as image_file:
        response = requests.post(
            api_url,
            files=dict(upload=image_file),
            headers={'Authorization': f'Token {api_token}'}
        )
    return response.json()

def capture_loop():
    save_dir = "./images"  # the directory where captured images are stored 
    os.makedirs(save_dir, exist_ok=True)

    photo_count = 0

    while max_photos == 0 or photo_count < max_photos:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join(save_dir, f"capture_{timestamp}.jpg")
        capture_image(image_path)
        
        # calling the API 
        result = send_to_plate_recognizer(image_path)
        print(f"API Response: {result}")
        photo_count += 1

        # Display the remaining time before the next capture
        for i in range(time_to_capture, 0, -1):
            print(f"Next capture in {i} seconds...", end='\r')
            time.sleep(1)

    print("Maximum number of photos reached, stopping the script.")

if __name__ == "__main__":
    try:
        capture_loop()
    except KeyboardInterrupt:
        print("Program killed by user")
    finally:
        camera.stop_preview()
        camera.close()
