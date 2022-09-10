import os
import colorama

#Colors
def green(txt):
    print("\033[32m{}".format(txt))

def white():
    print("\033[0m")

init()

iplistpath = input("Path to ip list\n>> ")
iplist = open(iplistpath,"r")
timeout = input("Response waiting time\n>> ")

pwd = os.getcwd()
lines  = iplist.readlines()

itr = 0

for line in lines:
    os.system("mkdir fs" + str(itr))    
    os.system("timeout "  + timeout + " curlftpfs ftp://" + line.strip() + " fs" + str(itr))
    print("[" + green("+") + white("]") + " fs number "  + str(itr) + " (" + line.strip() + ")" + " done")
    itr += 1

remove = input("Remove the file system(y/N)\n>> ")

if remove == "y":
    os.system("sudo umount " + pwd + " fs*")
    os.system("sudo rmdir " + pwd + "fs*")
