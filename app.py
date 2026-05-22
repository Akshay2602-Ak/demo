def classify_text(text):
    positive_words = ["good", "great", "happy", "excellent", "awesome"]
    negative_words = ["bad", "sad", "poor", "angry", "worst"]

    text = text.lower()

    if any(word in text for word in positive_words):
        return "Positive"
    elif any(word in text for word in negative_words):
        return "Negative"
    else:
        return "Neutral"


print(classify_text("This is awesome"))