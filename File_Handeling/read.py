File = open("text.txt", "r")
data = File.read()
print(data)
data = data.lower()

if "open" in data:
    print("Word is present")

File.close()