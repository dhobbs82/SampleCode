"""
Derrick Hobbs
4/11/2023
SDEV300
This is a password creation program
"""

import hashlib

message = input("Enter a message to encode: ")

hash_algorithms = [
    hashlib.md5(),
    hashlib.sha1(),
    hashlib.sha224(),
    hashlib.sha256(),
    hashlib.sha384(),
    hashlib.sha512(),
    hashlib.blake2b(),
    hashlib.blake2s(),
    hashlib.shake_128(),
    hashlib.shake_256()
]

for algorithm in hash_algorithms:
    algorithm.update(message.encode())
    if algorithm.name in ['shake_128', 'shake_256']:
        print(f"{algorithm.name}: {algorithm.hexdigest(16)}")
    else:
        print(f"{algorithm.name}: {algorithm.hexdigest()}")
