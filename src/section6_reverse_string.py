#!/usr/bin/env python3


def reverse_string(input: str) -> str:
    response = ""
    for char in input:
        response = char + response

    return response


if __name__ == "__main__":
    print(reverse_string("hello"))