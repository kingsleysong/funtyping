
import random,hashlib
password = '1123'
#salt = ''.join(random.sample("jfkdlsajfoieujfkdsjfkdlfjds",20))
salt='fdksfjdsfjdskfdslf'
md5_result = hashlib.md5(salt+password).hexdigest()
print md5_result
