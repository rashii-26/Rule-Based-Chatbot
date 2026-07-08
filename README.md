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
