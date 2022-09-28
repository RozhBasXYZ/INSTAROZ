import os

print("[\033[92m!\033[00m] memeriksa update terbaru......")
try:
	os.remove("run32")
	os.remove("run64")
	os.remove("test32")
	os.remove("test64")
except:pass
os.system("git pull")
