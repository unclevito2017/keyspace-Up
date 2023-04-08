# keyspace-Up
Program to increase the keyspace of a Bitcoin Public Key
Somewhat useless program that generates a public of increased keyspace. Example if the public key is in keyspace 10 and you input public key increase 22 keyspaces the new key generated will be found in Keyspace 32.
modules needed fastecdsa, binascii, Point
tested with python39
output to increased.txt
Example python39 keyspace_up.py
Enter the public key in hexadecimal format: 03a7a4c30291ac1db24b4ab00c442aa832f7794b5a0959bec6e8d7fee802289dcd   (keyspace 10)
Enter the reduction amount: 4
increased.txt 037dbbd8083d60c9349551a3f42ef560c3807fe2bf51d7fd69dfce62549a5f1277  (keyspace 14)
Mode xpoint
[+] Threads : 3
[+] Matrix screen
[+] Stats output every 30 seconds
[+] Opening file tests/test.txt
[+] N = 0x100000000
[+] Range
[+] -- from : 0x1
[+] -- to   : 0x1ffffffff
[+] Allocating memory for 1 elements: 0.00 MB
[+] Bloom filter for 1 elements.
[+] Loading data to the bloomfilter total: 0.00 MB
[+] Bloomfilter completed
[+] Sorting data ... done! 1 values were loaded and sorted
Base key: 1 thread 0
Base key: 100000001 thread 1

HIT!! Private Key: 2020
pubkey: 037dbbd8083d60c9349551a3f42ef560c3807fe2bf51d7fd69dfce62549a5f1277
to get back to the original private key you divide 2020 Hex by 4 power of 2 
2020 hex = 8224 decimal and 4 power 2 = 16  8224/16= 514 or 202 hex
