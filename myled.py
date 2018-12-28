#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess

def main():
	while True:
		print "input 0 ～ ∞:"
		number = input()

		if(number != 0):	
			led_cmd = "echo 1 > /dev/myled0"
			subprocess.call(led_cmd, shell=True)

			time.sleep(number)		

			led_cmd = "echo 0 > /dev/myled0"
			subprocess.call(led_cmd, shell=True)

		else:
			pass
				
if __name__ == "__main__":
	main()

		
