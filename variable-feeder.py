#!/usr/bin/env python3

import os

print("VF1=I AM VF1")
print("VF2=I AM VF2")

os.write(2, b'VF_ERR=I AM VF_ERR\n')
os.write(2, b'I am just a simple error message.\n')
