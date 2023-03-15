event = ""
counter = 0
while event != "END":
    event = input()
    if event == "cat" or event == "dog" or event == "coding" or event == "movie":
        counter += 1
    if event == "CAT" or event == "DOG" or event == "CODING" or event == "MOVIE":
        counter += 2
    if event == "END":
        break

if counter > 5:
    print(f"You need extra sleep")
else:
    print(f"{counter}")
