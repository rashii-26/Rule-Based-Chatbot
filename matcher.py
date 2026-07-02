"""
matcher.py
-----------
This file handles the FUZZY MATCHING logic.
We use RapidFuzz to compare the user's question with every question
stored in our knowledge base and find the closest match.
"""

from rapidfuzz import fuzz, process


# Minimum similarity score (out of 100) required to accept a match.
SIMILARITY_THRESHOLD = 60


def find_best_match(user_question, knowledge_base):
    """
    Compares the user's question against all FAQ questions in the
    knowledge base and returns the best matching entry (if good enough).

    :param user_question: the question typed by the student
    :param knowledge_base: list of dicts like {"question": ..., "answer": ...}
    :return: tuple (matched_answer_or_None, similarity_score)
    """

    # Create a simple list of just the FAQ questions to compare against
    all_questions = [item["question"] for item in knowledge_base]

    # process.extractOne() finds the single best match from a list of choices.
    # It uses fuzz.WRatio (a weighted ratio) by default, which works well
    # for short sentences like FAQ questions.
    best_match = process.extractOne(
        user_question,
        all_questions,
        scorer=fuzz.token_set_ratio
    )

    # best_match is a tuple: (matched_question, score, index)
    if best_match is None:
        return None, 0

    matched_question, score, index = best_match

    # Only accept the match if score meets our threshold
    if score >= SIMILARITY_THRESHOLD:
        matched_answer = knowledge_base[index]["answer"]
        return matched_answer, score
    else:
        return None, score