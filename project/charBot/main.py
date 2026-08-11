print("Hello! Welcome to the ChatBotn\n\n")
print("Hi I am a rule based ChatBot.")
print("You can chat with me and ask me basic question, Type 'Bye' to exit.")

#reply generation
def generate_reply(question):
    if question != "" :
        return responces[question]
    return "Out of memory capacity"

#extend memory
def extend_memory():
    question = input("Question: ").lower()
    answer = input("Answer: ")
    responces[question] = answer
    return

#create a small memory
responces = {
    "hello" : "Hi, how can I help you?",
    "how are you" : "I am fine thank you",
    "who are you" : "I am a dumb chat bot",
    "motivate me" : "she deserves better and you deserve shit.",
    "happy" : "So what?",
    "what is function" : "Go watch YouTube"
}

#user input
while True:
    user_input = input("please ask your question: ").lower()
    if user_input == "bye":
        print("\n\nNice chatting with you!")
        break
    elif user_input == "admin":
        extend_memory()
        print("New information added to the memory")
        continue
    reply = generate_reply(user_input)
    print(reply)
