bit = 0b111
mask = 0b0010

bit &= mask
print(bin(bit))

bit ^= mask
print(bin(bit))

bit ^= mask
print(bin(bit))