import req
req.used()

from resemblyzer import VoiceEncoder
import torchaudio
import API
import recorder
import random
import json
import time
import os
import isai
from utills import utills as ustills
import block
import Warnings as warnings
import add_num
import Warnings as warns


utills = ustills()
utills.startup_files()

warn = warnings.ErrorCollector()


def sign_up():
    goi =None
    print("What's your Username?")
    username = input(": ")
    
    print("\nYou will have 4 seconds to record your voice sample.")
    print("Recording starts in...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    user_id = int(add_num.plus())

    filename = str(user_id) + ".mp3"
    recorder.recorder(4, filename)
    
    if isai.isai(filename) ==True:
        print("❌ AI-generated voice detected. Please try again with a natural voice.")
        goi =True
    else:
        goi =False
    dicts ={}
    if os.path.exists("VRC.json"):
        with open("VRC.json", "r") as f:
            datas = json.load(f)
    else:
        datas = {"VRC": []}
    if goi==False:
        diffvalue =datas.keys()
        for i in diffvalue:
            if i == username:
                print("❌ Username already exists.")
                exit(1)
        datas["VRC"].append({username: filename})

    if goi:
        data = utills.add_ban_setting()
        datas =data

    with open("VRC.json", "w") as f:
        json.dump(datas, f, indent=4)
    if goi:
        os.remove(filename)
        exit(1)
    print(f"✅ Signup complete for {username}")

def login():
    gou =None
    print("\nWhat's your Username?")
    username = input(": ")

    if not os.path.exists("VRC.json"):
        print("❌ No registered users found.")
        return False

    with open("VRC.json", "r") as f:
        datas = json.load(f)

    user_file = None
    for entry in datas.get("VRC", []):
        if username in entry:
            user_file = entry[username]
            break

    if not user_file:
        print("❌ Username not found.")
        return False

    print("\nYou will have 4 seconds to record your login voice sample.")
    print("Recording starts in...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Recording your voice...")
    recorder.recorder(4, "pass.mp3")
    if isai.isai("pass.mp3") ==True:
        data = utills.add_ban_setting()
        
        print("❌ AI-generated voice detected")
        gou =True
    if gou !=True:
        print("\n🔍 Checking voice match...")
        match_result = API.main(user_file, "pass.mp3")
        if match_result == True:
            return True
        elif match_result == False:
            print("❌ Login failed, please try again.")
            return False
    os.remove("pass.mp3")
    
def main():
    while True:
        print("\nWelcome to the VRC!")
        print("1. Sign up with voice")
        print("2. Login with voice")
        print("3. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                sign_up()
                os.system("cls|clear")
            case "2":
                res = login()

                if res == True:
                    print("✅ Login successful!")
                    exit(0)
                elif res == False:
                    time.sleep(4)
                    os.system("cls|clear")

            case "3":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice, please select 1, 2, or 3.")
                

if __name__ == "__main__":
    if block.block():
        warn.fancy_error(warns.FancyError.AIDECT, raise_error=True ,details=True)
        exit(1)
    main()
