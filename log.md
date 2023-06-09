# 100 Days Of Hardware - Log

{% include_relative progress-chart.svg %}

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
