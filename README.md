# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Lab Question Answers

Answer for Question 1: 
Adding loss to my UDP client caused a lot of packets to be lost. When I typed a sequence of numbers quickly, a lot of the numbers wouldn't show up on my UDP server terminal.

"sudo tc qdisc add dev lo parent root netem loss 50%" is emulating a large queue of packets where most of these packets are being lost. This is why I'm losing numbers when I type a sequence quickly in my UDP client.

Answer for Question 2:
For the TCP test, I wasn't losing packets in the same manner as my UDP test. Instead of losing the sequence, all the numbers would appear on my TCP server but it would take longer.

Although the time it took for a number to show up on my TCP server was longer, I didn't lose packets like I did with UDP.

Answer for Question 3:
The speed of the sequence appearing on my server was definitely slower, but I didn't lose any numbers. I was also able to type on the TCP server and see the numbers on my client.

The speed of the sequence is slower because of the same command I used for the UDP server. I'm creating a large queue of packets for the server and it's taking the server longer to proccess them.

Answers to tcp_server questions.

1:
argc stands for arguement count and argv stands for arguement vector. argc is the number of arguements being passed into the program and argv is the array of arguements.

2:
A UNIX file descriptor is the number associated with a file opened on the operating system. For example, 10 files are opened on the system and Visual Studio Code is assigned the umber 102. 102 is the file descriptor for Visual Studio Code. The file descriptor table is a table where a file descriptor value, such as 102, will point to referrence the file associated with that number.

3:
"struct" is a data type that defines a physically grouped list of variables under one name. In the case of sockaddr_in, this is creating a list of variables serv_addr and cli_addr.

4:
The parameters of socket() are: AF_INET, SOCK_STREAM, 0. The return value is the function "error". This returns a message based on the input of "sockfd".

5:
The input parameters for bind() are sockfd, sockaddr, serv_adddr. For listen(), the input parameters are sockfd and 5.

6:
The infinite while loop is needed so the server can constantly take input from the client and display or return a message. If multiple connections are happening to the server we could potentially lose some data if they are sent at the same time.

7:
The fork() function creates a child process that runs concurrently with the parent process that made the fork system call. This would also multiple clients to connect to the server and handle their input concurrently without losing data.
...
v