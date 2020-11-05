#this is a random name generator. 
import sys, random
import requests
import re 
from bs4 import BeautifulSoup
import bs4

#Printing 
print("This is a name generator. ")
origin = input("Input the name origin you are interested in: 1-Sweden 2-Germany 3-France 4-Spain 5-England: ")
value = input("Input a last name to see how it sounds with a random name: ")

#Figure out which origin user is interested in. 
if origin == '1':
	r = requests.get('https://nameberry.com/popular_names/Sweden')
elif origin == '2':
	r = requests.get('https://nameberry.com/popular_names/Germany')	
elif origin == '3':
	r = requests.get('https://nameberry.com/popular_names/France')	
elif origin == '4':
	r = requests.get('https://nameberry.com/popular_names/Spain')
elif origin == '5':
	r = requests.get('https://nameberry.com/popular_names/England')	
else:
	print("invalid input")

page = BeautifulSoup(r.text, 'html.parser') 

#create a list of names to put them into
names = []

#I don't know what this line does, but the program does not work without it.     
body = page.find('a',attrs={"class" : "flex-1"})

#find all names that I want and put them into a list
for body in page.find_all('a',attrs={"class" : "flex-1"}):
	for x in body:
		if isinstance(x, bs4.element.NavigableString):
        		names.append(x.strip())
        		
#strip the ''s from the list       		
names[:] = (value for value in names if value != '')

#take a name from the list and pair it with the lastname given 
while True:
	
	first = random.choice(names)
	print(first + " " + value)

	try_again = input("Press enter to try again, press q to quit ")
	
	if try_again == "q":
		break
	
print("Come again!")


