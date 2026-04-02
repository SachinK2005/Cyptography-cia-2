# test_roundtrip.py
# verifies the full cycle: encrypt -> hash -> decrypt

from main import running_key_encrypt, running_key_decrypt, remove_non_alpha, KEY
from hash_function import fnv1a_hash

tests = [
    "HELLO WORLD",
    "DATA SECURITY",
    "RUNNING KEY CIPHER",
    "PYTHON",
    "ZZZZ",
]

print("=========================================")
print("   Encrypt -> Hash -> Decrypt Tests")
print("=========================================")

passed = 0
for t in tests:
    plain = remove_non_alpha(t)
    enc   = running_key_encrypt(plain, KEY)
    h     = fnv1a_hash(enc)
    dec   = running_key_decrypt(enc, KEY)
    ok    = dec == plain

    print(f"\nInput      : {plain}")
    print(f"Encrypted  : {enc}")
    print(f"FNV1a Hash : {h}")
    print(f"Decrypted  : {dec}")
    print(f"Status     : {'PASS' if ok else 'FAIL'}")

    if ok:
        passed += 1

# tamper test
print("\n--- Tamper Detection ---")
sample     = running_key_encrypt("HELLO WORLD", KEY)
h_original = fnv1a_hash(sample)
tampered   = sample[:-1] + ('X' if sample[-1] != 'X' else 'Y')
h_tampered = fnv1a_hash(tampered)
print(f"Original  : {sample} -> {h_original}")
print(f"Tampered  : {tampered} -> {h_tampered}")
print(f"Detected  : {h_original != h_tampered}")

print(f"\n=========================================")
print(f"  {passed}/{len(tests)} tests passed")
print(f"=========================================")
