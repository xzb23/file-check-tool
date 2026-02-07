import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", reserved=0, access=winreg.KEY_READ)
data_path = winreg.QueryValueEx(key, "Filecheck_Aza_path")[0] + "data"

def init_config():
    with open(data_path, "w", encoding="utf-8") as f:
        f.writelines(["0\n0"])