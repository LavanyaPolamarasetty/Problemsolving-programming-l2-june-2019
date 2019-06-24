import re
def phnovalidate(n):
    pattern='^[6-9]{1}[0-9]{9}$|^[0][6-9][0-9]$'
    if re.match(pattern,str(n)):
        print("valid number")
    else:
        print("invalid number")
phnovalidate(67899064899)
def emailvalidate(email):
    patt='^[0-9a-z][0-9a-z_.]{1,19}[@][0-9a-z]{3,18}[.][a-z]{1,4}$'
    if re.match(patt,str(email)):
        print("valid mail")
        
    else:
        print("invalid mail")
emailvalidate("abc@gmail.com")
