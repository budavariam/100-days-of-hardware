# 100 Days Of Hardware - Log

2023
{% include_relative progress-chart2023-04-15.svg %}

2024
{% include_relative progress-chart2024-04-15.svg %}

{::nomarkdown}
<div id="tooltip">...</div>
<script>
{% include_relative progress-chart-tooltip.js %}
</script>
<style>
{% include_relative progress-chart-tooltip.css %}
</style>
{:/}

## Day 1: 2023-04-15

[Tweet](https://twitter.com/BudavariMatyas/status/1647243754212933633)

**Today's Progress**: `#100DaysOfHardware` Day 1

I've set up a `@docusaurus`  site to gather my knowledge over there.

- Inventory of my current available items and components
- Project ideas to stay on track
- Project instructables on how to recreate them
- My tutorials on the hardware I already own

**Thoughts**: It's nice to get started with a clear state of mind, with some goals in mind of what I want to achieve. I have the base building blocks, I'm looking forward to see what I can make out of them.

![Docusaurus site](assets/day-1.jpg)

## Day 2: 2023-04-16

[Tweet](https://twitter.com/BudavariMatyas/status/1647537684133412865)

**Today's Progress**: `#100DaysOfHardware` Day 2

📚 I spent time revisiting the basics from what I've learned in Electronics class in high school

🧠 I added a Theory tutorial section

🩹 I embedded a plain simple Resistor Band Color calculator into the site

🛠️ I revisited how to use the multimeter

**Thoughts**: I spent way too much time implementing that calculator, but now I have better sections, and I can add any react code from now on.

## Day 3: 2023-04-17

[Tweet](https://twitter.com/BudavariMatyas/status/1648073274457309187)

**Today's Progress**: `#100DaysOfHardware` Day 3

📚 I finished going through my inventory and added a page for all items

🖋️ I started to look into how to connect the eink display to raspberry pi

💾 I collected and reviewed some demo source code for testing it out later

**Thoughts**: It was a loooong day

## Day 4: 2023-04-18

[Tweet](https://twitter.com/BudavariMatyas/status/1648403408741707777)

**Today's Progress**: `#100DaysOfHardware` Day 4

🗺️ I've started to put together a simpler project to practice how I'll work through my ideas

🚦 This project is just going to check status info from the network and light up LEDs accordingly

🛹 I've sketched the code and planned the circuit diagram

**Thoughts**:

## Day 5: 2023-04-22

[Tweet](https://twitter.com/BudavariMatyas/status/1649884631582253059)

**Today's Progress**: `#100DaysOfHardware` Day 5

🚨  As a practice I've blinked a LED again to get astarted

👋 I connected the PIR for movement detection, blinked the lights on that

🙄 I connected the eInk display to refresh data based on movement, but sadly I see many people were struggling as well

**Thoughts**:

![None](assets/day-5.jpg)

## Day 6: 2023-05-01

[Tweet](https://twitter.com/BudavariMatyas/status/1653026148110958594)

**Today's Progress**: `#100DaysOfHardware` Day 6

🔧 At last I figured out the problem with the e-ink Display. The wiring was too loose

🍞 I added an extra layer on the breadboard between the 2 sets of wires to fix them together

🖼️ I played around with the PIL library to display text and images

**Thoughts**: I had an idea that it could be a problem, and so it was. It works flawlessly. 2 of my wires broke in the process, and I set up remote development with raspberry VSCode remote SSH.

![waveshare eink display showing the logo of my website](assets/day-6.jpg)

## Day 7: 2023-05-02

[Tweet](https://twitter.com/BudavariMatyas/status/1653282990426927105)

**Today's Progress**: `#100DaysOfHardware` Day 7

📏 My app'll have a display, and I'll debug image positions a lot. I don't want to develop on hardware

🤓 I've set up a dev env. I've configured ssh with X11 forwarding, rsync for code sharing

🎁 VScode remote plugin doesn't give enough benefits yet

**Thoughts**: I thought VSCode remote will be the way, but I like X11 way more. I collect my knowledge and might even post a blog about my setup

## Day 8: 2023-05-23

[Tweet](https://twitter.com/BudavariMatyas/status/1661067193872793621)

**Today's Progress**: `#100DaysOfHardware` Day 8

⏭️ Today I wanted to learn more about what could be the next steps of a prototype

👨‍🎓 I refreshed my high school knowledge on how to draw the circuit, what is a PCB protoboard, what is a PCB

👨‍🔧 Looked into how to solder, what equipment do I need for it

**Thoughts**: bunh of reading, some knowledge management

## Day 9: 2023-06-03

[Tweet](https://twitter.com/BudavariMatyas/status/1665079614996205568)

**Today's Progress**: `#100DaysOfHardware` Day 9

🍓 Today I've tried out my Raspberry PI Pico W

🐍 I set up micropython on it via CLI from my rpi4. Later I used Thonny via X Window for development

🔋 I loaded the code into the device and ran it from a battery pack

🤓 I'm sooo excited!🤩

**Thoughts**: WOOOOW

![Raspberry pi pico is held via its USB cable with its embedded led turned on. On the background Thonny IDE is visible with the python code that runs to achieve the blinking effect](assets/day-9.jpg)

## Day 10: 2023-06-04

[Tweet](https://twitter.com/BudavariMatyas/status/1665431026263379970)

**Today's Progress**: `#100DaysOfHardware` Day 10

☀️ Summer is here, and I have to prepare for the heat

🌪️ I've dusted off my micro:bit and put together a circuit to have a button-controlled fan

🌊 Finally (after ~3 years) I tested my submersible water pumps, to see if all of them work fine with 5V

**Thoughts**: I was happy to see that the pumps work. 3V is not enough for them/

![Microbit circuit that has a button and controls a fan. A spinning fan is shown on the foreground](assets/day-10.jpg)

## Day 11: 2023-06-05

[Tweet](https://twitter.com/BudavariMatyas/status/1665827172727259138)

**Today's Progress**: `#100DaysOfHardware` Day 11

🙄 I looked for inspiration for useful projects around home

🐰 I'd be happy to build a a scheduled pet feeder with refill notifications

🍽️ I looked into how our LED strips work, whether I could utilize them as an extra light source in the kitchen

**Thoughts**:

## Day 12: 2023-06-15

[Tweet](https://twitter.com/BudavariMatyas/status/1669433800844103704)

**Today's Progress**: `#100DaysOfHardware` Day 12

🚦 Got a green light for the kitchen LED strip project

📋 I planned the final layout

🛒 I ordered the missing pieces 🤩

**Thoughts**:

## Day 13: 2023-06-19

[Tweet](https://twitter.com/BudavariMatyas/status/1670897662730678272)

**Today's Progress**: `#100DaysOfHardware` Day 13

🛒 I got the ordered pieces

👨‍🔧 I joined the wires while properly sealing them

🎉 I connected the led strip to the prepared cables

📼 I glued it to its final location

It may be plain simple but it's my first usable home improvement project so far 🎊

**Thoughts**:

## Day 14: 2023-06-20

[Tweet](https://twitter.com/BudavariMatyas/status/1671276231269007361)

**Today's Progress**: `#DaysOfHardware` Day 14

🏍️ I wired up the servo and my 5V motor to the raspberry and ran them from external battery

🌉  I started to look into how the L9110 motor driver module works

**Thoughts**:

## Day 15: 2023-06-24

[Tweet](https://twitter.com/BudavariMatyas/status/1672673816567218176)

**Today's Progress**: `#100DaysOfHardware` Day 15

👨🏻‍💻 Finally I set up the pi HAT development board with my raspberry pi pico

🔀 The cable is twisted compared to what I expected

✨ I hope it'll make prototyping easier

**Thoughts**:

![None](assets/day-15_0.jpg)

## Day 16: 2023-06-25

[Tweet](https://twitter.com/BudavariMatyas/status/1672871591359725568)

**Today's Progress**: `#100DaysOfHardware` Day 16

🚨 I've tried the mini PIR motion detector (U1 HW-740)

👨🏻‍💻 I can use the same code and it works from 3V

⌚ It's duration and sensitivity is not configurable, it's slower and had less range

🏃🏻‍♂️ For my motion sensing use-case it seems fine

**Thoughts**:

![None](assets/day-16_0.jpg)

## Day 17: 2023-07-08

[Tweet](https://twitter.com/BudavariMatyas/status/1677657344820256769)

**Today's Progress**: `#100DaysOfHardware` day 17

I started to work on my custom picture frame that'll have LED background lighting, it can have motion sensors and a light sensor.

My custom black and white images will come into life by the backlighting

(Inspired by Hwang Seontae)

**Thoughts**:

## Day 18: 2023-09-01

[Tweet](https://twitter.com/BudavariMatyas/status/1697693678607700375)

**Today's Progress**: `#100DaysOfHardware` Day 18

👨‍🔧 Finally I had some time to tinker a bit

💡 I've tried out my PioLED display

🍓 My raspberry dev environment needed some upgrades

📄 I've spent some timpe updating my docs to make my life easier later

**Thoughts**:

![None](assets/day-18_0.jpg)

## Day 19: 2023-09-16

[Tweet](https://twitter.com/BudavariMatyas/status/1703002573244895700)

**Today's Progress**: `#100DaysOfHardware` day 19

New batch of parts have arrived, now I can dive into sound playing and radiofreq 🎉

Though I did not check properly the connection types of the parts so I got some SMD parts, that are not immediately suitable for my breadboard.

I've learned my lesson

**Thoughts**:

## Day 20: 2023-09-17

[Tweet](https://twitter.com/BudavariMatyas/status/1703436912235614704)

**Today's Progress**: `#100DaysOfHardware` Day 20

I've played around with my epaper module with raspberry pi pico to display quotes from a shuffled list

**Thoughts**:

![None](assets/day-20_0.jpg)

## Day 21: 2023-09-18

[Tweet](https://twitter.com/BudavariMatyas/status/1703809500216475731)

**Today's Progress**: `#100DaysOfHardware` Day 21

Today I tried out my joystick component with my raspberry pi pico.

I got the right values without an external ADC.

**Thoughts**:

![None](assets/day-21_0.jpg)

## Day 22: 2023-09-22

[Tweet](https://twitter.com/BudavariMatyas/status/1705322524769198511)

**Today's Progress**: `#100DaysOfCode` Day 22

I've tried out my new DFPlayer mini  with my raspberry pi pico H to play music from an SD card

Shoutout and thanks for mannbro github user for the easy to use library he put together

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-22.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 23: 2023-09-22

[Tweet](https://twitter.com/BudavariMatyas/status/1705347446866407894)

**Today's Progress**: `#100DaysOfHardware` Day 23

🎨 I got started with prototype drawing, to make my experiments easier to reproduce

🗃️ What I love in the opensource community is that if something is not available, there could be someone who uploaded it somewhere just to make the components available

**Thoughts**:

![None](assets/day-23_0.jpg)

## Day 24: 2023-11-01

[Tweet](https://twitter.com/BudavariMatyas/status/1719721224006201574)

**Today's Progress**: `#100DaysOfHardware` Day 24

💻 I spinned up an mqtt server and started to learn (best) practices using it for IoT projects

🏁 We assembled our team for the upcoming hackathon where we'll build an AI powered cloud connected gadget.

**Thoughts**:

## Day 25: 2023-11-12

[Tweet](https://twitter.com/BudavariMatyas/status/1723788824700961072)

**Today's Progress**: `#100DaysOfHardware` Day 25

🐍 I've installed micropython on the ESP32

🎛️ I set up a proper dev environment for it

🎲 I can send random data to the MQTT broker

**Thoughts**:

![None](assets/day-25_0.jpg)

## Day 26: 2024-01-05

[Tweet](https://twitter.com/BudavariMatyas/status/1743312855527485591)

**Today's Progress**: `#100DaysOfHardware` day 26

🐍 Tried out my new nodemcu ESP-32S with micropython

🌈 Connected an RGB led with PWM

🙋‍♂️ Handled button interruptions

`#100DaysOfCode` `#cablePorn`

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-26.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 27: 2024-01-06

[Tweet](https://twitter.com/BudavariMatyas/status/1743574090521202964)

**Today's Progress**: `#100DaysOfHardware` Day 27

📺 I've added an LCD screen to yesterday's code

🗣️ Dove deeper into I2C communication protocol

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-27.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 28: 2024-01-10

[Tweet](https://twitter.com/BudavariMatyas/status/1745208201832722706)

**Today's Progress**: `#DaysOfHardware` Day 28

☸️ Today I connected a joystick to control 2 servos

⚡ By accident I learned more about analog to digital conversion. I had an issue with ESP32 not seeing the whole range of the joystick, apparently by default it only reads a fraction of the whole range

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-28.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 29: 2024-01-11

[Tweet](https://twitter.com/BudavariMatyas/status/1745561302716534993)

**Today's Progress**: `#100DaysOfHardware` Day 29

📶 We connected all i2c sensors to the microcontroller, validated their addresses and started to get data out of them

🧭 We connected a gps sensor through UART and got surprised about the bad quality of the signal inside the building

**Thoughts**:

## Day 30: 2024-01-18

[Tweet](https://twitter.com/BudavariMatyas/status/1748065859694661818)

**Today's Progress**: `#100DaysOfHardware` Day 30

👷 I've improved my pipeline to only upload code that has changes. I use ampy with my relatively large (more than 2 files) codebase

🌪️ I also added a smoke test to see whether the code starts up properly and reaches the end of the 1st iteration

**Thoughts**:

## Day 31: 2024-01-19

[Tweet](https://twitter.com/BudavariMatyas/status/1748428682887114944)

**Today's Progress**: `#100DaysOfHardware` Day 31

I'm starting to get desperate and demotivated by the readings of this sensor so much that I switched from esp to arduino to test other libs

I have no idea whether it works correctly or my calibration is bad

**Thoughts**:

![None](assets/day-31_0.jpg)

## Day 32: 2024-01-20

[Tweet](https://twitter.com/BudavariMatyas/status/1748631474981503328)

**Today's Progress**: `#100DaysOfHardware` Day 32

🔧 Turns out my problem was with the calibration and smoothing the data

♾️ After I used slow infinity shaped rotation, to make sure I get proper values for the calibration, North appeared where I expected

**Thoughts**:

![None](assets/day-32_0.jpg)

## Day 33: 2024-01-22

[Tweet](https://twitter.com/BudavariMatyas/status/1749515697632272773)

**Today's Progress**: `#100DaysOfHardware` Day 33

🔦 Today I've tried out different photoresistors on how well they would fit my usage needs

🌞 I struggled with which pins shall I use. When I tried Pin 4 it made the internal led bright as the sun

**Thoughts**:

![None](assets/day-33_0.jpg)

## Day 34: 2024-01-23

[Tweet](https://twitter.com/BudavariMatyas/status/1749906460509630468)

**Today's Progress**: `#100DaysOfHardware` Day 34

🚘 I haven't found a micropython driver for INA3221 that works with my ESP32 via I2C, so I started to port one from arduino

📚 I dove deeper into its datasheet and progressed slowly not to fry it unintentionally

**Thoughts**:

![None](assets/day-34_0.jpg)

## Day 35: 2024-02-01

[Tweet](https://twitter.com/BudavariMatyas/status/1753197104967598329)

**Today's Progress**: `#100DaysOfHardware` Day 35

🧸 I had some fun with my new toys

💊 I created an animated text scrolling through the famous quote of Morpheus

**Thoughts**:

![None](assets/day-35_0.jpg)

## Day 36: 2024-02-10

[Tweet](https://twitter.com/BudavariMatyas/status/1756275479366000841)

**Today's Progress**: `#100DaysOfHardware` Day 36

🏁 We participated in an internal IoT hackathon

🌻 We made a custom sun tracker solar panel with sensors and a data pipeline to measure its efficiency

📚 Stack: Micropython, Telegraf, Influxdb v2, Grafana, React.js, 3D Printing

🥉 We got 3rd place 🎉

**Thoughts**:

![None](assets/day-36_0.jpg)

## Day 37: 2024-02-25

[Tweet](https://twitter.com/BudavariMatyas/status/1761803998942605672)

**Today's Progress**: `#100DaysOfHardware` Day 37

🪖 Today made my very first soldered circuit

💡 Of course it's a LED!

**Thoughts**:

![None](assets/day-37_0.jpg)

## Day 38: 2024-03-13

[Tweet](https://twitter.com/BudavariMatyas/status/1768044246798373181)

**Today's Progress**: `#100DaysOfHardware` Day 38

🛵 Today I tried out my new L298N, to see how it drives my motors.

🐍 Sadly I had problems with Thonny even in this simple configuration... it resetted my ESP32 after few iterations, I guess I have a problem with the circuit or some hardware

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-38.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 39: 2024-03-17

[Tweet](https://twitter.com/BudavariMatyas/status/1769347834619244692)

**Today's Progress**: `#100DaysOfHardware` Day 39

🪖 I've tried out a different soldering iron. I'm pretty happy with the heating speed and the control I have over temperature

🧑‍🏭 I've fixed my previous mistakes in the dev board

🧑‍🍳 I still need a lot of practice, I possibly cooked another component

**Thoughts**:

![None](assets/day-39_0.jpg)

## Day 40: 2024-03-23

[Tweet](https://twitter.com/BudavariMatyas/status/1771534953521541614)

**Today's Progress**: `#100DaysOfHardware` Day 40

📌 I practiced soldering on pin connectors

😊 I'm not completely ashamed of my connections. Though I think I still use too much tin

⌚ I start to get used to the time it takes to heat everything up

✒️ I'm afraid I'm close to ruining my soldering tip

**Thoughts**:

![None](assets/day-40_0.jpg)

## Day 41: 2024-03-24

[Tweet](https://twitter.com/BudavariMatyas/status/1771826186663965157)

**Today's Progress**: `#100DaysOfHardware` Day 41

💡I tried out a relay to act as a switch for circuits with higher voltage

🛗 I elevated it using a spacer, it's better than when the wires control its location

🤦 I used 9V for this 12V bulb because I could not find my 12V adapter

**Thoughts**:

<video width="320" height="240" controls>
<source src="assets/day-41.mp4" type="video/mp4">
Your browser does not support the video tag...
</video>

## Day 42: 2024-03-28

[Tweet](https://twitter.com/BudavariMatyas/status/1773305997517357339)

**Today's Progress**: `#100DaysOfHardware` Day 42

🌃 I got some tin last night for trial

🌡️Now I completely get why people say it's harder to work with lead-free tin, I see almost 80°C diff in the effective temperature

🦿 I soldered legs to different components. This is what I've been waiting for! 🎉

**Thoughts**:

![None](assets/day-42_0.jpg)

## Day 43: 2024-04-14

[Tweet](https://twitter.com/BudavariMatyas/status/1779606666993979652)

**Today's Progress**: `#100DaysOfHardware` Day 43

🌿 Today I decided to start a small smart garden project

💪 I felt more confident than ever, only used 2 new components out of 6

🔎 I took extra time to double-check the wire connections, not to mess up any component

**Thoughts**:

![None](assets/day-43_0.jpg)

## Day 44: 2024-07-05

[Tweet](https://twitter.com/BudavariMatyas/status/1809290301066080671)

**Today's Progress**: `#100DaysOfHardware` Day 44

📝 I drafted an IoT device to collect temperature and humidity data based on ESP32 D1 mini, DHT-22 and BME-280

🧰 I don't have all my cables nearby so the POC is pretty basic

📜 Its micropython code sends data via WiFi through REST to influx/grafana

**Thoughts**:

![None](assets/day-44_0.jpg)

![None](assets/day-44_1.jpg)

## Day 45: 2024-07-15

[Tweet](https://twitter.com/BudavariMatyas/status/1812840708409037211)

**Today's Progress**: `#100DaysOfHardware` Day 45

Finally I figured out how to reliably update python code on my ESP32 from script

- By holding the reset button upon connecting the power source it skips the main file execution
- Also esptool kept my board busy after security info call, I replaced it

**Thoughts**:

## Day 46: 2024-07-20

[Tweet](https://twitter.com/BudavariMatyas/status/1814744165495824695)

**Today's Progress**: `#100DaysOfHardware` Day 46

📻 I played a bit with wireless transmission

🖇️ I tried a few paths to get data from this sensor. Now it connects to the device and polls the data

📢 It might broadcast its values without connecting, but I haven't yet figured it out if that's true

**Thoughts**:

![None](assets/day-46_0.jpg)

## Day 47: 2024-07-22

[Tweet](https://twitter.com/BudavariMatyas/status/1815436437346505072)

**Today's Progress**: `#100DaysOfHardware` Day 47

🔋I was able to read data from BLE without connecting to the sensor

📖 I figured out how to read the BLE advertisement data from the sensor

🤖 I made a poc with D1Mini

**Thoughts**:

![None](assets/day-47_0.jpg)

## Day 48: 2024-07-24

[Tweet](https://twitter.com/BudavariMatyas/status/1816169868988760176)

**Today's Progress**: `#100DaysOfHardware` Day 48

⚒️ I created a prototype from my pcb design

🪖 I soldered the wires and connected the relevant parts

🔔 It passed the continuity test

🤩 I'm proud of how it turned out! Even if it has its bad parts, looking forward to doing this more

**Thoughts**:

![None](assets/day-48_0.jpg)

![None](assets/day-48_1.jpg)

## Day 49: 2024-07-26

[Tweet](https://twitter.com/BudavariMatyas/status/1816874539118113092)

**Today's Progress**: `#100DaysOfHardware` Day 49

🔀 I revisited the parallel programming concepts in micropython

📻 I updated my ble advertisement collector code to pass the data properly with atomic operations in the shared memory

🤖 PoC is put into action and collects the data into influxdbv2

**Thoughts**:

## Day 50: 2024-08-02

[Tweet](https://twitter.com/BudavariMatyas/status/1819154266277445703)

**Today's Progress**: `#100DaysOfHardware` Day 50

🛹 I soldered 2 more boards

🛣️ I played around a little to make the wiring nicer while keeping it compatible with the first device

☯️ I really loved how I organized the steps so that I didn't need to go back and forth

**Thoughts**:

![None](assets/day-50_0.jpg)

## Day 51: 2024-08-02

[Tweet](https://twitter.com/BudavariMatyas/status/1819265700101341393)

**Today's Progress**: `#100DaysOfHardware` Day 51

🧙 I installed the devices, and put them into battle mode to monitor the rooms

📃 I documented the process so I'll remember the next time I need to do this.

☑️ I added a checklist not to miss a step

🏷️ Printed "pretty" labels for identification

**Thoughts**:

![None](assets/day-51_0.jpg)

## Day 52: 2024-08-03

[Tweet](https://twitter.com/BudavariMatyas/status/1819823120045293703)

**Today's Progress**: `#100DaysOfHardware` Day 52

🏁 Today I participated in the company hackathon. I decided to make a device.

🖼️ We made smart picture frame that generates an image from voice input

⚙️ We used ESP32, micropython, and a chainlit assistant

🥇 We got first place with it

**Thoughts**:

![None](assets/day-52_0.jpg)
