import json
import os

class utills():
    def init(self):
        self.value =None
    def add_ban_setting(self , filepath="VRC.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            if not isinstance(data["settings"], list):
                print("⚠️ 'settings' is missing or not a list.")
                return False
            for entry in data["settings"]:
                if isinstance(entry, dict) and "ban" in entry:
                    print("ℹ️ 'ban' setting already present. No changes made.")
                    return True
            data["settings"].append({"ban": {"ban": True}})
            return data
        except FileNotFoundError:
            print(f"❌ File '{filepath}' not found.")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}")
            return False
        

    def startup_files(self):
        file ="""{
    "name": "VRC",
    "version": "1.0.0",
    "description": "A JSON file for VRC configuration",
    "VRC": [
        {}
    ],
    "settings": [
        {
            "counter": {
                "counter": -1
            }
            
        }
    ]
}"""
        val = True if os.path.exists("VRC.json") else False
        if val == False:
            with open("VRC.json", "w") as f:
                f.write(file)
        else:
            pass
