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
makes a typewriting effect for printed statements

prompt = "A. hi what's up"
time.sleep(5)
typewriter("????: oh", .1)
time.sleep(2)
typewriter("????: hey",.1)

time.sleep(1)
while True:
    response = input(f"{prompt} : ")
    if response.lower() == "hi what's up":
        break
# loop until input is correct

time.sleep(0.05)
typewriter("????: nothing much", .1)
time.sleep(0.5)
typewriter("????: u?", .1)

time.sleep(0.05)
prompt = "A. using this program:"
while True:
    print(prompt)
    response = input()
    if response.lower() == "a":
        break

time.sleep(1)
typewriter("????: crazy", .1)
time.sleep(2)
typewriter("...", 3)

typewriter("????: what do you want to talk about?", .1)

prompt = "A. programming B. math C. family and friends D. [redacted]"

redacted = {

}

topics = { 
    "programming" : "oh I love programming! There's just something so fun about creating something with pure logic :>",
    "math" : "best subject fr. I love working with numbers!" 
    " There's just something beautiful with how all of the universe can be represented through mathematics," 
    " corny as it sounds.",
    "family and friends" : "my family and friends mean so much to me, they're the ones who build my character,"
    " I would give them the universe.",
    "redacted" : redacted
    
}
while True:
    response = input(f"{prompt} : ")
    response = response.lower()
    if response in topics.keys():
        break
typewriter(topics[response], 0.05)
