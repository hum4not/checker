import sys
import os
import requests as req
import getpass

name = getpass.getuser()
clear = lambda: os.system('cls')

def main():
    addRed=False
    os.system('color ' +'c'+ " & cls & title FREE SERVER INFO CHECKER - github.com/hum4not")
    print("SERVER INFO CHECKER (c) HMNT Development, humanot")
    print("Version 1.0 BETA")
    ip = input(f"Hello, {name}\n[?] Enter the ip: ")
    print("\n=======================================")
    resp = req.request(method='POST', url="http://" + ip + "/growtopia/server_data.php")
    print(resp.text)
    print("=======================================\n")
    input("PRESS ENTER TO GET IN THE MAIN MENU...")
    clear()
    main()
    
main()
