from collections import deque

bullet_price = int(input())
mag_max = int(input())

bullets = deque([int(bullet) for bullet in input().split()])
locks = deque([int(lock) for lock in input().split()])

reward = int(input())

mag_bullets = mag_max
shot_bullets = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    mag_bullets -= 1
    shot_bullets += 1

    if mag_bullets == 0 and bullets:
        mag_bullets = mag_max if len(bullets) >= mag_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((bullet_price * shot_bullets) - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
