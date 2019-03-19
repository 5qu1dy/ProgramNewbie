#Program Pertama Oktavianus Krisna
#Halooo

import os
import time

os.system ('clear')
pembuka='''
##################################################
#	   Author	  : WWDZN._	    	 #
#	   Cyber Team	  : MOMB T34M	    	 #
#	   Special Thanks : Deni Ganz	    	 #
#			    dan semua member     #
##################################################
'''

os.system ('figlet Program1 | lolcat')
time.sleep(1)
print (pembuka)
time.sleep(0.5)

print ('Menu :')
menu='''
[1] Install Metasploit
[2] Install A-Rat
[3] DDOS
[4] Hack Instagram
[5] IP Tracer

[00] Close
'''

print (menu)
time.sleep(1)
pilihan=input('Masukkan Pilihan Anda : ')
if pilihan=='1' or pilihan=='01':
   os.system ('figlet Metasploit | lolcat')
   time.sleep(1)
   os.system ('apt upgrade && apt upgrade;apt install wget;wget https://Auxilus.github.io/metasploit.sh')
elif pilihan=='2' or pilihan=='02':
     os.system ('figlet A-Rat | lolcat')
     time.sleep(1)
     os.system ('apt update && apt upgrade;apt install git python python2;git clone https://github.com/Xi4u7/A-Rat')
elif pilihan=='3' or pilihan=='03':
     os.system ('figlet DDOS | lolcat')
     time.sleep(1)
     os.system ('apt install git;apt install python;git clone http://github.com/cyweb/hammer')
elif pilihan=='4' or pilihan=='04':
     os.system ('figlet InstaHack | lolcat')
     time.sleep(1)
     os.system ('apt update && apt upgrade;apt install python2;apt install git;git clone https://github.com/Senitopeng/instabot.git')
elif pilihan=='5' or pilihan=='05':
     os.system ('figlet IP Tracer | lolcat')
     time.sleep(1)
     os.system ('apt install python;apt install git;git clone https://github.com/maldevel/IPGeoLocation')
elif pilihan=='0' or pilihan=='00':
     print ('Terima Kasih Telah Menggunakan Tools Saya :)')
     time.sleep(1)
     print (' ')
else:
    print ('ERR0R: Wrong Input...!!!')
    time.sleep(1)
