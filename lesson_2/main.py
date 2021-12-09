bit = 99
mask = 0b10000

bit &= mask
print(bin(bit))
bit ^= mask
print(bin(bit))
bit != mask
print(bin(bit))