import random
import string
def generatepassword(passwordlength):
    if passwordlength<8:
        print("password length should be atleast 8 characters for security")
        return
    chars=string.ascii_letters+string.digits+string.punctuation
    password1=(
        random.choice(string.ascii_uppercase)+
        random.choice(string.ascii_lowercase)+
        random.choice(string.digits)+
        random.choice(string.punctuation)
        
    )
    password1 +=''.join(random.choice(chars) for _ in range(passwordlength - 4))
    passwordlist=list(password1)
    random.shuffle(passwordlist)
    password=''.join(passwordlist)
    return password1
passwordlength = int(input("Enter the length of Password "))
generatepassword(passwordlength)