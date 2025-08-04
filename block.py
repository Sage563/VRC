import json

def block(filepath="VRC.json"):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return False
        settings = data.get("settings")
        if not isinstance(settings, list):
            return False
        for entry in settings:
            if isinstance(entry, dict) and "ban" in entry:
                return entry["ban"].get("ban", False)
            
        return False

    except FileNotFoundError:
        print(f"❌ File {filepath} not found.")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
        return False
