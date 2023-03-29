rooms_number = int(input())
room_inx = 0
total_free_chairs = 0
enough = True
for r in range(1, rooms_number+1):
    room_inx += 1
    chairs, visitors = input().split()
    if int(visitors) > len(chairs):
        diff = abs(len(chairs) - int(visitors))
        print(f"{diff} more chairs needed in room {room_inx}")
        enough = False
    if len(chairs) > int(visitors):
        total_free_chairs += len(chairs) - int(visitors)
if enough:
    print(f"Game On, {total_free_chairs} free chairs left")

