# plate-recognizer on the RaspberryPi 

This projects aims at detecting and parsing license plates number with the camera module of your RaspberryPi by calling [plate-recognizer](https://guides.platerecognizer.com/docs/snapshot/api-reference) API. 

To do so, you will have to meet these hardware requirements : 

* Raspberry Pi (at least version 3B)
* Picamera module
* Portable touch screen *(Optional)*
* Battery *(Optional)*

The last two are recommended if you plan to make a portable license plate detector. 

## Installation 

You should consider running this program in a python venv as RaspberryPiOS will prevent you from installing pip packages system wide, for it not to alter APT packages. 

Here is an example on how to do so : 

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


### Project tasks

- [ ] Optimization of color accuracy (strange color precision on the picamera module)
- [ ] Parse the API response to save results locally in a table
- [ ] Integration of stream API for live recording
