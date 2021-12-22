import random
for n in range(1):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number="1234567890"
    symbol="!@#$%?&*"

    all=lower+upper+number+symbol
    password="".join(random.sample(all,8))
    print(f"The password generated :{password}")