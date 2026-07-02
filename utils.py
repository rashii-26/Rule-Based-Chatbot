"""
utils.py
---------
Helper functions used across the project.
Keeping these separate makes the code cleaner and easier to explain in a viva.
"""

import json


def load_json_file(file_path):
    """
    Loads and returns data from a JSON file.
    :param file_path: path to the JSON file
    :return: parsed JSON data (list of dicts here)
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_greeting_message():
    """
    Returns a friendly greeting message shown when the chat starts.
    """
    return (
        "Hi! I'm your Student Support Assistant.\n\n"
        "I can help you with questions about **attendance, fees, exams, "
        "library, hostel, placements, scholarships, holidays, timetable, "
        "and faculty**.\n\nGo ahead, ask me anything!"
    )


def get_fallback_message():
    """
    Returns the default message when no good match is found.
    """
    return (
        "Sorry, I could not find an answer to your question. "
        "Please contact the Academic Office."
    )