from art import tprint as t
import socket
from prettytable import PrettyTable
g = '\033[92m' 
y = '\033[93m' 
r = '\033[91m' 
w = '\033[0m' 
L=[]
print(g)
t("ANONIM \nHACKER")
####################################
def ps(ip,port):
    internet=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        internet.connect((ip,port))
        print(y,f"                                                                                                                  {port}  PORT OCHIQ !")
    except:
        pass
        print(r,f"{port} PORT YOPIQ *")
    else:
        L.append(port)    
####################################
print(y)
ip=input("  [#] Nishon IP manzilini kiriting >  ")
d=int(input("  [#] Nechanchi portgacha skaynerlamoqchisiz (masalan : 80 ) \n  Raqam kiriting >>> "))
for port in range(1,d+1):
    ps(ip,port)
M = PrettyTable()    
M.field_names = [" NISHON * "," OCHIQ PORTLAR "]
M.add_row([ip,L])
print(g,">>>>>            NATIJALAR               <<<<<")
print(w,M)
print(f"{d} ta port skaynerlandi ")