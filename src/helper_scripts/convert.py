#!/usr/bin/env python3
"""
Decimal ↔ pure alphanumeric sexagesimal converter
Digit set: 0-9a-zA-X  (exactly 60 symbols)
"""

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX"
assert len(DIGITS) == 60

def to_sexagesimal(n: int) -> str:
    """Convert a non-negative integer to pure alphanumeric sexagesimal."""
    if n < 0:
        return "-" + to_sexagesimal(-n)
    if n == 0:
        return "0"
    result = []
    while n:
        result.append(DIGITS[n % 60])
        n //= 60
    return "".join(reversed(result))

def from_sexagesimal(s: str) -> int:
    """Convert a pure alphanumeric sexagesimal string back to decimal."""
    if s.startswith("-"):
        return -from_sexagesimal(s[1:])
    value = 0
    for ch in s:
        value = value * 60 + DIGITS.index(ch)
    return value

# ---------- quick demo ----------
if __name__ == "__main__":
    examples = [0, 1, 9, 10, 35, 36, 59, 60, 61, 1729, 3600, 123456, 999999]

    print(f"{'Decimal':>10}  →  Sexagesimal  →  Back")
    print("-" * 42)
    for n in examples:
        s = to_sexagesimal(n)
        back = from_sexagesimal(s)
        print(f"{n:>10}  →  {s:<12}  →  {back}")


