#!/usr/bin/python3

# RPI_RP2 custom upload script by wurmtal868


# from genericpath import exists
import serial, sys
from pathlib import Path
import os,time

# Check if the second argument exists
try:
    flashpath = sys.argv[2]
except:
    print ("ERROR: Path to RPI_RP2 missing")
    exit(1)

# Check if the first argument is a uf2 file

if (os.path.isfile(sys.argv[1])):
    fwFile=sys.argv[1]
    #Change extension to "uf2" and hope it exists ;o)
    if fwFile[-3:] != "uf2":
        fwFile = fwFile[:-3]+"uf2"
else:
    fwFile=""
if not (os.path.isfile(fwFile)):
    print("ERROR: FW file is missing or does not exist")
    print ("Usage: %s <FW_File> <Path_to_RPI_RP2>" %(sys.argv[0]))
    exit(1)

print ("Uploading:"+ fwFile)

#Get alist of serial ports of a Pico-Pi
ports=Path("/dev").glob("ttyA*")
liste=[]
for port in ports:
    print(port)
    liste.append("%s" %port)

if liste ==[]:
    print("no serial port found!")

#If list is not empty try to reset each port using 1200 baud
else:
    for serialPort in liste:
            
        print ("Trying to reset RPI_RP2 on %s" %(serialPort))
        
        try:
            ser = serial.Serial(serialPort,1200,parity=serial.PARITY_NONE, rtscts=1)
            ser.setDTR(False)
            if (ser.isOpen()):
                print("Sucess")    
                ser.close() # always close port
                wait=10
#Check if INFO_UF2.TXT" appears for 10 seconds maximum
                while (wait>0):
                    if (os.path.isfile("%s/INFO_UF2.TXT" % (flashpath))):
                        break
                    time.sleep(1)
                    wait = wait-1
                    print("waiting..")

            else:
                print("Can't open ",serialPort)
        except:
            pass
#Try to copy the the UF2 FW to the flashpath 
#even if the Pico is in BOOTSEL mode and no serial port was found
if (os.path.isfile("%s/INFO_UF2.TXT" % (flashpath))):
    command = ("cp %s %s" % (fwFile,flashpath))
    print(command)
    os.system(command)
else:
    print("could not find RPI_RP2 on %s" %(flashpath))
    exit(2)
