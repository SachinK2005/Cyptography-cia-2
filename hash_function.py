# hash_function.py
# FNV-1a Hash (Fowler-Noll-Vo) - written from scratch
#
# Why FNV-1a?
# I looked up different non-cryptographic hash functions and found FNV-1a.
# It works by XORing each byte with the hash value first, then multiplying
# by a prime. This "XOR first" order (1a variant) gives better avalanche
# effect compared to the original FNV-1 which multiplies first.
#
# FNV-1a formula for each byte:
#   hash = (hash XOR byte) * FNV_prime
#
# Constants used (32-bit version):
#   offset_basis = 2166136261
#   FNV_prime    = 16777619
#
# These specific constants were mathematically chosen to minimize
# collisions across typical string inputs. Output is 8 hex characters.

FNV_PRIME        = 16777619
FNV_OFFSET_BASIS = 2166136261

def fnv1a_hash(text):
    if type(text) != str:
        text = str(text)

    hash_val = FNV_OFFSET_BASIS

    for ch in text:
        byte = ord(ch)
        hash_val = hash_val ^ byte           # XOR with the byte first
        hash_val = hash_val * FNV_PRIME      # then multiply by prime
        hash_val = hash_val & 0xFFFFFFFF     # keep it 32 bit

    return format(hash_val, '08x')


if __name__ == "__main__":
    # quick tests
    print(fnv1a_hash("hello"))
    print(fnv1a_hash("HELLO"))
    print(fnv1a_hash("NETWORKSECURITY"))
    print(fnv1a_hash(""))

    # avalanche check - one character difference should change hash a lot
    print(fnv1a_hash("abc"))
    print(fnv1a_hash("abd"))
