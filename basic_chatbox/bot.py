import random
import re


class SimpleFinancialChatbot:
    def __init__(self):
        # Define responses for different topics
        self.responses = {
            "greeting": [
                "Hello! I'm your simple financial assistant.",
                "Hi there! How can I help with your financial questions?",
                "Welcome! I'm here to help with basic financial advice."
            ],
            "goodbye": [
                "Goodbye! Have a great day.",
                "See you later! Remember to save for the future.",
                "Bye! Thanks for chatting."
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "Anytime! That's what I'm here for."
            ],
            "stock": [
                "When investing in stocks, diversification is key to managing risk.",
                "Stocks can be volatile in the short term but historically provide good returns over long periods.",
                "Consider your risk tolerance and investment timeline when choosing stocks."
            ],
            "saving": [
                "A good rule of thumb is to save at least 20% of your income.",
                "Emergency funds should cover 3-6 months of expenses.",
                "Consider high-yield savings accounts for your emergency fund."
            ],
            "retirement": [
                "Start saving for retirement as early as possible to benefit from compound interest.",
                "Consider contributing to tax-advantaged accounts like 401(k)s or IRAs.",
                "The 4% rule suggests withdrawing 4% of your retirement savings annually."
            ],
            "budget": [
                "The 50/30/20 rule suggests using 50% of income for needs, 30% for wants, and 20% for savings.",
                "Tracking your expenses is the first step to creating an effective budget.",
                "Review and adjust your budget regularly to stay on track."
            ],
            "debt": [
                "Consider paying off high-interest debt first (like credit cards).",
                "The debt snowball method involves paying off smallest debts first for psychological wins.",
                "The debt avalanche method focuses on highest interest rates first and saves more money."
            ],
            "unknown": [
                "I'm not sure I understand. Could you rephrase that?",
                "I'm a simple bot and don't have an answer for that.",
                "I'm still learning and don't have information on that topic yet."
            ]
        }

        # Define patterns to match user input
        self.patterns = {
            "greeting": r"hello|hi|hey|greetings|good morning|good afternoon|good evening",
            "goodbye": r"bye|goodbye|see you|exit|quit",
            "thanks": r"thanks|thank you|appreciate",
            "stock": r"stock|stocks|invest|investing|investment|share|shares",
            "saving": r"save|saving|savings|emergency fund",
            "retirement": r"retire|retirement|401k|ira|pension",
            "budget": r"budget|budgeting|spending|expense|expenses",
            "debt": r"debt|loan|loans|credit card|mortgage|interest"
        }

    def get_response(self, user_input):
        """Generate a response based on user input"""
        user_input = user_input.lower()

        # Check for matches in patterns
        for topic, pattern in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(self.responses[topic])

        # If no match is found
        return random.choice(self.responses["unknown"])

    def start_chat(self):
        """Start the chatbot conversation"""
        print(
            "Financial Chatbot: Hello! I'm a simple financial chatbot. Ask me about stocks, saving, retirement, budgeting, or debt. Type 'exit' to end our conversation.")

        while True:
            user_input = input("You: ")

            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                print("Financial Chatbot: " + random.choice(self.responses["goodbye"]))
                break

            response = self.get_response(user_input)
            print("Financial Chatbot:", response)


# Demo usage
if __name__ == "__main__":
    chatbot = SimpleFinancialChatbot()
    chatbot.start_chat()