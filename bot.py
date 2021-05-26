from __future__ import print_function
print("request recived, script start:")
from colors import *
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m' 
BOLD = '\033[4m'  
RESET = '\033[0m'  
BLINK = '\033[5m'
print( RED + BOLD + 'start runing:' + RESET)
print('first number:')
first = float(input())
print('the operators=>>\n1. +\n2. -\n3. *\n4. /\nChoose one:')
symbol = input()
if symbol=="1" :
    print('your input is +')
    symboll="+"
elif symbol=="2" :
    print('your input is -')
    symboll="-"
elif symbol=="3" :
    print('your input is *')
    symboll="*"
elif symbol=="4" :
    print('your input is /')
    symboll="/"
else:
    print(color("Error, Wrong input for operator!",'red','white',style='blink2'))
    sys.exit(1)

print('the second number:')
second = float(input())
if symbol=="1" :
    result= first + second
elif symbol=="2" :
    result= first - second
elif symbol=="3" :
    result= first * second
elif symbol=="4" :
    result= first / second
else:
    pass
firststr=str(first)
secondstr=str(second)
print(type(result))
print( firststr + symboll + secondstr + "=" + color(result,'black','yellow',style='blink') )
print("</class>")
print( BLINK +"finish"+RESET)
