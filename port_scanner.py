#!/usr/bin/env python3.8
import os
import time

try:
	os.system("clear")
	os.system("sudo apt install figlet")
	os.system("clear")
	os.system("figlet Prime Port Scanner")

	print("""
	  ______________________________________
	 /			             	\\
	|          Port Scanner BY : Prime       |
	| 	Prime: KARABAGH IS AZERBAIJAN    |
	 \\                                      /
	  --------------------------------------

	1) I Seviyye Tarama
	2) II Seviyye Tarama
	3) III Seviyye Tarama

	""")

	inputs = int(input("Tarama hangi seviyyede olsun : "))


	if inputs == 1:
		target_ip = input("Hedef IP ::")
		os.system("sudo nmap " + target_ip)

	elif inputs == 2:
		target_ip = input("Hedef IP :: ")
		udp_scann = int(input("UDP taramasi da istiyormusun? (1 yes,2 no) :: "))
		if udp_scann == 1:
			os.system("sudo nmap -sS -sV -sU " + target_ip)
		else:
			os.system("sudo nmap -sS -sV " + target_ip)
	
	elif inputs == 3:
		target_ip = input("Hedef IP :: " )
		udp_scann = int(input("UDP taramasi da istiyormusun? (1 yes,2 no) :: "))
		if udp_scann == 1:
			os.system("sudo nmap -O -A -sS -sV -sU " + target_ip)
		else:
			os.system("sudo nmap -O -A -sS -sV " + target_ip)
			
	
	else:
		a = list("Boyle bir komut yok... Yeniden basladikda bu komutlari deneyin : 1, 2, 3...")
		b = ""				
		for i in a:
			b = b+i
			os.system("clear")
			
			os.system("echo "+ b)
			time.sleep(0.1)
		time.sleep(3)
		os.system("./port_scanner.py")
		quit()

except KeyboardInterrupt:
	for i in range(0,6):
		os.system("clear")		
		print("\nProgram Ending" + "."*i)
		time.sleep(0.4)
	print("Program ended")
		