# plate-recognizer on the RaspberryPi 

This projects aims at detecting and parsing license plates number with the camera module of your RaspberryPi by calling [plate-recognizer](https://guides.platerecognizer.com/docs/snapshot/api-reference) API. 

To do so, you will have to meet these hardware requirements : 

* Raspberry Pi (at least version 3B) 
* Picamera module
* Portable touch screen *(Optional)*
* Battery *(Optional)*


OS Requirements : 

RaspberryPiOS 64bit or 32bit (64 recommended)

The last two are recommended if you plan to make a portable license plate detector. 
> **_NOTE:_** Users of Raspberry Pi 3 or earlier devices will need to enable Glamor in order for the GUI preview to work. To do this run sudo raspi-config in a command window, choose Advanced Options and then enable Glamor graphic acceleration. Finally reboot your device. [source](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)
## Installation 

You should consider running this program in a python venv as RaspberryPiOS will prevent you from installing pip packages system wide, for it not to alter APT packages. 

Here is an example on how to do so: 

```
mkdir pr-rpi
python3 -m venv --system-site-packages pr-rpi/
source pr-rpi/bin/activate
```
> **_FYI:_**  Using the argument `--system-site-packages` is important to use, otherwise libcamera library will fail to compile in the venv.

Then proceed to the installation of the packages dependencies:
```
pip install -r requirements.txt
```

## Usage 

You can simply launch the program with this command: 

```
python3 platerecognizer-snapshot.py
```

There is a default maximum of photos capture of 6 with a 10 seconds interval between each capture, which will make the script run for 1 minute.
This default limit is set to prevent you from exceeding your maximum API call number (if you are on plate-recognizer's free plan)

But you can of course change these default values with these arguments: 

* `--max-photos <int value>`
* `--ttc <int value>`

### Project tasks

- [ ] Optimization of color accuracy (strange color precision on the picamera module)
- [ ] Parse the API response to save results locally in a table
- [ ] Integration of stream API for live recording
