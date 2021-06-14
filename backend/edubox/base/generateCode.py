import random
import string

def get_code():
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    return code