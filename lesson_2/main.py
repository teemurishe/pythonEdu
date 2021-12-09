bit = 0b111
mask = 0b0010

bit &= mask
print(bin(bit))

bit ^= mask
print(bin(bit))

bit ^= mask
print(bin(bit))

bit = 99
mask = 0b10000

bit &= mask
print(bin(bit))
bit ^= mask
print(bin(bit))
bit != mask
print(bin(bit))

def makeHappy():
    while True:
        print('Be happy and smile!')

makeHappy()