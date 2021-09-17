#TODO implementing HCF

def hcf(a, b):
    if(a ==0):
        return b

    return hcf(b%a, a)

print(hcf(3, 9))
print(hcf(2, 20))
print(hcf(45, 100))
