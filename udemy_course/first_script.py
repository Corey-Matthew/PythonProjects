#!/usr/bin/env python3

import mymodule
import math
import platform
import getpass
import sys

print(mymodule.string)
print(math.pi)
print(f"This is {platform.system()} os")
print(f"Python versoin is: {platform.python_version()}")
print(platform.machine())
print(platform.processor())
print(platform.uname())

print(getpass.getuser())

print(sys.platform)
print(platform.system())
print(sys.version)
print(sys.version_info)
print(sys.argv)
