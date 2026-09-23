#!/usr/bin/env python3
"""
Decimal ↔ pure alphanumeric sexagesimal converter
Digit set: 0-9a-zA-X  (exactly 60 symbols)
"""

import argparse


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
    if not s:
        raise ValueError("sexagesimal value cannot be empty")

    if s.startswith("-"):
        if len(s) == 1:
            raise ValueError("invalid negative value")
        return -from_sexagesimal(s[1:])

    value = 0
    for ch in s:
        try:
            digit = DIGITS.index(ch)
        except ValueError:
            raise ValueError(f"invalid sexagesimal digit: {ch!r}") from None

        value = value * 60 + digit

    return value


def print_conversion_table() -> None:
    examples = [0, 1, 9, 10, 35, 36, 59, 60, 61, 1729, 3600, 123456, 999999]

    print(f"{'Decimal':>10}  →  {'Sexagesimal':<12}  →  Back")
    print("-" * 42)

    for n in examples:
        s = to_sexagesimal(n)
        back = from_sexagesimal(s)
        print(f"{n:>10}  →  {s:<12}  →  {back}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert between decimal and pure alphanumeric sexagesimal."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Decimal → sexagesimal
    to_parser = subparsers.add_parser(
        "to",
        help="convert decimal to sexagesimal",
    )
    to_parser.add_argument(
        "number",
        type=int,
        help="non-negative or negative decimal integer",
    )

    # Sexagesimal → decimal
    from_parser = subparsers.add_parser(
        "from",
        help="convert sexagesimal to decimal",
    )
    from_parser.add_argument(
        "value",
        help="sexagesimal value using digits 0-9a-zA-X",
    )

    # Conversion table
    subparsers.add_parser(
        "table",
        help="print the conversion table",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "to":
            print(to_sexagesimal(args.number))

        elif args.command == "from":
            print(from_sexagesimal(args.value))

        elif args.command == "table":
            print_conversion_table()

    except ValueError as exc:
        parser.error(str(exc))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


