import hashlib

def askuserName(Prompt):
    return Prompt

def passWord(PPrompt):
    password = PPrompt
    hashed = hashlib.md5(password.encode()).hexdigit()
    