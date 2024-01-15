#!/usr/bin/python3
import os
import platform
import re
def print_interfaces():
    if platform.system() == "Windows":
        os.system('powershell Get-NetAdapter -Name *')
    elif platform.system() == "Linux":
        os.system("ip a | grep -E '[0-9]+:\s(\w+):'")
    select = input ('Enter the interface name: ')
    return select
def change_mac():   
    if platform.system() == "Windows":
        interface = print_interfaces()
        mac = input("Enter your spoofed mac")
        os.system('powershell Set-NetAdapter -Name "'+interface+'" -MacAddress "'+mac+'"')
    elif platform.system() == "Linux":
        os.system("sudo ip link set dev "+interface+" address "+"mac")
    print ("Mac changed to: "+mac)
