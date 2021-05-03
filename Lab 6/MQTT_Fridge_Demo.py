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

   topic = f"IDD/Ingredients_needed"
   print(f"now writing to topic {topic}")
   print("type new-topic to swich topics")
   val = f"{ingredients}"
   client.publish(topic, val)
######END OF SENDER######

######START OF RECIPES######
def checkRecipes(desired_recipe, passed_list):
   
   eggyBreakfast = {"Egg": 0, "Ketchup": 0, "Pepper": 2}
   tunaSurprise = {"Tuna": 2, "Egg": 5, "Wasabi": 1}
   chocolatePeanutButter = {"Sugar": 1, "Chocolate": 1, "Peanut": 1}

   recipes = [eggyBreakfast, tunaSurprise, chocolatePeanutButter]
   desired = recipes[int(desired_recipe)-1]
   # desired = recipes[0]

   need_ingredient = desired.copy()

   for ingredient in desired:
      if ingredient in passed_list:
         need_ingredient[ingredient] = desired[ingredient] - passed_list[ingredient]

   final_set = {k:v for k, v in need_ingredient.items() if v>0}
   if len(final_set) < 1:
      final_set = "You have all the ingredients"
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

######START OF USER INTERACTION######
recipes = ["1) Eggs for Breakfast, 2) Lunchtime Tuna, 3) Peanut Butter Chocolate Dessert"]
print(recipes)
print("What do you want to make please enter the number of the associated recipe")
desired_recipe = None
desired_recipe = input()
print("Please place your ingredients in frame")
######END OF USER INTERACTION######


current_ingredient = ""
previous_ingredient = ""
while(desired_recipe != None):
# while(True):
   passed_list= {}

   if webCam:
      ret, img = cap.read()

   rows, cols, channels = img.shape
   
   colors = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Eggs
   Egg_color_range_bound_1 = np.array([30, 255, 255])
   Egg_color_range_bound_2 = np.array([10, 100, 100])
   Egg_color = cv2.inRange(colors, Egg_color_range_bound_2, Egg_color_range_bound_1)
   contours_Egg, _ = cv2.findContours(Egg_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_egg = 0
   quant_egg = int()
   for pic, contour in enumerate(contours_Egg):
      area = cv2.contourArea(contour)
      if(10000> area > 300):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
         cv2.putText(img, "Egg", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0))
         current_ingredient = "Egg"
         quantity_egg += 1
         quant_egg = quantity_egg
   
   passed_list[current_ingredient] = quant_egg


#Tuna
   Tuna_color_range_bound_1 = np.array([120,255,255])
   Tuna_color_range_bound_2 = np.array([30,40,0])
   Tuna_color = cv2.inRange(colors, Tuna_color_range_bound_2, Tuna_color_range_bound_1)
   contours_Tuna, _ = cv2.findContours(Tuna_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_tuna = 0
   quant_tuna = int()
   for pic, contour in enumerate(contours_Tuna):
      area = cv2.contourArea(contour)
      if(2700>area > 250):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
         cv2.putText(img, "Tuna", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0))
         current_ingredient = "Tuna"
         quantity_tuna += 1
         quant_tuna = quantity_tuna
   
   passed_list[current_ingredient] = quant_tuna


#Cooking Spray
   wasabi_color_range_bound_1 = np.array([40,255,255])
   wasabi_color_range_bound_2 = np.array([30,100,100])
   wasabi_color = cv2.inRange(colors, wasabi_color_range_bound_2, wasabi_color_range_bound_1)
   contours_wasabi, _ = cv2.findContours(wasabi_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_wasabi = 0
   for pic, contour in enumerate(contours_wasabi):
      area = cv2.contourArea(contour)
      if(area > 2000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
         cv2.putText(img, "Wasabi", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0))
         current_ingredient = "Wasabi"
         quantity_wasabi += 1
   
   passed_list[current_ingredient] = quantity_wasabi

#sugar
   sugar_color_range_bound_1 = np.array([30, 255, 255])
   sugar_color_range_bound_2 = np.array([22, 120, 120])
   sugar_color = cv2.inRange(colors, sugar_color_range_bound_2, sugar_color_range_bound_1)
   contours_sugar, _ = cv2.findContours(sugar_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_sugar = 0
   quant_sugar = int()
   for pic, contour in enumerate(contours_sugar):
      area = cv2.contourArea(contour)
      if(area > 9000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
         cv2.putText(img, "Sugar", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0))  
         current_ingredient = "Sugar"
         quantity_sugar += 1
         quant_sugar = quantity_sugar

   passed_list[current_ingredient] = quant_sugar

#Oil
   oil_color_range_bound_1 = np.array([30, 255, 255])
   oil_color_range_bound_2 = np.array([10, 100, 100])
   oil_color = cv2.inRange(colors, oil_color_range_bound_2, oil_color_range_bound_1)
   contours_oil, _ = cv2.findContours(oil_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_oil = 0
   for pic, contour in enumerate(contours_oil):
      area = cv2.contourArea(contour)
      if(28000>area > 10000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (8, 200, 230), 2)
         cv2.putText(img, "Oil", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (8, 200, 230))   
         current_ingredient = "Oil" 
         quantity_oil += 1


   passed_list[current_ingredient] = quantity_oil  

#Green Pepper
   pepper_color_range_bound_1 = np.array([70, 255,255])
   pepper_color_range_bound_2 = np.array([40,40,40])
   pepper_color = cv2.inRange(colors, pepper_color_range_bound_2, pepper_color_range_bound_1)
   contours_pepper, _ = cv2.findContours(pepper_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_pepper = 0
   for pic, contour in enumerate(contours_pepper):
      area = cv2.contourArea(contour)
      if(area > 1000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 2)
         cv2.putText(img, "Pepper", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0))        
         current_ingredient = "Pepper"
         quantity_pepper += 1

   passed_list[current_ingredient] = quantity_pepper

# Ketchup
   ketchup_color_range_bound_1 = np.array([5, 200, 255])
   ketchup_color_range_bound_2 = np.array([0,20,20])
   ketchup_color = cv2.inRange(colors, ketchup_color_range_bound_2, ketchup_color_range_bound_1)
   contours_ketchup, _ = cv2.findContours(ketchup_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_ketchup = 0
   for pic, contour in enumerate(contours_ketchup):
      area = cv2.contourArea(contour)
      if(7000>area > 2000):
         x, y, width, height = cv2.boundingRect(contour)
         img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 2)
         cv2.putText(img, "Ketchup", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0))      
         current_ingredient = "Ketchup"
         quantity_ketchup += 1

   passed_list[current_ingredient] = quantity_ketchup


#Break Send the message to mqtt
   break_color_range_bound_1 = np.array([165, 200, 255])
   break_color_range_bound_2 = np.array([150,40,20])
   break_color = cv2.inRange(colors, break_color_range_bound_2, break_color_range_bound_1)
   contours_break, _ = cv2.findContours(break_color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   quantity_break = 0
   for pic, contour in enumerate(contours_break):
      area = cv2.contourArea(contour)
      if(area > 1000):
         # x, y, width, height = cv2.boundingRect(contour)
         # img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 0), 2)
         # cv2.putText(img, "sent", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0))     
         checkRecipes(desired_recipe, passed_list)
         print("Sent")
         time.sleep(2)
         
   

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
