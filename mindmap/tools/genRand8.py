import random
import string

def get():
	return ''.join(random.sample(string.ascii_letters + string.digits, 8))
