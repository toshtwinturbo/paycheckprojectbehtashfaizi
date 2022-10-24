import random

print('Generate a Strong Password')
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+."


string = lower + upper + numbers + symbols
length = int(input("How Many Characters Do You Want Your Password To Be: "))
password = "".join(random.sample(string, length))

print("Here Is Your Password:", password)