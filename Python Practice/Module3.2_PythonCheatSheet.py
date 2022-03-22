# 3.2.2 Print Hello World
# print("Hello World")

#3.2.3 The type() function is used to determine data type
#type(3.1)

#3.2.5 Lists
#counties = ["Arapahoe","Denver","Jefferson"]
#List = [] or =list() #Tuples = () or =tuples()  #Dictionaries = {} or dict()

#print(counties) #print entire list
#print(counties[0]) #print index 0 of 0-1-2 indexed list

#Negative indexes are used to identify a list item's position relative to the end of the list
#print(counties[-1]) # -1 is the last index, -2 is second to last index, so on so forth

#len() = Will give you total number of items in the list
#print(len(counties)) #Returns 3 because there are 3 items in the list

#slicing a list will return certain values in the list
#print (counties[0:2]) #will return the 1st and 2nd items - looking from 0 to 2 returns 0 & 1
#print(counties[0:1]) #will return the 1st only, looking from 0 to 1, returing only 1
#print(counties[ :2])  #wil return first to second, or 0 & 1

#insert and remove from list - use append(add to end of list)
#insert and remove from list - use .insert (index , object) or .remove
#Remove using .remove(obj) - Removes based on object
#pop(index) - removes based on index number - () to removed last

#counties.insert(2,"El Paso") #will insert El Paso to the 3rd item in the list
#counties.remove("El Paso")
#print(counties)

#Change an element in a list - list[index]="object"
#counties[2] = "El Paso" #Changes idex 2 from "Jefferson" to "El Paso"
#print(counties)

#3.3.6 Tuples
#List = []  #Tuples = ()  #Dictionaries = {}
#tuples are immutable: Declare Tuples - My_Example = tuple()

#counties_tuple = ("Arapahoe","Denver","Jefferson")
#You can use searching like in a list
#print(len(counties_tuple)) #Returns index size of tuple = 3 indexes
#print (counties_tuple[0]) #Returns index 0 or number 1 index
#print(counties_tuple[:2]) #Returns index inside 0-2 = 0 & 1 

#3.2.7 Dictionaries - This is a hard one
#Python dictionary has a key and a value, or key-value pairs.
#Key-value pairs are enclosed in a set of curly braces {}
#Syntax = {key1:value1, key2:value2, .... ,keyN:valueN}
#Create Dictionary - My_Example = {} or dict()
#List = [] or =list() #Tuples = () or =tuples()  #Dictionaries = {} or dict()


#Lets Create a Dictionary and add KEY:VAlues one by one
#counties_dict = {} #create empty dictionary
#counties_dict["Arapahoe"] = 422829 #Adds Key and Value as first item in dictionary
#print(counties_dict)
#counties_dict["Denver"] = 463353 #Adds Key and Value as 2nd item in dictionary
#print(counties_dict)
#counties_dict["Jefferson"] = 432438 #Adds Key and Value as 3rd item in dictionary
#print(counties_dict)

#alternatively create all at once
#counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson":432438}
#print(counties_dict)

#Searching in Dictionaries Continued
#we can use the items() method on the dictionary. This will return a list of tuples where the first element in each tuple is the key of the dictionary, and the second element in each tuple is the value corresponding to that key.
#counties_dict.items()
#To get only the keys from a dictionary, add the keys()
#counties_dict.keys()
#To retrieve only the values from a dictionary, add the values()
#counties_dict.values()

#Getting Specific Values from Dictionaries
#There are two methods you can use to get a specific value from a dictionary.
#With the get() method, we pass a key inside the parentheses to "get" the value of that key.

#counties_dict.get("Denver") #Gets the Value of a Key
#print(counties_dict.get("Denver"))

#Or you can use the syntax My_Example[key] to get the valye of a Key
#counties_dict["Denver"]
#print(counties_dict["Denver"])

###LIST OF DICTIONARIES
# Sometimes Python dictionaries have the same keys associated with different values, which are written in this format
# Example - [{key1:value1, key2:value2}, {key1:value3, key2:value4}]
# This is referred to as a list of dictionaries because each dictionary, {}, is wrapped in brackets.

### Let's create a list of dictionaries where the keys are "county" and "registered_voters," and each county and its corresponding registered voters are the values for those keys.
# Keys are county & registered_voters

## First create list called voting data
#voting_data = [] #this is a list, a dictionary would be {} and a tuple would be () or =tuple()
#Now insert or append each dictionary to the list

#This is the append method
#The dictionary 1 = key = "county" and value ="county name"
#The dictionary 2 = key is "registered_voters" and value = # of voters

#Add first list of dictionary
#use append(add to end of list)
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#print(voting_data)

