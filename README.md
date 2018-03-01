# Proyecto-OIDs
Scripts for obtaining QOS OIDs on Cisco interfaces
The proyect is a convoluted mess that probably only works in my environment. 
It was also my first time coding in Python after learning the basics.

The Process:

1.  In a linux machine open the excel QOS_Guatemala.xlsx and populate it with the data of the devices you want to pull information.
    The information needed includes hostname, device IP, SNMP server from which the walks will be done from and the snmp community.
2.  Run the python script PWSGuatemala.py to create a text file with the Powershell lines necesary to pull the devices snmp information required.
3.  Transfer the Powershell SNMP Script Guatemala.txt to a windows server with the permissions requirements to access the SNMP info of the devices.
    A coding change in the text file will probably be necessary.
4.  Copy the lines of the file from the last point into a Powershell window, this will create a file for each of the devices that were polled.
5.  Because of coding differeces between windows and linux, copy all the files generated in the last point into the directory "/Excels/Cambio de coding"
6.  Run the script touft8.py. This script will automatically change the unicode of the files and move them to the /Excels directory.
7.  Run the OIDExcelGuatemala.py script. This will populate the OID_Guatemala.xlsx file with the QOS OIDs for every interface of the routers involved.
8.  This last task is very specific for my requirement at the moment. Run the script Format_OIDExcelGuatemala.py.
    It goes through every interface polled and accoding to certain parameters labels them as an MPLS interface. 
    Those interfaces are copied the the last excel file OID-Guatemala_Core-MPLS.xlsx
