#!/data/data/com.termux/files/usr/bin/bash
echo -e "\n Sedang Menginstall Module Yang Diperlukan\n"
echo -e "\n install pkg update and pkg upgrade ...\n"
pkg update -y && pkg upgrade -y
echo -e "\n install new repository: tur-repo ...\n"
pkg install tur-repo -y && pkg update -y
echo -e "\n install package and dependencies ...\n"
pkg install git nano openssl play-audio binutils build-essential python3.10 -y
echo 'alias python3="python3.10"' >> $PREFIX/etc/bash.bashrc
echo 'alias pip="python3.10 -m pip"' >> $PREFIX/etc/bash.bashrc
source $PREFIX/etc/bash.bashrc
echo -e "\n cloning github repository -> 'instaroz' ...\n"
git clone https://github.com/RozhBasXYZ/INSTAROZ
echo -e "\n install module and requirements ...\n"
cd INSTAROZ && python3.10 -m pip install --upgrade pip && python3.10 -m pip install wheel && python3.10 -m pip install -r requirements.txt
find data/ -name '*.md' -delete
echo -e "\n sedang melakukan build.py"
python3.10 build.py
echo -e "\n build sukses, berikan izin storage ( y / izinkan )"
termux-setup-storage
echo -e "\n sukses memberikan izin, sc segera siap..."
cd /sdcard && mkdir STAROZ 
python3.10 run.py
