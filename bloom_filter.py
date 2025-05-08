import hashlib
from typing import List, Dict

class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _get_hashes(self, item: str) -> List[int]:
        hashes = []
        for i in range(self.num_hashes):
            hash_input = f"{item}_{i}".encode("utf-8")
            hash_digest = hashlib.md5(hash_input).hexdigest()
            hash_int = int(hash_digest, 16)
            hashes.append(hash_int % self.size)
        return hashes

    def add(self, item: str):
        if not isinstance(item, str) or not item.strip():
            return
        for index in self._get_hashes(item):
            self.bit_array[index] = 1

    def check(self, item: str) -> bool:
        if not isinstance(item, str) or not item.strip():
            return False
        return all(self.bit_array[i] for i in self._get_hashes(item))

def check_password_uniqueness(bloom: BloomFilter, passwords: List[str]) -> Dict[str, str]:
    result = {}
    for pw in passwords:
        if not isinstance(pw, str) or not pw.strip():
            result[pw] = "некоректний"
        elif bloom.check(pw):
            result[pw] = "вже використаний"
        else:
            result[pw] = "унікальний"
            bloom.add(pw)
    return result

# 🔎 Example usage
if __name__ == "__main__":
    bloom = BloomFilter(size=1000, num_hashes=3)
    existing = ["password123", "admin123", "qwerty123"]
    for p in existing:
        bloom.add(p)

    to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, to_check)

    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")
