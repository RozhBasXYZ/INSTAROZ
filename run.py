import os

try:
   from data.instarozh import makedirectory as main
   main()
except:
   from data.instarozh32 import makedirectory as main2
   main2()
