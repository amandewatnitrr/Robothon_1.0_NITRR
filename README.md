# Robothon_1.0_NITRR
An IoT System for Real Time Analysis of Water Quality Index and categorizing there direct feasibility for any Purpose and Anamoly Detection based Machine Learning Algorithm to predict toxicity in Water periodically. 

#Hardware Part:
You need to have following sensors to connect and program your microcontroller:
1. Arduino Mega 2560
2. pH Sensor
3. DSB1820 Temperature Sensor
4. Turbidity Sensor
5. MICS 4540 (NO2 Sensor)

Connect the hardware as per the requirments, the rough schematic has been shown in the abstract, compile the .ino file and upload it on the Arduino board.

Run the python Script included that fetches data from comport and store it in seprate variables. Now upload send the values stored in the variables to the backend Firebase using API.
