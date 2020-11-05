# -*- coding: utf-8 -*-

#############################################
# author : Baptiste PICARD 		 			#
# date : 05/11/2020							#
# last modif : 05/11/2020					#
# contact : dev.baptpicxdev@gmail.com		#
# 								 			#
# overview : Main code.						#
#############################################

## Imports
import math
import datetime

## Librairies

## Functions 
def get_pi() :
	return math.pi
 
## Main script
if __name__ == '__main__':
	start_time = datetime.datetime.now()
	print("Starting the script.")
	print(get_pi())
	print("End of the script. It takes : {} secs.".format((datetime.datetime.now()-start_time).seconds))