file_path = input().split("\\")

file = file_path[-1]
name, extension = file.split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
