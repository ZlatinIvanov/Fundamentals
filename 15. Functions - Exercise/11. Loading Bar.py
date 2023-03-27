def loading_bar(percentage):
    bar = "[" + "".join("%" for i in range(int(percentage / 10)))
    bar += "".join("." for i in range(10 - int(percentage / 10))) + "]"
    if percentage < 100:
        message = f"{percentage}% {bar}"
    if percentage == 100:
        message = "100% Complete!"
    if percentage == 100:
        message += f"\n{bar}"
    else:
        message += "\nStill loading..."
    print(message)


percentage = int(input())
loading_bar(percentage)


