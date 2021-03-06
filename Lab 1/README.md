

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Set up [your Github "Lab Hub" repository](../../../) by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how](https://guides.github.com/features/mastering-markdown/) to post links to your submissions on your readme.md so we can find them easily.

### For lab, you will need:

1. Paper
1. Markers/ Pen
1. Smart Phone--Main required feature is that the phone needs to have a browser and display a webpage.
1. Computer--we will use your computer to host a webpage which also features controls
1. Found objects and materials--you’ll have to costume your phone so that it looks like some other device. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case. Be creative!
1. Scissors

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
For this assignment, you are going to 

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.
**Describe your setting, players, activity and goals here.**

The purpose of this device is to help the user be more mindful of his/her hydration practices. In particular, this device is a smart water cup that sits on the user's desk. It starts off with an orange tone at the beginning of each day to signal that the user has not adequatly hydrated. Over time, as the user drinks more water, the device senses this and gradually changes its color to a cooler blue tone. The setting for this interaction will be at the user's work desk where he/she normally drinks water throughout the day. The actors involved will simply be the user and the device. Since device is synced to the user's Apple Watch for proximity detection, this ensures that the device does not give off false readings in the event that somebody else interacts with it.

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**

![sketch1](IMG_0194.jpg "storyboard")

![sketch2](IMG_0196.jpg "storyboard")


Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**

I got positive feedback from the group. My group members stated that this is a common problem where their water glass sits unused for hours even though they are trying to be better about staying hydrated. My group helped me think through strategies for ensuring that the device does not get thrown off by other people in the household (similar to Amazon Alexa), so I added the Apple Watch integration based on this feedback.


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**
Overall, the interaction went pretty well. I realized very quickly that this device has the potential to be pretty messy with the water, so I need to be mindful of how I handle the full prototype.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**
One idea that came up during this process is to incorporate an additional feature based on inactivity. Rather than solely show a warmer tone color statically if the user does not drink enough, the device can start pulsing if it detects that it has not been touched in a couple hours. This ramp up can help signal to the user that they are falling behind on their water drinking goals for the day in a more dynamic fashion.


## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

**Give us feedback on Tinkerbelle.**

I had issues with getting tinkerbelle to run on my computer. I could not connect to the app through my browser even though it was running at my terminal. I ultimately had to use a friend's computer to finish this assignment.

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**

The goal for this initial video is to demo the act of taking a drink of water and having the device's color change accordingly
https://youtu.be/K0tEWTWpAWc

Now, change the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

The goal for this different interaction is to demo a user 'cheating' the device by simply pouring out the water and watching its color change.
https://youtu.be/-33fIlxDgqo

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

The main considerations for the setting of my costumed device, as alluded to earlier, is the presence of water. Water can be damaging to electronics like smartphones, so I mitigated this risk by putting my costumed device in a zioloc bag before filling the smart cup with water.

Another consideration for this setting, given that it is daytime, is the brightness of the screen and the ability for users to still disern the color being shown to them. I was able to see the colors in my demo, but this is another factor that could potentially be improved.

**Include sketches of what your device might look like here.**

![sketch3](IMG_0203.jpg "costumed device sketch")

**What concerns or opportunitities are influencing the way you've designed the device to look?**

I wanted to make this device a fully-enclosed cup so that the user interacting with the device can use the same behaviors they are used to when it comes to drinking water. The downside to this approach, while better for the user, is that the interior of the cup loses a lot of volume to the smartphone. I thought this trade-off was worth it for the purposes of this lab.

## Part F. Record

**Take a video of your prototyped interaction.**

The Tinkerbelle prototype video can be found here: https://youtu.be/viKkhV8hoQ0
This video takes the viewer through a user drinking water throughout the day using this smart cup device.

**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

I worked on the design process alone and got feedback from Shivani Doshi, Nicole Zhang, and Brandt Beckerman on the design of the device.

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

One piece of feedback I got from my Shivani Doshi was to better illustrate the use-case for this device. It was not totally clear to the user that the goal of this device was to encourage hydration for the user. Instead, my partner interpreted the purpose of the device as a spill-detector. One suggestion I got to mitigate this is to rework the storytelling from the video to emphasize the benefit to the user more than the product itself.

Another piece of feedback I got from Nicole Zhang was to think about changing the orientation of the light so that it sits at the bottom of the cup rather than in the middle. This would provide for a sleeker interface that maximized the utility of the glass. Additionally, I could incorprate more than just visual cues for to nudge the user's behavior, such as sounds or vibrations. 

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process.
1. Video sketch of the prototyped interaction.
1. Submit these in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.

## Part A. Plan 

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?
_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.
_Activity:_ What is happening between the actors?
_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

**Describe your setting, players, activity and goals here.**
This device is a smart nightstand with an integrated wireless charging tabletop and sunrise clock. The nightstand wakes up the user with light instead of sound. By doing this, the nightstand mimics the progression of dawn, changing from red to orange to white before the user's alarm sounds. This gradual exposure to blue light from red light helps the user wake up naturally in line with how our ancestors woke up with the sun.

This interaction is happening in the user's bedroom. The players involved are simply the user and the device itself. If there were other people in the user's home, they would have to think about how this device might wake them up at a different time than what than they desire (as expected with any alarm). There are two activities happening here. The first is the clock's progression from nighttime (red light), to dusk (blue light), to morning (white light). The other activity is the user's pre-bedtime routine which consists of putting his/her phone down to charge and turning on the white-noise functionality. Both of these actions happen through auditory cues rather than visual cues. Ultimately, the goal for the user is to have a well-rested night of sleep with the help of this device.


Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**
![storyboard](IMG_C38C1C92DED9-1.jpeg "prototype storyboard")


Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**
During lab section, I got positive feedback from my group. They really liked the positive impact a device like this might have on their sleep hygeine. Additionally, the white noise feature was much-needed for an apartment style building like The House where the walls do not necessarily filter out sounds from other units or the surrounding city. My group encouraged me to focus on the usability of the design, which is what inspired me to make the whole surface compatible with wireless charging. This feedback also challenged me to come up with a way to turn on/off white noise without the user needing to touch the device itself.


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**
One thing that is easily overlooked is how the device sits relative to the user. Many different users may be used to different height nightstands/beds, and this design consideration is important to note in order to maximize compatibility across many different bedroom layouts. I also initially tried verbal cues to turn on/off features, but found nonverbal cues to be faster and more appropriate for a drowsy user.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**
Overall, the acting pointed out potential design oversights, but the device itself seems to be pretty well-suited to the task. As a result, I will move forward with prototyping.


## Part C. Prototype the device
I was only able to get Tinkerbelle to work by using the node version. Perhaps this might be a good workaround for the Python issues others were facing.


## Part D. Wizard the device
Here, I demo two interactions with the "paper prototype" version of the device.
https://youtu.be/j0kHazHHSCE


## Part E. Costume the device


**Include sketches of what your device might look like here.**
![prototype_sketch](IMG_3149.jpg "prototyped device sketch")

**What concerns or opportunitities are influencing the way you've designed the device to look?**
This device needs to be aesthetically appealing enough to serve double-duty as the user's furniture in their bedroom. Additionally, it needs enough surface area to both reliably charge multiple devices while keeping its utility as a tabletop surface. Finally, the sunrise light has to strike a balance between being big enough for the user to see the light without overburdening their senses. 


## Part F. Record

**Take a video of your prototyped interaction.**
Here is the final prototype going through the following user actions 1.) Charge phone/Airpods 2.) Remotely turn on white noise 3.) Go through progressions of light emitted.
https://youtu.be/41yPT0mDxXs

**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 
