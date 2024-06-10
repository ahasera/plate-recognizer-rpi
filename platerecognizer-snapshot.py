import time
import requests
from picamera2 import Picamera2, Preview
from datetime import datetime
import os
import threading

# camera config init
camera = Picamera2()
config = camera.create_still_configuration(main={"size": (1024, 768)})
camera.configure(config)
camera.start_preview(Preview.QTGL)
camera.start()
time_to_capture = 10 # this value sets the time between each capture

api_url = "https://api.platerecognizer.com/v1/plate-reader/"
api_token = "" # put your API token here

pause = False

def capture_image(image_path):
    """--image capture--"""
    camera.capture_file(image_path)
    print(f"Image taken and stored here : {image_path}")

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
    global pause
    save_dir = "./images" # the directory where captured images are stored 
    os.makedirs(save_dir, exist_ok=True)

    while True:
        if not pause:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(save_dir, f"capture_{timestamp}.jpg")
            capture_image(image_path)
            
            # calling the API 
            result = send_to_plate_recognizer(image_path)
            print(f"API Response: {result}")
        
        # Display the remaining time before the next capture
        for i in range(time_to_capture, 0, -1):
            if not pause:
                print(f"Next capture in {i} seconds...", end='\r')
            time.sleep(1)
        if pause:
            print("Capture paused. Press 'p' to resume.", end='\r')
            while pause:
                time.sleep(1)

def listen_for_pause():
    global pause
    while True:
        user_input = input()
        if user_input.lower() == 'p':
            pause = not pause
            if pause:
                print("Pause activated.")
            else:
                print("Pause stopped captures will resume")

if __name__ == "__main__":
    try:
        threading.Thread(target=listen_for_pause, daemon=True).start()
        capture_loop()
    except KeyboardInterrupt:
        print("program killed by user")
    finally:
        camera.stop_preview()
        camera.close()
