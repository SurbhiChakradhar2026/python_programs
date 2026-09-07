# Open the file in read mode
file = open("geeks.txt", "r")
line = file.read(2)
#print(line)
with open('geeks.txt','a') as f:
    f.write('This is a new line added to the file.')
with open("geeks.txt") as f:
  print(f.read())


f = open("myfile.txt", "x")
