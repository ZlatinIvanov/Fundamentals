number_of_words = int(input())

for n in range(0, number_of_words):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88 and number != 86:
        print("GREAT!")
    elif number > 88:
        print("Bye.")