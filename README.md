# Python Quiz App

A simple command-line quiz app built with Python.

## Features

- Loads questions from a JSON file
- Shuffles question order each time the quiz starts
- Accepts answers A, B, C, or D
- Lets the user retry after a wrong answer
- Tracks progress during the quiz
- Shows final score, percentage, and grade at the end

## Files

- `quiz-app.py` — main Python program
- `example.json` — quiz question data

## How it works

The program reads quiz questions from `example.json`, randomizes their order, asks each question in the terminal, checks the user's answer, and prints the final result at the end.

## Requirements

- Python 3 installed on your computer

## How to run

1. Open the project folder in your terminal.
2. Run:

```bash
python quiz-app.py
```

If that does not work, try:

```bash
python3 quiz-app.py
```

## Example question format

```json
{
  "question": "Who was the primary leader of the Reign of Terror",
  "options": ["Georges Danton", "Maximilien Robespierre", "Maria Antoinette", "King Louis XVI"],
  "answer": 1
}
```

## What I practiced

- Python basics
- Functions
- Loops and conditionals
- User input handling
- Working with JSON files
- Randomizing data

## Possible future improvements

- Add more questions and categories
- Add difficulty levels
- Add a timer
- Store high scores
- Build a GUI or web version later

## Author

Created by alex-slovakia