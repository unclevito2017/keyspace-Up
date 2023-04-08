# keyspace-Up
Program to increase the keyspace of a Bitcoin Public Key<p>
Somewhat useless program that generates a public key of increased keyspace. Example if the public key is in keyspace 10 and you input public key increase 4 <p>keyspace the new public key generated will be found in Keyspace 14.<p>
modules needed fastecdsa, binascii, Point<p>
tested with python39<p>
output to increased.txt<p>
Example python39 keyspace_up.py<p>
Enter the public key in hexadecimal format: 03a7a4c30291ac1db24b4ab00c442aa832f7794b5a0959bec6e8d7fee802289dcd   (keyspace 10)<p>
Enter the reduction amount: 4<p>
increased.txt output 037dbbd8083d60c9349551a3f42ef560c3807fe2bf51d7fd69dfce62549a5f1277  (keyspace 14)<p>

  Mode xpoint<p>
[+] Threads : 3<p>
[+] Matrix screen<p>
[+] Stats output every 30 seconds<p>
[+] Opening file tests/test.txt<p>
[+] N = 0x100000000<p>
[+] Range<p>
[+] -- from : 0x1<p>
[+] -- to   : 0x1ffffffff<p>
[+] Allocating memory for 1 elements: 0.00 MB<p>
[+] Bloom filter for 1 elements.
[+] Loading data to the bloomfilter total: 0.00 MB<p>
[+] Bloomfilter completed<p>
[+] Sorting data ... done! 1 values were loaded and sorted<p>
Base key: 1 thread 0<p>
Base key: 100000001 thread 1<p>

HIT!! Private Key: 2020<p>  
pubkey: 037dbbd8083d60c9349551a3f42ef560c3807fe2bf51d7fd69dfce62549a5f1277<p>
to get back to the original private key you divide 2020 Hex by 4 power of 2 <p>
2020 hex = 8224 decimal and 4 power 2 = 16<p>  8224/16= 514 or 202 hex <p>
