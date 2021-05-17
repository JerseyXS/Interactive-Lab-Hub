# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12



## Real World Do Not Disturb Light

For anyone who's familiar with the concept of Deep Work, it can be very challenging to focus on a task at-hand with countless distractions around you. Whether you are in an office-space or working at a multi-member household, the cost of context switching averages to about 25-minutes. While it may sound sensationalist, this massive cost can easily balloon into many hours of lost productivity per day. Tasks that should've taken 2 hours of focused work to complete can easily stretch into a full 8 hour workdays with enough random distractions from other people. Yet people continue to distract eachother in the workplace and in the household because they simply do not know any better. Companies are losing billions of dollars in lost productivity because of this phenomenon. My project is an end-to-end solution to this productivity epidemic.

The project I built is a very simple device that can be thought of as a real-world status indicator or do not disturb light. The key difference here is that it is fully automated, customizable, and designed to work completely from Google Calendar. This design decision was made intentionally so that the user does not need to alter their workflows in order to benefit from the device. Right out of the gate, it will recognize if a user is busy and change its status accordingly.

In designing this device, I wanted it to look appealing on a desk and friendly to the user. It should not be intimidating, but rather inviting. I also wanted to make sure that the design was able to accomplish its task under a variety of circumstances. Low light performance, bright room performance, and across-the-room performance were all factors I considered. I knew I wouldn't be able to use the parts I already owned to accomplish this, so I sought out a bright LED array. I went for a 16x16 in order to give me enough resolution to draw custom shapes for the user without sacrificing on brightness. However, the LED array itself was actually too bright, so I added a charcoal diffusor to reduce eye strain and give ita  more polished appearance. 

The other factor I considered for the design was how it would be mounted. I did not think simply placing it on the desk would be appropriate. It is easy for people to not notice something on a desk until they are already too close. I recall back from a banking internship that employee name plates were placed directly on top of each employee's monitor to maximize intra-office visibility. This led me to seek out a monitor-mounting solution. After perusing Amazon, I came to the conclusion that a magnetic, monitor-mounted smartphone holder would serve this job extremely well. In order to place a magnet on the device, however, I needed an enclosure. This led me to the Pimoroni Coupe. What I really liked about this enclosure was that it could be assembled in layers. Since my LED array was so big, I needed to leave the outermost layer exposed. After assembling this partial enclosure, I was then abe to mount the device to my monitor in such a way that the power cable is completely hidden and daisy chained off of the monitors USB A ports.

![sketch2](pi1.jpg "sketch")
![sketch2](pi_back.jpg "sketch")
![sketch2](pi_front.jpg "sketch")
![sketch2](stand.jpg "sketch")
![sketch2](red.jpg "sketch")
![sketch2](green.jpg "sketch")
![sketch2](yellow.jpg "sketch")


### Materials Used
I used the following materials in order to build this project:
* Raspberry Pi 4
* Unicorn Hat HD (LED Display) w/ Light Diffusor
* Pimoroni Pibow Coupe (Enclosure)
* Adjustable Laptop Stand w/ Magnetic Mount
* USB-A to USB-C Cable
* Google Account

### Running the Code
This project can be run on the command line using the command: python quickstart.py

This will start the script. The script will first set up the Google Calendar API connection using the user's credentials. It will then create a stream of upcoming events. Through a loop that runs every second, the code then checks if the next event in the stream is happening right now. It will then convert the JSON date format to a regular timestamp and compare this event timestamp to the current timestamp. This is where the three cases for the light come in. If the event is >10 minutes away, a green light will show. If the event has not start and is <10 minutes away, a yellow light will show. If the event has started, a red light will show. The lights were hand-drawn using numpy arrays at the beginnig of the script and colored according to the unicornhat API. 

### Reflections

Overall, I was very pleased with the end result of the project and have already started using it in my day-to-day life. The most enjoyable part for me was designing the device, both physically and from a usability standpoint. The most difficult part of the project was interacting with and debugging the Google Calendar API. The Google Cloud dashboard is very robust and overkill for managing a simple API, yet I had to jump through a lot of hoops to get it working and have it continue to work once I accidentally triggerd the API call limit. If I were to implement this in production, I would have to spend a considerable amount of time ensuring the end-user does not run into issues with the Google Calendar API integration. If I had more time, I would like to incorporate additional apps like Slack, Teams, and Outlook.

Documentation of design process
Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
Video of someone using your project (or as safe a version of that as can be managed given social distancing)
Reflections on process (What have you learned or wish you knew at the start?)

### Final Video
https://youtu.be/h4mzEMo_POE
