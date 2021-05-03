# How to load a Tensorflow model using OpenCV
# Jean Vitor de Paulo Blog - https://jeanvitor.com/tensorflow-object-detecion-opencv/
# David edited some stuff
# CREDIT Multiple Color Detection in Real-Time using Python-OpenCV https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/ CREDIT

import numpy as np
import cv2
import sys
import paho.mqtt.client as mqtt
import uuid
from pynput.keyboard import Key, Listener, Controller
import time
from threading import Timer

# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

######START OF SENDER######
def sendOnMQTT(ingredients):
   # Every client needs a random ID
   client = mqtt.Client(str(uuid.uuid1()))
   # configure network encryption etc
   client.tls_set()
   # this is the username and pw we have setup for the class
   client.username_pw_set('idd', 'device@theFarm')

   #connect to the broker
   client.connect(
      'farlab.infosci.cornell.edu',
      port=8883)

   topic = f"IDD/Bake_With_Me"
   print(f"now writing to topic {topic}")
   print("type new-topic to swich topics")
   val = f"{ingredients}"
   client.publish(topic, val)
######END OF SENDER######

######START OF RECIPES######
def checkRecipes(desired_recipe, passed_list):
   
   bananaBread = {"banana": 3, "butter": 2, "flour": 2, "sugar": 1, "eggs": 4}
   pumpkinStew = {"pumpkin": 3, "butter": 2, "chicken": 2, "beets": 1, "eggs": 4}
   eggsBenedict = {"cream": 1, "butter": 2, "flour": 2, "bacon": 1, "eggs": 2}

   recipes = [bananaBread, pumpkinStew, eggsBenedict]
   desired = recipes[desired_recipe-1]

   need_ingredient = desired.copy()

   for ingredient in desired:
      if ingredient in passed_list:
         need_ingredient[ingredient] = desired[ingredient] - passed_list[ingredient]

   final_set = {k:v for k, v in need_ingredient.items() if v>0}

   return sendOnMQTT(final_set)

######END OF RECIPES######

######START OF WEBCAM######
img = None
webCam = True
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image")
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")
######END OF WEBCAM######

######START OF KEYBOARD######

   # mainFunc(action_phrase)
######END OF KEYBOARD######

######START OF USER INTERACTION######
recipes = ["1) Banana Bread, 2) Pumpkin Stew, 3) Eggs Benedict"]
print(recipes)
print("What do you want to make please enter the number of the associated recipe")
desired_recipe = None
desired_recipe = input()
print("Please place your ingredients in frame")
print("Once You have your ingredients in frame please press the \"G\" key")
######END OF USER INTERACTION######




current_ingredient = ""
previous_ingredient = ""

#######SAL HERE IS WHERE THE WHILE LOOP STARTS
while(desired_recipe != None):
   passed_list= {}

   if webCam:
      ret, img = cap.read()

   rows, cols, channels = img.shape
   
   colors = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

 
#######SAL HERE IS WHERE THE THE TEST IS 
#Test
#######SAL MODIFY THESE HSV VALUES TO MATCH COLOR 
   Test_color_range_bound_1 = np.array([120,255,255])
   Test_color_range_bound_2 = np.array([100,150,0])
   Test_color = cv2.inRange(colors, Test_color_range_bound_2, Test_color_range_bound_1)
   contours_Test, _ = cv2.findContours(Test_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity = 0
   quant_Test = int()
   for pic, contour in enumerate(contours_Test):
      area = cv2.contourArea(contour)
#######SAL MODIFY THIS AREA PER OBJECT
      if(area > 12000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
         cv2.putText(img, "Test1", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0))
         current_ingredient = "Test1"
         new_quant = quantity + 1
         quant_Test = max(new_quant, quantity)
   
   passed_list[current_ingredient] = quant_Test


#####SAL Break Send the message to mqtt CHOOSE THE COLOR TO HAVE A BREAK SAL
   Break_color_range_bound_1 = np.array([120,255,255])
   Break_color_range_bound_2 = np.array([100,150,0])
   Break_color = cv2.inRange(colors, Break_color_range_bound_2, Break_color_range_bound_1)
   contours_Break, _ = cv2.findContours(Break_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   for pic, contour in enumerate(contours_Break):
      area = cv2.contourArea(contour)
      if(area > 12000):
         checkRecipes(desired_recipe, passed_list)
         print("Sent")
         time.sleep(5)
         
   

   if webCam:
      if sys.argv[-1] == "noWindow":
         print("Finished a frame")
         cv2.imwrite('detected_out.jpg',img)
         continue
      cv2.imshow('detected (press q to quit)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break


cv2.imwrite('detected_out.jpg',img)
cv2.imshow('Image out', img)
cv2.waitKey(0)
cv2.destroyAllWindows()