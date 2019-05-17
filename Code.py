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