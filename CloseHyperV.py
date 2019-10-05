from __future__ import print_function
from subprocess import Popen, PIPE, STDOUT
import ctypes, sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():

    '''	write your code below	'''

    os.system("echo 禁用Hyper-V服务...")
    os.system("bcdedit /set {current} hypervisorlaunchtype OFF")
    os.system("Dism /online /Disable-Feature /FeatureName:Microsoft-Hyper-V-All /FeatureName:Microsoft-Hyper-V /FeatureName:Microsoft-Hyper-V-Tools-All /FeatureName:Microsoft-Hyper-V-Management-PowerShell /FeatureName:Microsoft-Hyper-V-Hypervisor /FeatureName:Microsoft-Hyper-V-Services /FeatureName:Microsoft-Hyper-V-Management-Clients")

else:
    if sys.version_info[0] == 3:
    	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)