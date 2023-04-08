from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
from binascii import unhexlify, hexlify

# Define the public key and get the reduction amount from user input
public_key_hex = input("Enter the public key in hexadecimal format: ")
reduction = int(input("Enter the reduction amount: "))
keyspace_increase = 2 ** reduction

# Convert the public key from hex to a point object
public_key_bytes = unhexlify(public_key_hex)
x_decimal = int.from_bytes(public_key_bytes[1:], 'big')
y_squared = (x_decimal ** 3 + secp256k1.a * x_decimal + secp256k1.b) % secp256k1.p
y_decimal = pow(y_squared, (secp256k1.p + 1) // 4, secp256k1.p)
if public_key_bytes[0] == 0x03:
    y_decimal = secp256k1.p - y_decimal
public_key = Point(x_decimal, y_decimal, curve=secp256k1)

# Multiply the public key by the reduction amount
reduced_public_key = keyspace_increase * public_key

# Convert the reduced public key back to hex
reduced_public_key_bytes = bytearray([0x02 + (reduced_public_key.y % 2)])
reduced_public_key_bytes += reduced_public_key.x.to_bytes(32, 'big')
reduced_public_key_hex = hexlify(reduced_public_key_bytes).decode()

# Write the reduced public key to a file
with open('increased.txt', 'w') as f:
    f.write(reduced_public_key_hex)
