import re

n = int(input())
pattern = r"[sStTaArR]"
decrypt_reg = r"@([a-zA-Z]+)[^@:!>-]*\:([0-9]+)!([AD])!->(\d+)"
planet_list = []
population_list = []
attack_list = []
destroy_list = []
for _ in range(n):
    messages = input()
    matches = re.findall(pattern, messages)
    counter = len(matches)
    decrypted_message = ''.join(chr(ord(c) - counter) for c in messages)
    decryption = re.findall(decrypt_reg, decrypted_message)
    for match in decryption:
        name = match[0]
        population = int(match[1])
        attack_type = match[2]
        soldier_count = int(match[3])
        if attack_type == "A":
            attack_list.append(name)
        elif attack_type == "D":
            destroy_list.append(name)
attack_list = sorted(attack_list)
destroy_list = sorted(destroy_list)
print(f"Attacked planets: {len(attack_list)}")
for x in attack_list:
    print(f"-> {x}")
print(f"Destroyed planets: {len(destroy_list)}")
for x in destroy_list:
    print(f"-> {x}")
# 2
# STCDoghudd4=63333$D$0A53333
# EHfsytsnhf?8555&I&2C9555SR
