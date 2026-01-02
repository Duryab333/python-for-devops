#file = open("demo.txt") # OPEN
#print(file.read()) # OPERATION
#file.write("Hello Dosto, kya haal chaal")
#file.close() # CLOSE

def read_file(file_name):
    with open(file_name, "r") as f:
        print(f.read())

read_file("demo.txt")