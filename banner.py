import socket
IP = input("Introduce la direccion IP: ")
puertos = input("Introduce un rango de puertos con esta mascara 100-1000:  ")
Pinicio,Pfinal = puertos.split('-')
Pinicio = int(Pinicio);Pfinal = int(Pfinal)
for puerto in range(Pinicio,Pfinal+1):
 try:
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    con.connect((IP,puerto))
    banner = con.recv(2048).decode()
    con.close()
    print("Socket",IP,":{} abierto".format(puerto))
    print(banner)
 except:
     print("Socket",IP,":{} Cerrado".format(puerto))
