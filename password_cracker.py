import hashlib
import itertools
import time

# Setting desired password length
password_length = 5

def hashing_password_method(password):
    # Function to hash a password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

# List of Passwords to crack
hashed_passwords_to_crack = [
    hashing_password_method("pass1"),
    hashing_password_method("hello"),
    hashing_password_method("abc_1"),
]

def generating_all_password_possibility_method(length):
    # Function to generate all possible passwords of a given length
    print("Generating Cartesian products of characters in the char variable")
    
    # I am aware that actual possible char is longer and more diverse but this 
    # is just to showcase and hasten the process
    chars = "abcdefghijklmnopqrstuvwxyz_0123456789" 
    
    # Generate Cartesian products of characters to form passwords
    passwords = [''.join(p) for p in itertools.product(chars, repeat=length)]
    
    print(f"Successfully generated {len(passwords)}x passwords")
    return passwords

# Cracking of passwords
def crack_passwords():
    # Generating the password bank
    passwords_to_check = generating_all_password_possibility_method(password_length)
    
    start_time = time.time()  # Start the timer
    
    # Iterating through generated password bank
    for password in passwords_to_check:
        # Hashing password in password bank to prepared to be hashed.
        hashed_password = hashing_password_method(password)
        
        # Checking if generated hashed password is found in hashed_passwords_to_crack.
        if (hashed_password in hashed_passwords_to_crack):
            end_time = time.time()  # End the timer
            elapsed_time = end_time - start_time
            print(f"Password cracked: {password} (Hash: {hashed_password})")
            print(f"Time taken: {elapsed_time:.2f} seconds")

            # Removing hashed password from list
            hashed_passwords_to_crack.remove(hashed_password)
            if (len(hashed_passwords_to_crack) == 0):
                print("All passwords cracked.")
                end_time = time.time()  # End the timer
                elapsed_time = end_time - start_time
                print(f"Time taken to guess all passwords: {elapsed_time:.2f} seconds")
                break

crack_passwords()
