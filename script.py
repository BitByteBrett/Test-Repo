import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    gretting = "Hello, {}".format(who_to_greet)
    return gretting


r = requests.get("https://coreyms.com")
print(r.status_code)
