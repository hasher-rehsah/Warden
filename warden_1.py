password = '2341'
print('welcome warden. Enter your 4 digit password')
guess = input('Password:')
count = 0

if len(guess) > 4 or len(guess) < 4:
    print('Password must be 4 characters long')
    guess = input('Password')



while guess != password:
    if len(guess) > 4 or len(guess) < 4:
        print('Password must be 4 characters long')
        guess = input('Password')
    elif len(guess) == 4:
        for i in range(len(password)):
            if guess[i] == password[i]:
                count = count + 1
        print('you have', count, 'right')
        guess = input('Password:')
        count = 0
print = input('Welcome warden. Press enter to exit')        
