import time
prompt = "A. hi what's up \n"
time.sleep(5)
print("Person: oh")
time.sleep(2)
print("Person: hey")

time.sleep(1)
response = input(prompt)
while response.lower() != "a":
    response = input(prompt)

time.sleep(1)
print("Person: nothing much")
time.sleep(0.5)
print("Person: u?")

time.sleep(1)
prompt = "A. using this program \n"
response = input(prompt)
while response.lower() != "a":
    response = input(prompt)

time.sleep(1)
print("Person: crazy")
