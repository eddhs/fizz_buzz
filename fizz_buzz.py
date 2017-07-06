playing = True
while playing:
    try:
        numbercap=int(input('fizz buzz counting up to: '))
    except ValueError:
        print('please insert a number integer')
    else: 
        playing=False
    
list=range(1,(numbercap)+1)
for x in list:
    if x % 15 == 0:
        print('fizz buzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 ==0:
        print('buzz')
    else:
        print(x)

    