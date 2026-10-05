# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    # Implement your solution here
    counts = Counter(A)
    for item, frequency in counts.items():
        if frequency == 1 and item is not None:
         return item
