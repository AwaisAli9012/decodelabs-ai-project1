# ============================================================
#  DecodeLabs | Artificial Intelligence | Project 1
#  Rule-Based AI Chatbot
#  Batch: 2026
# ============================================================

def get_response(user_input):
    """
    Core AI logic: takes user input and returns a response
    using if-else decision making (rule-based system).
    """

    # Normalize input: lowercase and strip extra spaces
    user_input = user_input.lower().strip()

    # ── Greetings ──────────────────────────────────────────
    if user_input in ["hi", "hello", "hey", "salam", "assalamualaikum"]:
        return "Hello! Welcome to the DecodeLabs AI Chatbot. How can I help you today?"

    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm just a program, but I'm running perfectly! Thanks for asking. 😊"

    elif user_input in ["good morning", "good morning!"]:
        return "Good morning! Hope you have a productive day ahead. ☀️"

    elif user_input in ["good night", "good night!"]:
        return "Good night! Get some rest. 🌙"

    # ── Identity Questions ─────────────────────────────────
    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I am DecoBot, a Rule-Based AI Chatbot built for DecodeLabs Project 1!"

    elif user_input in ["who made you", "who created you", "who built you"]:
        return "I was built by a DecodeLabs intern as part of the AI Industrial Training Program."

    elif user_input in ["what can you do", "help", "what do you do"]:
        return (
            "I can answer simple questions! Try asking me:\n"
            "  - 'What is AI?'\n"
            "  - 'What is machine learning?'\n"
            "  - 'Tell me a joke'\n"
            "  - 'What is Python?'\n"
            "  - 'bye' to exit"
        )

    # ── AI / Tech Knowledge ────────────────────────────────
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return (
            "Artificial Intelligence (AI) is the simulation of human intelligence\n"
            "by machines — enabling them to learn, reason, and make decisions."
        )

    elif "machine learning" in user_input:
        return (
            "Machine Learning is a branch of AI where systems learn from data\n"
            "and improve their performance over time without being explicitly programmed."
        )

    elif "deep learning" in user_input:
        return (
            "Deep Learning uses neural networks with many layers to analyze data.\n"
            "It powers things like image recognition, ChatGPT, and voice assistants."
        )

    elif "what is python" in user_input or "python" in user_input:
        return (
            "Python is a popular, beginner-friendly programming language.\n"
            "It is widely used in AI, data science, and web development."
        )

    elif "what is a chatbot" in user_input or "chatbot" in user_input:
        return (
            "A chatbot is a program designed to simulate conversation with humans.\n"
            "Rule-based chatbots (like me!) use if-else logic to respond.\n"
            "Advanced chatbots use AI models like GPT to generate responses."
        )

    # ── Fun Responses ──────────────────────────────────────
    elif "joke" in user_input or "tell me a joke" in user_input:
        return (
            "Why do programmers prefer dark mode?\n"
            "Because light attracts bugs! 🐛😄"
        )

    elif "quote" in user_input or "motivate me" in user_input:
        return "\"The best way to predict the future is to create it.\" — Abraham Lincoln 💡"

    elif user_input in ["thank you", "thanks", "shukriya"]:
        return "You're welcome! Happy to help. 😊"

    # ── Exit Commands ──────────────────────────────────────
    elif user_input in ["bye", "goodbye", "exit", "quit", "khuda hafiz"]:
        return "EXIT"  # Special signal to break the loop

    # ── Default / Unknown Input ────────────────────────────
    else:
        return (
            "I'm not sure how to respond to that yet.\n"
            "I'm a rule-based bot — try asking about AI, Python, or type 'help'."
        )


def run_chatbot():
    """
    Main loop: keeps the chatbot running until the user exits.
    """
    print("=" * 55)
    print("   Welcome to DecoBot — Rule-Based AI Chatbot")
    print("   Powered by DecodeLabs | Batch 2026")
    print("=" * 55)
    print("   Type 'help' to see what I can do.")
    print("   Type 'bye' to exit.")
    print("=" * 55)
    print()

    # Continuous loop — runs until user types exit command
    while True:
        user_input = input("You: ")

        # Skip empty input
        if not user_input.strip():
            continue

        response = get_response(user_input)

        # Check for exit signal
        if response == "EXIT":
            print("DecoBot: Goodbye! Keep building and keep learning. 🚀")
            print("=" * 55)
            break

        print(f"DecoBot: {response}")
        print()


# ── Entry Point ────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot() 
