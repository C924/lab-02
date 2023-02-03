# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Lab Question Answers

Answer for Question 1: 
Adding loss to my UDP client caused a lot of packets to be lost. When I typed a sequence of numbers quickly, a lot of the numbers wouldn't show up on my UDP server terminal.

sudo tc qdisc add dev lo parent root netem loss 50% is emulating a large queue of packets where most of these packets are being lost. This is why I'm losing numbers when I type a sequence quickly in my UDP client.

Answer for Question 2:
For the TCP test, I wasn't losing packets in the same manner as my UDP test. Instead of losing the sequence, all the numbers would appear on my TCP server but it would take longer.

Although the time it took for a number to show up on my TCP server was longer, I didn't lose packets like I did with UDP.

Answer for Question 3:
The speed of the sequence appearing on my server was definitely slower, but I didn't lose any numbers. I was also able to type on the TCP server and see the numbers on my client.

The speed of the sequence is slower because of the same command I used for the UDP server. I'm creating a large queue of packets for the server and it's taking the server longer to proccess them.

...
