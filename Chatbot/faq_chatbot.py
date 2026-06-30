import json
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')
with open("faqs.json", "r") as file:
    faqs = json.load(file)
questions = [faq["question"] for faq in faqs]
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [
        word for word in tokens
        if word not in stopwords.words('english')
        and word not in string.punctuation
    ]
    return " ".join(tokens)
processed_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)
def get_response(user_query):
    processed_query = preprocess(user_query)
    query_vector = vectorizer.transform([processed_query])
    similarities = cosine_similarity(query_vector, faq_vectors)
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]
    if best_score < 0.2:
        return "Sorry, I couldn't find a relevant answer."
    return faqs[best_match_index]["answer"]
if __name__ == "__main__":
    print("FAQ Chatbot")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)
