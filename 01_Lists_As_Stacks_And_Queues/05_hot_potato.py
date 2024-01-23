from collections import deque

kids = deque(input().split())
n_toss = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-n_toss)
    removed_kid = kids.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids.popleft()}")
