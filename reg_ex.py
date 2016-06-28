#!/usr/bin/python

import os
import re

new_reg_ex = re.findall("ab*c", "ac")
new_reg_ex_2 = re.findall("a..c", "abbc")

print new_reg_ex
print new_reg_ex_2
