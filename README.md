# plate-recognizer on the RaspberryPi 

This projects aims at detecting and parsing license plates number with the camera module of your RaspberryPi by calling [plate-recognizer](https://guides.platerecognizer.com/docs/snapshot/api-reference) API. 

To do so, you will have to meet these hardware requirements : 

* Raspberry Pi (at least version 3B)
* Picamera module
* Portable touch screen *(Optional)*
* Battery *(Optional)*

The last two are recommended if you plan to make a portable license plate detector. 


### Project tasks

- [] Optimization of color accuracy (strange color precision on the picamera module)
- [] Parse the API response to save results locally in a table
- [] Integration of stream API for live recording
