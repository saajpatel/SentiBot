import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# VADER sentiment lexicon for SIA
nltk.download('vader_lexicon')

# initialize SIA
sia = SentimentIntensityAnalyzer()

# Function to analyze polarity score
def sentiment_result(text):
    score = sia.polarity_scores(text)['compound']
    if (score >= 0.5):
        return "pos"
    elif (score <= -0.5):
        return "neg"
    else:
        return "neu"

#Generate appropiate response based on sentiment
def response_generator(user_input, context):
    senti = sentiment_result(user_input)
    response = ""

    if (senti == "pos"):
        response = "I'm glad to hear that! "
    elif (senti == "neg"):
        response = "Sorry to hear that! "
    else:
        response = "Got it. "
    
    if "help" in user_input.lower():
        response += "How can I assist you further?"
    elif "issue" in user_input.lower():
        response += "Let me see if I can resolve this issue for you."
    else:
        response += "What else would you like to discuss?"
    
    if context:
        last_input = context[-1]
        if "help" in last_input.lower():
            response += " You mentioned needing help earlier. Can you provide more details?"
        elif "issue" in last_input.lower():
            response += " Let's work on the issue that you mentioned."

    context.append(user_input)
    return response

# Chat Bot Loop
print("Customer Chat Bot (Type 'exit' to exit)")
context = []
while True:
    user_input = input("You: ")
    if (user_input == "exit"):
        print("Bot: Thank you for chatting! Have a great day!")
        break
    bot_output = response_generator(user_input, context)
    print("Bot: " + bot_output + "\n")