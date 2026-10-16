from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Dataset: Frequently Asked Questions & Answers
faqs = {
    "What is CodeAlpha?": "CodeAlpha is an internship platform that provides hands-on project tasks for tech students.",
    "How do I submit my task?": "You can submit your task by uploading your project code to GitHub and submitting the public repository URL.",
    "What is your refund policy?": "You can request a full refund within 30 days of purchase.",
    "How can I reset my password?": "Click on 'Forgot Password' on the login page and follow the email instructions.",
    "What are support hours?": "Our support team is available 24/7 via email and live chat.",
    "How do I track my order?": "You can track your order using the tracking link sent to your email.",
    "Hello": "Hello! Welcome to the FAQ Chatbot. How can I help you today?",
    "Bye": "Goodbye! Have a great day ahead!"
}

questions = list(faqs.keys())
answers = list(faqs.values())

# 2. Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_response(user_query):
    user_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(user_vector, question_vectors)
    
    best_match_idx = similarities.argmax()
    best_score = similarities[0, best_match_idx]
    
    if best_score < 0.2:
        return "I'm sorry, I couldn't find an answer to that question. Please rephrase."
    
    return answers[best_match_idx]

# 3. Interactive Terminal Loop
if __name__ == "__main__":
    print("========================================")
    print("      CodeAlpha FAQ Chatbot Active      ")
    print("   (Type 'exit' or 'quit' to stop)      ")
    print("========================================")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
            
        reply = get_response(user_input)
        print(f"Chatbot: {reply}")
