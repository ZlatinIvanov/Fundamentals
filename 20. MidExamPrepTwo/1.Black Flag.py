days = int(input())
plunder_for_day = int(input())
expected_plunder = float(input())

total_plunder = 0


for n in range(1, days+1):
    total_plunder += plunder_for_day
    if n % 3 == 0:
        total_plunder += plunder_for_day * 0.5
    if n % 5 == 0:
        total_plunder = total_plunder - (total_plunder * 0.3)
percentage = (total_plunder / expected_plunder) * 100
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")