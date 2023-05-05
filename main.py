import random
import string
password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10))
print(password)
