# TKinter Vermiculture 
TKinter Vermiculture is a Python based visualization system to monitor a self controlled Vermiculture environment.

### Modules used
  - TKinter
  - PySerial

# How it works?

The Vermiculture is the action of keeping worms. The self controlled enviroment works using a microcontroller that reads Temperature and Humidity sensors and then using that information implements an on-off control on some actuators a fan, a heater and a water pump to keep the entire enviroment in the set points, Then for to monitor the system, via Serial Communication the system send the data about the sensors and the actuators in a single formated message every 5 seconds.

#### How it began?
Was a paid work make this monitor and control system, the first script was write using only one file that contains the view, the serial comunication and everything, in order to improve the system and my programming skills I am in the process to update the project using the MVC Pattern.

##### Actuator
- A common 110V Resistive Heater
- 12V Fan (Like the computers fan)
- 12V Water Pump

##### Sensor (For now)
- [DHT-11](https://learn.adafruit.com/dht)
The sensor was manually adapted to be buried on the dirt

##### The enviroment

The entire system is in a box, half full of organic material and also the worms, we need to keep the system between 12-25°C (53-77°F) and a least 80% of humidity, the Resistive heater is place at the bottom of the box to maintain the temperature in the range, at the side of the box there is a valve to drain the liquid humus at the other side there is the DHT-11 sensor and the fan in the empty half near to the top to keep ventilation active, in the top of the box, the output of the water pump to increase the humidity if is neccesary.

<p align="center">
<img src="https://raw.githubusercontent.com/Ned-zib/TKinter_Vermiculture/master/images/vermi.png">
<P>

### How to run?
- Run the controller.py file

### Actual Issues
- If the serial port does not send any data the system goes stuck
- The Get and Write (in Tk) Serial data system use a recursive method in order to don't stuck the Tk loop, so this can reach the Recursion limit (10.000) and raise an stack overflow fatal error is not posible set this recursion limit to infinite, and the system can't be change to a loop
### Future 
  - Turn the system to an IOT based monitor and control system

# Status: in process
