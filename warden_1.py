password = '2341'



print('hello warden. Enter your 4 digit password')
guess = input('Password:')

if guess == password:
    print('welcome warden dont forget etc etc etc')
    exit = input('press enter to exit. warning this will exit the program')
    quit()
     
     
     
while guess != password:
    a=list(set(password)&set(guess))
    count = 0
    for x in a:
        count = count +1
    print('you have',count,'right')  
    guess = input('Password:')
    
    
print('welcome Warden etc etc etc')
exit = input('press enter to exit. warning this will exit the program')
