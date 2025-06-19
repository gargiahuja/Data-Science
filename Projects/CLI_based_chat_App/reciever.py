import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Socket created")
    #sender k andar ip address reiever ka hi aayega 
    #humesha and reciever ka hi aayega khud ka
    #reciever k andar uska hi aayega
    ip_add="192.168.73.50"
    port= 3333                                         #0-65535: range of port number koi bhi chooze krlo
    complete_add=(ip_add,port)
    s.bind(complete_add)
    #bind combine krne k liye kaam aara h!!
    while True:
        message,sender_address=s.recvfrom(1024) #1024 is the bytes limit
        print("Raw Message ",message)
        print("Sender Address ",sender_address)

        decoded_msg=message.decode("ascii")
        print("Message",decoded_msg)

except Exception as e:
    print("An error has occured! ",e)