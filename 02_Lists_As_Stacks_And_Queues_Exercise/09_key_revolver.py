from collections import deque

price_per_bullet = int(input())
size_of_barrel = int(input())
bullets = deque(int(bullet) for bullet in input().split())
locks = deque(int(lock) for lock in input().split())
value_of_intelligence = int(input())
used_bullets = 0
counter = 0
is_safe_opened = False

while bullets:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    used_bullets += 1
    counter += 1
    if counter == size_of_barrel and bullets:
        print("Reloading!")
        counter = 0

    if not locks:
        is_safe_opened = True
        break


if is_safe_opened:
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - price_per_bullet * used_bullets}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")