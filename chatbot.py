"""
chatbot.py
-----------
The "brain" of the chatbot. It loads the knowledge base and uses
matcher.py to generate responses to user questions.
"""

from matcher import find_best_match
from utils import load_json_file, get_fallback_message


class StudentSupportBot:
    """
    A simple rule-based chatbot that answers student queries
    using fuzzy matching against a JSON knowledge base.
    """

    def __init__(self, kb_path="knowledge_base.json"):
        # Load the knowledge base once when the bot is created
        self.knowledge_base = load_json_file(kb_path)

    def get_response(self, user_question):
        """
        Takes a user question and returns the best possible answer.
        :param user_question: string typed by the student
        :return: string answer
        """
        # Basic input cleaning
        user_question = user_question.strip()

        if not user_question:
            return "Please type a question so I can help you."

        # Find the best matching FAQ using fuzzy matching
        answer, score = find_best_match(user_question, self.knowledge_base)

        if answer:
            return answer
        else:
            return get_fallback_message()