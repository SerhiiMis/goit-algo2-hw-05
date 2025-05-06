# 📘 Big Data Tasks: Bloom Filter & HyperLogLog

## 🧪 Task 1: Password Uniqueness Check Using Bloom Filter

### 🎯 Goal

Efficiently check whether passwords have been used before using a Bloom Filter without storing them directly.

### ✅ Functional Requirements

- Implement `BloomFilter` class with:
  - `.add(item: str)`
  - `.check(item: str) -> bool`
- Implement `check_password_uniqueness(bloom, password_list)`
  - Returns a dictionary: `{password: "вже використаний" | "унікальний"}`
- Handle empty or invalid inputs
- Optimized for large datasets with minimal memory usage

### 🧪 Example Usage

```python
bloom = BloomFilter(size=1000, num_hashes=3)
bloom.add("password123")
bloom.add("admin123")
bloom.add("qwerty123")

to_check = ["password123", "newpassword", "admin123", "guest"]
results = check_password_uniqueness(bloom, to_check)
```

#### ✅ Expected Output

```
Пароль 'password123' — вже використаний.
Пароль 'newpassword' — унікальний.
Пароль 'admin123' — вже використаний.
Пароль 'guest' — унікальний.
```

---

## 📊 Task 2: Compare Unique Count — Set vs HyperLogLog

### 🎯 Goal

Compare exact unique element counting vs approximate counting using HyperLogLog.

### ✅ Functional Requirements

- Load real log file `lms-stage-access.log`
- Extract valid IP addresses
- Implement two functions:
  - `count_unique_exact(lines) -> int`
  - `count_unique_hll(lines) -> float`
- Measure and compare execution time of both methods
- Present results in table format

### 🧪 Example Output

```
Результати порівняння:
                       Точний підрахунок   HyperLogLog
Унікальні елементи              100000.0      99652.0
Час виконання (сек.)                0.45          0.10
```

---

### 📌 Notes

- HyperLogLog has ~1% relative error
- Must ignore malformed lines in logs
- Both implementations should scale well to large datasets
