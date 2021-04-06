import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$&[]_-" #add or take away symbols of choice

all = lower+upper+numbers+symbols

length = 8 #adjust to lenght of password wanted
password = "".join(random.sample(all,length))
print(password)


#should i make it as a loop ??
