print("\n Welcome to the Astronauts in Space Tool. \n")
print("\n With this tool, you will receive information about the three astronauts currently working in space.\n")

print("\n ------------------------------------------------------------------------------\n")
#Print the number of spacecrafts active
print ("\n There is currently one spacecraft active. The International Space Station - ISS. \n")
#Create a display showing the number of astronauts
print ("\n There are currently three international astronauts currently assigned to the The International Space Station. \n")
#Print each spacecraft and the astronaut assigned to it. ##Need to add a loop but there was just one space craft??# Not sure what to do.
print ("\n The names, assigned spaceship, ages, genders and nationalities of these three adventurous space cadets are as follows: \n")

# Add demographic data dictionaries (name, country, age, gender and print out
astronauts = {'Anton Shkaplerov': 'ISS', 'Scott Tingle': 'ISS', 'Norishige Kanai': 'ISS'}

Country_of_Origin = {'Anton Shkaplerov': 'Russia' , 'Scott Tingle': 'USA', 'Norishige Kanai': 'Japan'}

age = {'Anton Shkaplerov': '46', 'Scott Tingle':  '52', 'Norishige Kanai': '41'}

gender = {'Anton Shkaplerov': 'Male' , 'Scott Tingle': 'Male', 'Norishige Kanai': 'Male'}, 

#Print out of assigned craft,age, gender, origin using dictionaries

craft = {}
craft['Anton Shkaplerov'] = 'ISS'
craft['Scott Tingle'] = 'ISS'
craft['Norishige Kanai'] = 'ISS'
print (craft)

ages = {}
ages['Anton Shkaplerov'] = 46
ages['Scott Tingle'] = 52
ages['Norishige Kanai'] = 41
print (ages)

gender = {}
gender['Anton Shkaplerov'] = 'Male' 
gender['Scott Tingle'] = 'Male' 
gender['Norishige Kanai'] = 'Male'
print (gender)

Country_of_Origin = {}
Country_of_Origin['Anton Shkaplerov'] = 'Russia'
Country_of_Origin['Scott Tingle'] = 'USA'
Country_of_Origin['Norishige Kanai'] = 'Japan'
print (Country_of_Origin)


print("\n --------------------------------------------------------------------------\n")  

#Printing out astonaut details as a list.

print ("\nHere the astronauts are clearly listed: \n")
    
def astronaut1_details():
    name, age = "Anton Shkaplerov", 46
    origin = "Russia"
    gender = "Male"
    craft = "International Space Station"
    print("Name: {}\nAge: {}\nOrigin: {} \nGender: {} \nAssigned_Craft: {}".format(name, age, origin, gender, craft))

astronaut1_details()

print("\n ------------------------------------------------------------------------- \n")


def astronaut2_details():
    name, age = "Scott Tingle", 52
    origin = "USA"
    gender = "Male"
    craft = "International Space Station"
    print("Name: {}\nAge: {}\nOrigin: {} \nGender: {} \nAssigned_Craft: {}".format(name, age, origin, gender, craft)) 

astronaut2_details()

print("\n --------------------------------------------------------------------------\n")


def astronaut3_details():
    name, age = "Norishige Kanai", 41
    origin = "Japan"
    gender = "Male"
    craft = "International Space Station"
    print("Name: {}\nAge: {}\nOrigin: {} \nGender: {} \nAssigned_Craft: {}".format(name, age, origin, gender, craft)) 

astronaut3_details()

# Goodbye/exit messageprompt

print("\n Thank you for trying our Astronauts in Space Tool. You can find more fun Python projects at: https://codeclubprojects.org/en-GB/python/iss/. Good-bye! \n")





