# AI Student Support Chatbot

A simple, rule-based chatbot built to handle common student queries related to attendance, fees, exams, library, hostel, placements, scholarships, holidays, timetable, and faculty. The chatbot uses fuzzy string matching to find the closest matching FAQ and does not rely on any AI model, external API, or internet connection.

## Tech Stack

- Python 3.8+
- Streamlit (for the web-based chat interface)
- RapidFuzz (for fuzzy text matching)
- JSON (used as a simple knowledge base; no database required)

## Project Structure

```
StudentSupportBot/
├── app.py                 Streamlit UI (main entry point)
├── chatbot.py              Chatbot logic (loads knowledge base, generates responses)
├── matcher.py               Fuzzy matching logic using RapidFuzz
├── knowledge_base.json      FAQ data (question-answer pairs)
├── utils.py                 Helper functions
├── requirements.txt         Python dependencies
└── README.md                 Project documentation
```

## Installation

1. Clone or download this repository.
2. Open a terminal inside the project folder.
3. (Optional but recommended) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      (Windows)
   source venv/bin/activate   (Mac/Linux)
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Run

```
streamlit run app.py
```

This will open the chatbot in your default web browser, typically at `http://localhost:8501`.

## How It Works

1. `knowledge_base.json` stores all FAQ questions and answers as a list of objects in the form `{"question": ..., "answer": ...}`.
2. When the app starts, `chatbot.py` loads this JSON file into memory.
3. When a student types a question into the Streamlit chat interface (`app.py`), the input is passed to the `get_response()` method in `chatbot.py`.
4. `matcher.py` uses RapidFuzz's `process.extractOne()` function along with the `token_set_ratio` scorer to compare the user's question against every stored FAQ question and calculate a similarity score between 0 and 100.
5. The FAQ question with the highest similarity score is selected.
   - If the score is 60 or above, the bot returns the matching answer.
   - If the score is below 60, the bot returns a fallback message: "Sorry, I could not find an answer to your question. Please contact the Academic Office."
6. The conversation history (both user and bot messages) is stored using Streamlit's `session_state`, so it persists while the app is running.
7. The Clear Chat button resets the conversation back to the initial greeting message.

No machine learning model, embeddings, or external API calls are used. The matching is based entirely on string similarity scoring.

## Notes on the Matching Threshold

The similarity threshold was set to 60 after testing several real and irrelevant queries. This value was chosen because it correctly matches genuine but short or casually phrased questions (for example, "placement package" or "library timing") while still rejecting completely unrelated questions (for example, "what's the weather today"). The `token_set_ratio` scorer was chosen over the default `WRatio` because it does not depend on word order and performed more reliably on both matching and non-matching test cases.

## Viva Questions and Answers

**Q1. What algorithm does RapidFuzz use for matching?**
This project uses `fuzz.token_set_ratio`, which compares the sets of words in two strings regardless of order. This makes it effective for short or reordered questions, such as "package placement" matching "What is the average placement package?"

**Q2. Why was fuzzy matching chosen instead of a real AI model?**
Fuzzy matching is lightweight, fast, works offline, does not require training data or GPUs, and is easy to explain and reason about. This makes it well suited for a simple FAQ-based support system.

**Q3. What is the similarity threshold, and why was 60 chosen?**
The threshold is 60 out of 100. This value was selected through testing: real FAQ-style queries with typos or short phrasing scored between roughly 60 and 90, while unrelated queries scored well below 40. A threshold of 60 keeps a safe margin on both sides.

**Q4. What happens if no good match is found?**
The bot returns a polite fallback message directing the student to contact the Academic Office, rather than guessing or returning an incorrect answer.

**Q5. How is the knowledge base stored?**
In a JSON file (`knowledge_base.json`) as a list of question-answer pairs. JSON was chosen because it is human-readable, easy to edit, and does not require setting up a database.

**Q6. How does Streamlit maintain chat history?**
Through `st.session_state`, a Streamlit feature that persists data across reruns of the script, since Streamlit reruns the entire script on every user interaction.

**Q7. Can this chatbot understand context or follow-up questions?**
No. Each question is matched independently against the knowledge base. The chatbot has no memory of previous questions; it is a stateless matcher rather than a conversational AI.

**Q8. How would you add a new FAQ?**
By adding a new `{"question": ..., "answer": ...}` entry to `knowledge_base.json`. No code changes are required.

**Q9. What does `process.extractOne()` do?**
It is a RapidFuzz function that takes a query string and a list of choices, and returns the single best-matching choice along with its similarity score and index in the list.

**Q10. Does this chatbot use any external API or internet connection?**
No. Everything runs locally. The JSON file, matching logic, and user interface all work offline using only the installed Python libraries.