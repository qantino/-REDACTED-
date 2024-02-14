import time
import visuals
date = time.ctime()
greeting = None

if "Feb 14" in date:
    greeting = "Happy Valentines Day!"
else:
    greeting = "I love you :>"

def typewriter(message, interval):
    char_list = list(message)
    for char in char_list:
        if char == "," or char == "." or char == "!" or char == ">":
            print(char, end = "", flush = True)
            time.sleep(1)
        else:
            print(char, end = "", flush = True)
            time.sleep(interval)
    print("\n")
# makes a typewriting effect for printed statements

prompt = "A. hi what's up"
time.sleep(5)
typewriter("????: oh", .1)
time.sleep(2)
typewriter("????: hey",.1)

time.sleep(1)
while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "hi what's up":
        break
# loop until input is valid

time.sleep(0.05)
typewriter("????: nothing much", .1)
time.sleep(0.5)
typewriter("????: u?", .1)

time.sleep(0.05)
prompt = "A. using this program"
while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "using this program":
        break

time.sleep(1)
typewriter("????: crazy", .1)
time.sleep(2)
typewriter("...", 3)

typewriter("????: what do you want to talk about?", .1)

prompt = "A. programming B. math C. family and friends D. redacted"


topics = { 
    "programming" : "oh I love programming! There's just something so fun about creating something with pure logic :>",
    "math" : "best subject fr. I love working with numbers!" 
    " There's just something beautiful with how all of the universe can be represented through mathematics, corny as it sounds.",
    "family and friends" : "my family and friends mean so much to me, they're the ones who build my character,"
    " I would give them the universe.",
    "redacted" : "redacted is my favorite out of all things ever. i love redacted more than anything",
}
while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "redacted":
        break
    elif response in topics.keys():
        typewriter(topics[response], 0.05)
        prompt = prompt.replace(response, "redacted")

typewriter("...", 3)
typewriter(topics[response], 0.025)

prompt = "A. what is redacted?"

while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "what is redacted" or response == "what is redacted?":
        break

typewriter("redacted is my world.", 0.025)

prompt = "A. elaborate?"

while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "elaborate" or response == "elaborate?":
        break

typewriter("never have I felt warmth, safety, and love, the way I do when I'm by her side.", 0.025)
typewriter("Her joy, brings me joy. Whenever she's sad, I am too. I want to give her everything I have and beyond.", 0.025)
typewriter("I can tell that at times, she gets jealous of the people I liked before.", 0.025)
typewriter("She doesn't realize that she's leagues above all of them, that she's what made me realize the difference between liking someone and loving someone. She completes me, and I want to face all the challenges of life with her. I am forever grateful for her.", 0.025)

prompt = "A. who is redacted?"

while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "who is redacted" or response == "who is redacted?":
        break

typewriter("Khloe, love of my life <3", 0.05)

prompt = "A. damn"

while True:
    response = input(f"{prompt}: ")
    response = response.lower().strip()
    if response == "damn":
        break

typewriter("Oh sorry! Said all that without you even knowing my name", 0.05)
typewriter("Hi, I'm Luis, and you are?", 0.05)

prompt = "Enter name: "
response = input(prompt)
response = response.lower().strip()

redacted = ["khloe", "cindehara", "haefiu", "charmaine", "charmainegames", "kazuhamain420", "maine", "khlo", "klo", "lunawcnders"]
other_people = {
    "christine": "hi favorite crocheter! tell Khloe I said hi!",
    "gwayne": "hi favorite spotify playlist provider! tell Khloe I said hi!",
    "shaz": "hi cap! tell Khloe I said hi!",
    "shaznae": "hi cap! tell Khloe I said hi!",
    "ash" : "hi pres! tell Khloe I said hi!",
    "ashley" : "hi pres! tell Khloe I said hi!",
    "cecil" : "hi vp! tell Khloe I said hi!",
    "cecilia" : "hi vp! tell Khloe I said hi!",
    "seb" : "hi treasurer! tell Khloe I said hi!",
    "sebastiana" : "hi treasurer! tell Khloe I said hi!",
    "marian" : "hi bookworm! tell Khloe I said hi!",
    "angel": "hi mary grace! tell Khloe I said hi!",
    "johan": "wow hi! tell Khloe I said hi!",
    "annika": "helloo rosarian! tell Khloe I said hi!",
    "luis" : "luis why are you using ur own program",

                }
# defines list of khloe names
while response not in redacted:
    if response in other_people.keys():
        typewriter(other_people[response], 0.05)
    else:
        typewriter(f"Hi {response.title()}! Tell Khloe I said hi.", 0.05)
    response = input(prompt)
    response = response.lower().strip()    

typewriter(f"Hi Khloe :> {greeting}", 0.05)

if "Feb 14" in date:
    visuals.flower()
else:
    visuals.heart()