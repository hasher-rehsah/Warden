import random  # for password generation // not using secrets because these are fake credentials.
import hashlib  # preventing keeping the password in source code.

MAXIMUM_GUESS_COUNT = 10  # change this number accordingly.

password = hashlib.sha256(f"{random.randint(1000, 10000)}".encode("utf-8")).hexdigest()
# above line hashes a random number from 1000-9999 using sha256 to prevent anyone from viewing the password through the source code.

guess_count = 0

while guess_count < MAXIMUM_GUESS_COUNT:
    user_guess = input('Welcome warden, enter your 4 digit password: ')
    if len(user_guess) != 4:
        print("Password must be 4 characters long.")
    guess_count += 1
    if hashlib.sha256(f"{user_guess}".encode("utf-8")).hexdigest() == password:
        input("Welcome warden, press enter to exit. ")
