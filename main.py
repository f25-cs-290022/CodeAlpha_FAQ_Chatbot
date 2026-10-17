
# Task 2: FAQ Chatbot

print("Welcome to FAQ Chatbot!")
print("You can ask questions about courses, registration, and certificates.")
print("Type 'exit' to stop the chatbot.")

while True:
    question = input("\nYou: ").lower().strip()

    if question == "exit":
        print("Bot: Thank you for using FAQ Chatbot!")
        break

    elif "hello" in question or "hi" in question:
        print("Bot: Hello! How can I help you?")

    elif "course" in question:
        print("Bot: You can find course details on the official website.")

    elif "register" in question:
        print("Bot: Visit the registration page and fill out the form.")

    elif "certificate" in question:
        print("Bot: Complete your course requirements to get your certificate.")

    elif "password" in question:
        print("Bot: Click on Forgot Password on the login page.")

    elif "fee" in question:
        print("Bot: Please check the official website for course fees.")

    elif "support" in question or "help" in question:
        print("Bot: Please contact the support team.")

    else:
        print("Bot: Sorry, I don't know the answer to this question.")
