# import gzip and decompress
import gzip

#s = b'This is GFG author, and final year student.'
#s = gzip.compress(s)
s = bytes.fromhex("0241410002206a4869aadddfd6cf956eefeb0ea0000000040380")
#0241410002206a4869aadddfd6cf956eefeb0ea0000000040380
# using gzip.decompress(s) method
#t = gzip.decompress(s)
#print(t)

s = b'This is GFG author, and final year student.'
s = gzip.compress(s)
print(s)


