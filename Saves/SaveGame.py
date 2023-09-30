import os

def GetSaveFilePath():
    current_save_dir = os.path.join(__file__, "..", "Current")
    save_file = os.listdir(current_save_dir)[0]
    return os.path.join(current_save_dir, save_file)

def Load():
    save_file = GetSaveFilePath()
    save_data = ""
    with open(save_file, encoding='utf-8-sig') as file:
        save_data = file.read()
    return save_data

def Save(save_data: str):
    save_file = GetSaveFilePath()
    with open(save_file, encoding='utf-8-sig') as file:
        return file.write(save_data)
