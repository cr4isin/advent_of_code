
import hashlib
from itertools import count

for index in count():
    if hashlib.md5(str.encode(f'ckczppom{index}')).hexdigest().startswith('00000'):
        print(index)
        break