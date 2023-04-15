#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 2 (Item 3:The Vigenère Cipher)

#Imports necessary elements
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#Prompts user input for message and key
message = input(str('Write your message: ')).lower()
key = input(str('Write your key: ')).lower()

#instantiates list for conversion
output_1=[]
output_2=[]

#Repeats the key until its' length is the same as the message
#converts the message into numbers and added to a list
#converts the key into numbers and added to a list
#adds the two list together
#Computes the mod 26 from the result
#Converts into ciphertext
#Prints and animates the final output