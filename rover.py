# Online Python Playground
# Use the online compiler to write, edit & run your Python code
# Create, edit & delete files online

# ENDG 233 Fall 2023
# Portfolio Project 1
# rover.py
# Program for calculating the time it takes a rover to travel depending on rover parameters and storm status.
# Samipya Rijal


# This module can be used to access math.floor() and math.ceil() as needed.
# e.g. math.floor(10/3) = 3, math.ceil(10/3) = 4
import math

# Tip: Create constants that can be used to store the rover parameters.
# Units should be indicated in comments
# e.g.  battery_1 = 100         # 100 kWh
# BEGIN CODE HERE
rover_used = int(input("Which rover would you like to move:")) #asks the user what rover they would like to use, 1 for Charlie, 2 for Alpha, 3 for November, explains the notation to the user as well 

if rover_used == 1: #Rover used is Charlie
    movement_speed = 5 #assigns 5 for the variable movement_speed as Charlie moves at 5km/h
    charge_time = 20 #assigns 20 for the variable charge_time as this is how long it takes for Charlie's battery to charge
    battery_distance = 200 #assigns 200 for the variable battery as this is how far Charlie can move on a fully charge  

elif rover_used == 2: #Rover used is Alpha
    movement_speed = 4 #assigns 4 for the variable movement_speed as Alpha moves at 4km/h
    charge_time = 16.25 #Assigns 16.25 for the variable charge_time as this is how long it takes for Alpha's battery to fully charge
    battery_distance = 325 #assigns 325 for the variable battery distance as this is how far Alpha can move on a single charge
   
elif rover_used == 3: #Rover used is Novemebr 
    movement_speed = 6 #assigns 6 for the variable movement_speed as November moves at 6km/h
    charge_time = 20 #Assigns 25 for the variable charge_time as this is how long it takes for Noveber's battery to fully charge
    battery_distance = 266.666666667 # assigns 266.666666667 for the variable battery distance as this how far November can move on a single charge

else:
    movement_speed = 1 #Assigns a 1 for the variable movement_speed to define the variable as the code continues to be executed 
    charge_time = 1 #Assigns a 1 for the variable charge_time to define the variable as the code continues to be executed 
    battery_distance = 1 #Assigns a 1 for the variable battery_distance to define the variable as the code continues to be executed 

distance = (int(input("How far is the mission in km?"))) #asks the user how far they would like to move on Mars and specifies that the value they need to enter should be in kilometres

charges_needed = math.floor(distance / battery_distance) #this math operation calculates how many times the rover's battery start with 100% with counts as one charge needed

if charges_needed < 1: #If no additional charge is needed the rover can make the trip without stopping to charge
    total_time = distance / movement_speed #Since no additional time is needed to charge the total time is simply the distance divided the speed of the rover
else: #This trip requires the batteries to be charged
    total_time = (distance / movement_speed) + (charge_time * charges_needed) #Since the batteries need to be charged we needed to calculate the time needed to charge them, along with the time to reach the destination and add those values together

storm_present = str(input("Is there a storm in the forecast(True or False)?")) # This input asks the user if there is a storm in the path of the rover

if storm_present == "True":  #This if statement checks if there is a storm in the forecast in the area
    total_time = total_time*1.2 #If there is a storm in the area we need to multiply the total time by 1.2 as it will take 20% longer to complete the journey
#Since we are assuming the user doesn't type anything but true and false, we can assume that if they didn't type true they typed false which doesn't require us to do anything else

# This print statement should be your final line of code.
# You may change the variable names or where the statement is placed within a logic block, but the rest of the statement should remain the same.

if rover_used < 4: #Checks if the rover selection made by the user is between one and three
    print(f'The total travel time for Rover {rover_used} to travel {distance:.1f} km is {total_time:.1f} hours.'.format(rover_used, distance, total_time)) #This part of the code prints out the statement if the rover selection made by the user was correct
else:
    print("Rover number not recognized.") #This tells the user that the rover number they have entered is not recognized