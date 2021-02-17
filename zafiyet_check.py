#!/usr/bin/env python
import os
import time

try:
    os.system("clear")
    os.system("sudo apt install nikto")
    os.system("clear")
    os.system("figlet Prime Vulnerability Scanner")

    print("""
          ______________________________________
         /                                      \\
        |          Port Scanner BY : Prime       |
        |       Prime: KARABAGH IS AZERBAIJAN    |
         \\                                      /
          --------------------------------------

    """)
    target_ip = raw_input("Hedef IP veye hedef site :: ")
    os.system("sudo nikto -h " + target_ip)
	


except KeyboardInterrupt:
    for i in range(0,6):
        os.system("clear")
	print("\nProgram Ending" + "."*i)
        time.sleep(0.4)
    print("Program ended")
