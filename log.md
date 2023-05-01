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