##Add second list of dictionary
##Now use insert method rather than append method
##insert and remove from list - use .insert (index , object)
##This is the second item, so index 1
#voting_data.insert(1,{"county":"Denver", "registered_voter": 463353})
#print(voting_data)

### add 3rd list of dictionary
#voting_data.insert(2,{"county":"Jefferson", "registered_voter": 432438})
#print(voting_data)

##This is a list of dicionaries - each element or index is a dictionary
##What is list index 0?
#print(voting_data[0])
##It is the first dictionary -> {'county': 'Arapahoe', 'registered_voters': 422829}

##Notes on If Else 
#temperature = float(81)
#if temperature > 80:
    #print("Guhhhhhh")
#else:
    #print("Goooooo")

###Convert 80F to C
#TempF = float(80)
#TempC = (TempF - 32) * (5/9)
##Format using F" f'{value:{width},.{precision}}'
#print(f"{TempC:,.2f}")

##Notes on elif - If Else in one statement
## What is the score?
#  input() will ask you in the termial to input a value
#score = int(input("What is your test score? "))

## Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
    #print('Your grade is a C.')
#elif score >= 60:
    #print('Your grade is a D.')
## !!! Last else is not a if else or elif
#else:
    #print('Your grade is an F.')

## Notes on Logical Operators (in // not in)
#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")

### !!!! how to comment out code - Command plus /

# # Notes on Logical Operators (and // or // not)
# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

### 3.2.10 Repetition Statements
### Loops
### A condition-controlled (while-loop) loop uses a true or false condition to control the number of times that it repeats
### A count-controlled (for-loop) loop repeats a specific number of times depending on the conditions
##While Loop Example
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1 #Should equal 1 - 5

#For Python_Practice.py Files examples in 3.2.10
# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#the county variable is declared and set equal to the first item in the list of counties, "Arapahoe." Then we print the first item, "Arapahoe," to the screen. For the second iteration
    # print(county)

## Range can be a useful tool in For Loops
## Numbers = [0,1,2,3,4,5] is the same as range(4)
# for num in range(5):
#     print(num)

## You can also use indexing to filter through lists ranges
# for index in range(len(counties)):
#     print(counties[index])

## Iterate through a dictionary
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#To retreave keys - for loops default to keys
# for county in counties_dict:
#     print(county)

# #You can also specify Keys using counties_dict.keys()
# # Or specify values using counties_dict.values()
# for county in counties_dict.keys():
#     print(county)

# # Specify values using counties_dict.values()
# for voters in counties_dict.values():
#     print(voters)


## When using the format dictionary_name[key], 
# include the key county in the for loop in the print statement. 
# This will return the VALUE of the key in the output
# for county in counties_dict:
#     print(counties_dict[county])

## Or you can use the get() function to get values from keys
# for county in counties_dict:
#     print(counties_dict.get(county))

#!!!!!!!!!!!!
## This is important - Getting KEY-VALUE Pairs in a Dictionary
## for key, value in dictionary_name.items(): ---> print(key, value)
## Use the .items() method --> The items() method returns a view object. 
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
# When iterating over a dictionary:
# The first variable declared in the for loop is assigned to the keys.
# The second variable is assigned to the values.

# for county, voters in counties_dict.items():
#     print(str(county) + " county has" , str(voters) + " registered voters")

# Arapahoe county has 422829 registered voters
# Denver county has 463353 registered voters
# Jefferson county has 432438 registered voters

###Iterate Through a List of Dictionaries
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

### Use nested loop 
## Loop 1 --> Interate over Dictionary # in List
## Dictionary #1 in voting_data List = "county":"Arapahoe", "registered_voters": 422829}
## Dict #1 --> Key #1 = County  -  Value #1 = Arapahoe
## Dict #1 --> Key #2 = registered_voters  -  Value #2 = 422829
## Dict #2 --> Key #1 = County  -  Value #1 = Denver
## Dict #2 --> Key #2 = registered_voters  -  Value #2 = 463353
## Dict #3 --> Key #1 = County  -  Value #1 = Jefferson
## Dict #3 --> Key #2 = registered_voters  -  Value #2 = 432438

# for county_dict in voting_data: #Loops through dictionary
#     for value in county_dict.values(): #Loops through Values - Values are example --> Arapahoe and 422829
#         print(value)

#If we only want to print the county name from each dictionary,
# for county_dict in voting_data:
#     print(county_dict['county'])

#If we only want the voter values
# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

#######################
#######################
###!!!!SKILL DRILL 3.2.11
#######################

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#Print each county and registered voter from the dictionary.
#count_dict = dictionary #s
for county_dict in voting_data:
    county = county_dict.get('county')
    voters = county_dict.get('registered_voters')
    print(f'{county} county has {voters:,} registered voters.')




