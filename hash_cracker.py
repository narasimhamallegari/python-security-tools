import hashlib

# ================================================
# Hash Cracker
# Author: Narasimha Mallegari
# Description: Dictionary attack on MD5, SHA1,
#              SHA256 password hashes.
# Usage: python3 hash_cracker.py
# Legal: Only use on hashes you own or have
#        written permission to test.
# ================================================

print("=" * 50)
print("  Hash Cracker")
print("  github.com/narasimhamallegari")
print("=" * 50)

target_hash = input("\nEnter hash to crack: ").strip().lower()
wordlist = input("Wordlist path: ").strip()

if len(target_hash) == 32:
    hash_type = "MD5"
elif len(target_hash) == 40:
    hash_type = "SHA1"
elif len(target_hash) == 64:
    hash_type = "SHA256"
else:
    hash_type = "Unknown"

print(f"\nDetected: {hash_type}")
print(f"Wordlist: {wordlist}")
print("-" * 50)

attempts = 0
found = False

try:
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            attempts += 1

            if (hashlib.md5(word.encode()).hexdigest() == target_hash or
                hashlib.sha1(word.encode()).hexdigest() == target_hash or
                hashlib.sha256(word.encode()).hexdigest() == target_hash):
                print(f"\n[CRACKED]  Password: {word}")
                print(f"Attempts:  {attempts:,}")
                found = True
                break

            if attempts % 500000 == 0:
                print(f"Checked {attempts:,}...")

    if not found:
        print(f"\n[NOT FOUND] Not in wordlist.")
        print(f"Total checked: {attempts:,}")

except FileNotFoundError:
    print(f"\nWordlist not found: {wordlist}")
    print("Extract rockyou: sudo gunzip /usr/share/wordlists/rockyou.txt.gz")
