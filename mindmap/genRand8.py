import random
import string

def get():
	''.join(random.sample(string.ascii_letters + string.digits, 8))
