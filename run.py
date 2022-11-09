import os
from babas import makedirectory as run64

if "64" in str(os.system("uname -m")):
   run64()
else:
   run32()

