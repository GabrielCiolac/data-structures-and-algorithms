#!/usr/bin/env python3


def merge_sorted(arr1: list, arr2: list) -> list:
    response = []
    while len(arr1) > 0 or len(arr2) > 0:
        if len(arr1) == 0:
            response += arr2
            break
        elif len(arr2) == 0:
            response += arr1
            break
        elif arr1[0] < arr2[0]:
            response.append(arr1.pop(0))
        else:
            response.append(arr2.pop(0))

    return response



if __name__ == "__main__":
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36, 37]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36, 37, 38]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36, 37, 38, 39]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
    print(merge_sorted([0, 3, 4, 31], [4, 6, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]))
