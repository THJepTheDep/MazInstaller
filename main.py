import time
import requests as req

NAME = input("PROJECT_NAME: ")
URL = input("GITHUB URL: ")
FILE_NAME = input("FILE_NAME: ")

#print(NAME.upper(),"|", GITHUB.upper())

print("Processing data...")
time.sleep(2)
print("Getting URL...")
time.sleep(2)

with req.get(URL) as rq:
    with open(FILE_NAME, 'wb') as file:
        file.write(rq.content)

print("Compiling...")
time.sleep(2)
print("Reading...")
time.sleep(2)
print("Writing...")
time.sleep(2)
print("Done!")
