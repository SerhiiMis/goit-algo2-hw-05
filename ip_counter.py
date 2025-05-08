import re
import time
from datasketch import HyperLogLog

def extract_ips(file_path: str) -> list:
    ip_pattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    ips = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = ip_pattern.search(line)
            if match:
                ips.append(match.group(0))

    return ips

def count_unique_exact(ips: list) -> int:
    return len(set(ips))

def count_unique_hll(ips: list) -> float:
    hll = HyperLogLog()
    for ip in ips:
        hll.update(ip.encode("utf-8"))
    return hll.count()

def measure_time(func, *args) -> tuple:
    start = time.time()
    result = func(*args)
    duration = time.time() - start
    return result, duration

if __name__ == "__main__":
    file_path = "lms-stage-access.log"  
    ips = extract_ips(file_path)

    exact_count, exact_time = measure_time(count_unique_exact, ips)
    hll_count, hll_time = measure_time(count_unique_hll, ips)

    print("Результати порівняння:")
    print(f"{'Метод':<25} {'Унікальні IP':<20} {'Час (сек.)':<15}")
    print(f"{'Точний підрахунок':<25} {exact_count:<20} {exact_time:.5f}")
    print(f"{'HyperLogLog':<25} {int(hll_count):<20} {hll_time:.5f}")
