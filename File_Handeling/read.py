File = open("text.txt", "r")
data = File.readline().strip()
print(data)
data = File.readline().strip()
print(data)
data = File.readline().strip()
print(data)
data = data.lower()

if "open" in data:
    print("Word is present")

File.close()


#read line by line

with open("text.txt", "r") as f:            #you don't have to close the file
    for line in f:
        print(line.strip())

