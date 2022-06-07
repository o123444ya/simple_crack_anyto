import winreg,ctypes, sys,time
#Made By Huanxiang
#https://fb.com/o123444ya
def DEL_TEL(reg):
    try:
        winreg.DeleteValue(reg, 'Teleport')
        print('\n[+]\nDetected Teleport Data\nCleared.')
    except:pass
def DEL_JOY(reg):
    try:
        winreg.DeleteValue(reg, 'Joystick')
        print('\n[+]\nDetected Joystick Data\nCleared.')
    except:pass
def DEL_WAL(reg):
    try:
        winreg.DeleteValue(reg, 'Walk')
        print('\n[+]\nDetected Walk Data\nCleared.')
    except:pass
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print('Get UAC Access.\nStart.')
    while 1:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\iMyfone\\AnyTo', access=winreg.KEY_WRITE) as reg:
                DEL_TEL(reg)
                time.sleep(.5)
                DEL_JOY(reg)
                time.sleep(.5)
                DEL_WAL(reg)
                time.sleep(.5)
        except KeyboardInterrupt:exit('Ctrl-C')
        except:pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
