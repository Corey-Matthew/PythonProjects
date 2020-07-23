#!/usr/bin/env python3
import subprocess

cmd= "bash --version"

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

if rc == 0:
    for each_line in out.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()[3].split('(')[0])
else:
    print("Command failed and error is: ", err)


