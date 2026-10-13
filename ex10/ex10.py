def chatbot(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "name" in user_input:
        return "I am an AI chatbot."
    elif "how are you" in user_input:
        return "I am fine! Thank you."
    elif "college" in user_input:
        return "College is a place for learning and development."
    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."
    elif "thank" in user_input:
        return "You're welcome!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand your question."
print("===== AI CHATBOT =====")
print("Type 'bye' to exit.")
while True:
    user = input("You: ")
    response = chatbot(user)
    print("Bot:", response)
    if "bye" in user.lower():
        break
 
