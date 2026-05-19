def classify_text(text):
    positive_words = ["good", "great", "happy", "excellent",]
    negative_words = ["bad", "sad", "poor", "angry", "hate", "worst"]
    text = text.lower()

    if any(word in text for word in positive_words):
        return "Positive"
    elif any(word in text for word in negative_words):
        return "Negative"
    else:
        return "Neutral"


user_text = input("Enter your text: ")
result = classify_text(user_text)
print("AI Prediction:", result)

