#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()

        print('Request received:')
        request = str(recvSocket.recv(2048), 'utf-8') 
        #proceso petición y veo que me piden. Hago lo que me piden
        print(request)
        print('Answering back...')
        info = request.split(' ')[1]

        if len(info.split('/')) == 4: 
            numero1 = float(info.split("/")[1])
            operacion = info.split("/")[2]
            numero2 = float(info.split("/")[3])
        
        resultado = calculadora.funciones[operacion](numero1, numero2)
        resultado = str(resultado)
        resultado = bytes(resultado, 'utf-8')
        #respondo en consecuencia
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body>El resultado es: " + resultado + b"</body></html>" +
                        b"\r\n")
        recvSocket.close()        
        
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
    
    
    
    #http:localhost:1234/1/suma/3
