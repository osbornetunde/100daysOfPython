#Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import zlib


s="hello world!hello world!hello world!hello world!"
c_data = zlib.compress(s.encode())

print(len(c_data))

print(zlib.decompress(c_data))