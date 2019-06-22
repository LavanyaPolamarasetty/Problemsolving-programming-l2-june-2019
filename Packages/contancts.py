contacts ={}
def addcontact(name,phone):
    #verify that the contact doesnot already exist
    if name not in contacts:
        contacts[name]=phone
        print("Contact %s added" % name)
    else:
        print("contact %s already exists" % name)
    return


def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exist" % name)
    return

def listcontact():
    for k,v in contacts.items():
        print(k,':',v)
        
        
def modifycontacts(name,phone):
    contacts[name]=phone
    print(contacts)
    
    
def removecontact(name):
    contacts.pop(name)
    print(contacts)
    
def importcontacts(newcontact):
    contacts.update(newcontact)
    print(contacts)