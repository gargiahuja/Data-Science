import socket
#ek network k through connection banane k kaam aati h
try:
    #creating socket
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # dgram: data ka chhota packet jo ek jagha se dusri jagha bina connecion k bheja jata h
    #agar python socket programming me me udp socket banati hu tab yeh use hota h

    #INET: 

    print("Socket created")
    
    ip_add="192.168.73.93"
    port=888                                         #0-65535: range of port number koi bhi chooze krlo
    target_add=(ip_add,port)
    message=input("Enter the message: ")
    encoded_msg=message.encode("ascii")
    print("message sent successfuly! ")
    s.close()

except Exception as e:
    print("An Error occured")

