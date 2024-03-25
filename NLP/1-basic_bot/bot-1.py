import random

#Let us have some random responses
random_responses = ["Nice to hear. How was your day?"
                    "That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Do you have any specific questions in mind?"
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I am your first chatbot Galaxy, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")

while True:
    # Input from the user
    user_input = input("> ")
    if user_input.lower() == "bye":
        # exit the loop if user typed 'bye'
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("It was nice talking to you, goodbye!")