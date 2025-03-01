# SentiBot
Simple Sentiment Analysis Bot

SentiBot was implemented in Python. It uses VADER, a lexicon sentiment analysis tool from NLTK to determine the sentiment of user inputs, and generates responses accordingly. Additionally, it provides context-aware responses depending on certain keywords used by the user. The chatbot is capable of handling positive, negative, and neutral sentiments, and responds accordingly.

# Features:

Sentiment Analysis: Classify user inputs as positive, negative, or neutral with VADER lexicon sentiment analysis tool to accurately determine sentiment of user inputs.

Context-Aware Responses: Maintains context from user inputs by saving user responses in a simple list, to provide more relevant and contextual responses.

# Requirements

Python 3.6+

NLTK

# Example

```console
Customer Chat Bot (Type 'exit' to exit)
You: I'm so happy! I just got a promotion at work!
Bot: I'm glad to hear that! What else would you like to discuss?

You: Can you help me with something?
Bot: Got it. How can I assist you further?

You: exit
Bot: Thank you for chatting! Have a great day!

```
```console
Customer Chat Bot (Type 'exit' to exit)
You: I need help with my homework.
Bot: Got it. How can I assist you further?

You: I'm struggling with math problems.
Bot: Sorry to hear that! What else would you like to discuss? You mentioned needing help earlier. Can you provide more details?

You: exit
Bot: Thank you for chatting! Have a great day!

```
