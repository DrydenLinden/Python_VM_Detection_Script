#!/usr/bin/env python3
import os




def windowsVMDetection():
	print("Detecting if in a  windows VM")


def linuxVMDetection():
	virtualization = os.system( "systemd-detect-virt")
	if virtualization == "none":
		print("Not in a Linux VM")
		return 0
	else: 
		print(virtualization)
		return 1



linuxVMDetection()