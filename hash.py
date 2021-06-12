import hashlib

data = input("Enter text input ")
tobyte = bytes(data, 'UTF-8')
m = hashlib.md5(tobyte)
print(m.hexdigest())