import sys 
import hashlib 
  
if sys.version_info < (3, 6): 
    import sha3 
  
# initiating the "s" object to use the 
# s = hashlib.<secure name>()
method= input()
s = hashlib.md5() 
  
# will output the name of the hashing algorithm currently in use. 
print(s.name) 
  
# will output the Digest-Size of the hashing algorithm being used. 
print(s.digest_size) 
  
# providing the input to the hashing algorithm. 
s.update(method) 
  
print(s.hexdigest()) 
