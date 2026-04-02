# Running Key Cipher + FNV-1a Hash

**Cipher assigned:** Running Key Cipher (Roll no. mod 10 = 5)  
**Language:** Python 3  
**Hash chosen:** FNV-1a (Fowler-Noll-Vo) — implemented from scratch

---

## Files

| File | Description |
|------|-------------|
| `main.py` | Running Key Cipher (encrypt + decrypt) with user input, imports hash |
| `hash_function.py` | FNV-1a 32-bit hash implemented from scratch |
| `test_roundtrip.py` | Full encrypt → hash → decrypt test script |

---

## Running Key Cipher - Theory

The running key cipher is a polyalphabetic substitution cipher. Unlike Vigenere which uses a short repeating key, this cipher uses a long passage of text as the key (one key letter per plaintext letter). The key must be at least as long as the message.

**Encryption:**
```
C = (P + K) mod 26
```

**Decryption:**
```
P = (C - K + 26) mod 26
```

Where P, C, K are alphabet positions of plaintext, ciphertext, and key letters (A=0 ... Z=25).

Because the key never repeats, the Kasiski test cannot determine key length, making this harder to break than standard Vigenere.

---

## Hash Function - FNV-1a Theory

FNV-1a (Fowler-Noll-Vo variant 1a) is a well known non-cryptographic hash. The "1a" variant XORs before multiplying, which gives better bit diffusion than the original FNV-1.

**Formula (for each character):**
```
hash = (hash XOR byte) * FNV_prime
```

**Constants (32-bit):**
```
offset_basis = 2166136261
FNV_prime    = 16777619
```

These constants were mathematically derived to minimize collisions. Output is kept within 32 bits after each step using a bitmask. Final result is an 8-character hex string.

I chose FNV-1a because the algorithm is transparent and simple enough to implement line by line without any library help, and it has noticeably better avalanche properties than simpler hashes like djb2.

---

## How to Run

Python 3, no extra libraries needed.

```bash
python main.py           # interactive encrypt/decrypt + worked examples
python hash_function.py  # test the hash function standalone
python test_roundtrip.py # run all round-trip tests
```

---

## Worked Examples

Running key: *"It is a truth universally acknowledged that a single man in possession of a good fortune..."* (Pride and Prejudice)

### Example 1

| Field | Value |
|-------|-------|
| Plaintext | `HELLOWORLD` |
| Key letters used | `ITISATRUTH` |
| Ciphertext | `PXTDOPFLEK` |
| FNV-1a Hash | `01073534` |
| Decrypted | `HELLOWORLD` ✓ |

Manual check (first letter):
- H=7, I=8 → (7+8) mod 26 = 15 → **P** ✓

### Example 2

| Field | Value |
|-------|-------|
| Plaintext | `DATASECURITY` |
| Key letters used | `ITISATRUTHUN` |
| Ciphertext | `LTBSSXTOKPNL` |
| FNV-1a Hash | `6cba83c9` |
| Decrypted | `DATASECURITY` ✓ |

---

## References

- Stinson, D.R. - Cryptography: Theory and Practice
- https://en.wikipedia.org/wiki/Running_key_cipher
- FNV hash: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
