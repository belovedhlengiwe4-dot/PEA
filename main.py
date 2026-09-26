print("Hello, what is your name?")
name = input()
if name == "Pea":
    print("Hey, I'm also Pea. There's not many of us with such a cute name.")
else:
    print("Hi, " + name + ". Nice to meet you.")

print("How old are you? ")
age = input()
print("Wow, " + age + " years old! That's great.")

print("How was your day? ")
response = input()
if response.lower() == "good":
    print("Glad to hear that. ☺️")
elif response.lower() == "neutral" or response.lower() == "not so good":
    print("It has been scientifically proven that looking at Cha Woo Min photos elevates one's mood. \nIt won't hurt to give it a shot. 😏")
elif response.lower() == "bad":
    print("Sorry to hear that. Take a mini nap and reset.")
else:
    print("I see.")