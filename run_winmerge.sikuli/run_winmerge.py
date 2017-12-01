import subprocess

winmerge_exe = '"C:\\Program Files\\WinMerge\\WinMergeU.exe"'

compare_source = "C:\Sourcecode\source_folder"
compare_target = "C:\Sourcecode\target_folder"

command = winmerge_exe + " " + compare_source + " " + compare_target + "\n"
print command
subprocess.Popen(command, shell=True)
