# import gzip and decompress
import gzip
import zlib

#Whats known
#0241410002206a4869aadddfd6cf956eefeb0ea0000000040380
#02: ???
#4141: Protocol Version: AA
#00: Major Version: 0
#02: Minor Version: 2

#The rest:
#206a4869aadddfd6cf956eefeb0ea0000000040380


#0241410002
# 204aca6adf40c016c56fa06000000000000494c77b065d1806822a8109680001200820d041a083410682080001e004f58800025195be5da380055be8180000158f00c8481c53d105940f3a93622b7d0301003c4654f7fe0000e4600188

print("example zlib")
s = b'his is GFG author, and final year student.'

# using zlib.compress(s) method
t = zlib.compress(s)
print("Compressed String")
print(t)

print("\nDecompressed String")
print(zlib.decompress(t))


print ("-----------------------------------------------------------")
#0241410002206a4869aadddfd6cf956eefeb0ea0000000040380
t = bytes.fromhex("6a4869aadddfd6cf956eefeb0ea0000000040380")
#print(zlib.decompress(t))



s = b'f This is GFG author, and final year student.'
s = gzip.compress(s)
print((s))

s = bytes.fromhex("dfd6cf956eefeb0ea0000000040380")
#0241410002206a4869aadddfd6cf956eefeb0ea0000000040380
# using gzip.decompress(s) method
t = gzip.decompress(s)
print(t)

s = b'This is GFG author, and final year student.'
s = gzip.compress(s)
print(s)




