import bcrypt


password = b"SecretPasswordd5"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

if bcrypt.checkpw(password, hashed):
   print("It matches")
else:
    print("Does not match")