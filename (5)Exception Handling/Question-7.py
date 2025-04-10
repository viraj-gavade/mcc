class OwnException(Exception):
    pass

class EarlyLetter(OwnException):
    pass

class LaterLetter(OwnException):
    pass

#character to be guessed
character = 's'
while True:
    try:
        demo=input("Please enter a character:")
        if demo<character:
            raise EarlyLetter
        elif demo>character:
            raise LaterLetter
    except EarlyLetter:
        print("OOps !! The entered alphabet is preceding one,try again!")
        print(' ')

    except LaterLetter:
        print("OOps !! The entered alphabet is succeding one,try again!")
        print(' ')

    else:f
        print('Hurray!! You guessed Correctly!')
        break
    
