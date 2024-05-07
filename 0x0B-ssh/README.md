# 0x0B-SSH

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely. It provides a text-based interface by spawning a remote shell. After connecting, all commands you type in your local terminal are sent to the remote server and executed there.

## Learning Objectives

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash

login senquence 

ssh ubuntu@3.85.136.169 -i ~/.ssh/school
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1021-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Jan 24 06:25:47 UTC 2024

  System load:  0.0               Processes:             98
  Usage of /:   7.9% of 19.20GB   Users logged in:       0
  Memory usage: 21%               IPv4 address for eth0: 10.247.111.45
  Swap usage:   0%

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

0 updates can be applied immediately.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
New release '22.04.3 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Wed Jan 24 06:20:18 2024 from 196.191.61.203
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

