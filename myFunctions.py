def isprime(number):
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count = count + 1
    if count>2:
        print("Not Prime")
        # return False
    else:
        print("Prime")
        # return True

def Greetings(name):
    return "Good morning,"+name