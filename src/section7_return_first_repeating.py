#!/usr/bin/env python3


from typing import Any, List, Optional


def first_repeating(input : List[Any]) -> Optional[Any]:
    seen = set()
    for item in input:
        if item in seen:
            return item
        else:
            seen.add(item)

    return None

if __name__ == "__main__":
    print(first_repeating([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
    print(first_repeating([1, 2, 3, 4, 5, 6, 7, 8, 9]))