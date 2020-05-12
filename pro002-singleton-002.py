def log_message(msg):        
    with open("login.txt", "a") as log_file:
        log_file.write("this is a message.\n")


