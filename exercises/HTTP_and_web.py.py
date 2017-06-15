from socket import *
serverName=gethostname()
serverPort = 12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input('Input lowercase sentence:')
clientSocket.send(sentence.encode('ascii'))
modifiedSentence=clientSocket.recv(1024).decode('ascii')
print('From Server: ',modifiedSentence)
clientSocket.close()