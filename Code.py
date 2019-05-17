ask1=input('Enter your name')
print('Hello')
ask2=int(input('Enter you age'))
if(ask2<18):
    print('I am not allowed to talk to you.')
    print('You need to leave. NOW.')
else:
    ask3=input('Who is your mother\'s favorite child?')
    if(ask3==ask1):
        print('I doubt that')
    else:
        ask4=int(input('If the robots take over the earth, would you 1. Accept 2. Accept 3. Accept 4. Rebel?'))
        if(ask4!=4):
            print('Exallent')
        else:
            print('Oh')