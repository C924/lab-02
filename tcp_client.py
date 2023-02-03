"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "172.20.10.9"
PORT = 5050


def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    # TODO: Get user input and send it to the server using your TCP socket
    msg = input("Send a message to the server").encode(encoding='UTF-8',errors='strict')
    server.sendall(msg)
    # TODO: Receive a response from the server and close the TCP connection
    rsp = server.recv(256).decode(encoding='UTF-8',errors='strict')
    print(rsp)
    pass


if __name__ == '__main__':
    main()
