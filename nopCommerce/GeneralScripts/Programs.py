# Reverse string
import random
import string
import logging

import pytest

Str = "Suresh"
print(Str[::-1])

# Swapping strings
Str1 = "Ramesh"
dummyStr = Str
Str = Str1
Str1 = dummyStr

print(f"Str:{Str}", f"Str1:{Str1}")
print("Str:%s" % Str, "Str1:%s" % Str1)

print(12, 45, sep="_")

a = 2000898
b = 2000898
print(id(a), id(b))


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


print(random_generator())


def ran_gen():
    p = ''
    for x in range(0, 4):
        s = random.choice(string.ascii_lowercase + string.digits)
        p = p + s
        # print(p)
    return "Test_" + p


print(ran_gen())

log = logging.getLogger()


@pytest.mark.parametrize("x", [2, 4])
@pytest.mark.parametrize("y", [3, 9, 7])
def test_param(x,y):
    print("x:", x)
    print("y:", y)
    log.info("Value is:", x)
    log.info("Value is:", y)
