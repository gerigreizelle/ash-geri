


slang_replies = {
    "bet" : {
        "positive": ["Aight. I'm in!"],
        "negative": ["You sure you 'bet' on that?"],
        "neutral": []
    },

    "no cap" : {
        "positive": ["Realtalk"],
        "negative": [],
        "neutral": []
    },

    "cap" : {
        "positive": ["For real? Mad respect."],
        "negative": ["You know that's a cap, right?"],
        "neutral": []
    },

    "slay" : {
        "positive": ["Slay queen!"],
        "negative": [],
        "neutral": ["Slayyyy.. I guess?"]
    },

    "rizz" : {
        "positive": [],
        "negative": [],
        "neutral": []
    },

    "sus" : {
        "positive": [],
        "negative": [],
        "neutral": []
    },

    "mid" : {
        "positive": [],
        "negative": [],
        "neutral": []
    }
}


positive_tone = []


def chatbot():
    print("👾 Gen Z Chatbot is live! Type 'bye' to dip.")   
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'hi':
            print(f"Bot: Hello! What's good?")

        elif user_input.lower() == 'hello':
            print(f"Bot: Hi! What's good?")


        if user_input.lower() == "bye":
            print("Bot: Aight, catch you later! 🫶")
            break
        


chatbot()
