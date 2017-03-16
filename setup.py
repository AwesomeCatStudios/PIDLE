#from cx_Freeze import setup, Executable

#setup(name = "idlelauncher" ,
'''      version = "1.5" ,
      description = "pidle is an idle" ,
      executables = [Executable("idlelauncher.py",base="Win32GUI",
      targetName="Product.exe")],scripts=["idleconfig.py","idletools.py","runaction.py"])
'''
import sys
from cx_Freeze import setup, Executable
include_files = [r"C:\Python 3.5\DLLs\tcl86t.dll",
r"C:\Python 3.5\DLLs\tk86t.dll"]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","subprocess","webbrowser","shlex"], "excludes": [],"include_files":include_files}

#,"idleconfig","idletools"
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifidle",
        version = "1.5",
        description = "fidle an idle",
        options = {"build_exe": build_exe_options},
        executables = [Executable("idlelaunch.py", base=base)])
