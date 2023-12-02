#!/usr/bin/env python3


from typing import Any


class ArrayCustom:
    def __init__(self):
        self.length = 0
        self.backing_array = []

    def get(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            return None
        return self.backing_array[index]
    
    def push(self, item: Any) -> int:
        self.backing_array.append(item)
        self.length += 1
        return self.length
    
    def pop(self) -> Any:
        if self.length == 0:
            return None
        self.length -= 1
        return self.backing_array.pop()
    
    def shift_items(self, index: int) -> None:
        for i in range(index, self.length - 1):
            self.backing_array[i] = self.backing_array[i + 1]

    def delete(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            return None
        item = self.backing_array[index]
        self.shift_items(index)
        self.backing_array.pop()
        self.length -= 1
        return item

    


if __name__ == "__main__":
    my_array = ArrayCustom()
    my_array.push("hi")
    my_array.push("you")
    my_array.push("!")
    my_array.delete(1)
    print(my_array.backing_array)