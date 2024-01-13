import time

def typewriter(message, interval):
    char_list = list(message)
    for char in char_list:
        if char == "," or char == "." or char == "!":
            print(char, end = "", flush = True)
            time.sleep(1)
        else:
            print(char, end = "", flush = True)
            time.sleep(interval)
    print("\n")
# # makes a typewriting effect for printed statements

# prompt = "A. hi what's up:"
# time.sleep(5)
# typewriter("????: oh", .1)
# time.sleep(2)
# typewriter("????: hey",.1)

# time.sleep(1)
# while True:
#     print(prompt)
#     response = input()
#     if response.lower() == "a":
#         break
# # loop until input is correct

# time.sleep(0.05)
# typewriter("????: nothing much", .1)
# time.sleep(0.5)
# typewriter("????: u?", .1)

# time.sleep(0.05)
# prompt = "A. using this program:"
# while True:
#     print(prompt)
#     response = input()
#     if response.lower() == "a":
#         break

# time.sleep(1)
# typewriter("????: crazy", .1)
# time.sleep(2)
# typewriter("...", 3)

# typewriter("????: what do you want to talk about?", .1)

# prompt = "A. working out B. math C. family and friends D. [redacted]"

toy_shops = { 
    "working out" : "oh I love working out! It's honestly the best thing in the world",
    "toy kingdom" : "woohoo",
    "toytown" : "okeyyy",
}
typewriter(toy_shops["working out"], .1)