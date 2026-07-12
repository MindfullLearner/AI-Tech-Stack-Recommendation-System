# 🤖 AI Tech Stack Recommendation System

A simple AI-inspired recommendation system built using **Python**. This project recommends suitable software engineering career paths based on the user's existing technical skills and suggests additional skills to learn for each recommended career.

## 📌 Project Overview

The AI Tech Stack Recommendation System compares a user's skills with predefined career skill requirements. It calculates a match percentage for each career, ranks them from highest to lowest, and provides personalized learning recommendations.

This project demonstrates the use of basic AI recommendation logic using Python fundamentals without relying on machine learning libraries.

---

## ✨ Features

- Accepts user skills as comma-separated input.
- Matches user skills with different software engineering career paths.
- Calculates compatibility percentage for each career.
- Sorts recommendations from highest to lowest match.
- Displays only relevant career recommendations (0% matches are hidden).
- Shows:
  - ✅ Skills the user already has.
  - ❌ Skills the user should learn.
- Handles empty input by prompting the user again.

---

## 💻 Technologies Used

- Python 3
- Dictionaries
- Lists
- Loops
- Functions
- Conditional Statements
- String Manipulation
- Sorting using `sorted()` and `lambda`

---

## 📂 Career Paths Included

- Data Scientist
- Frontend Developer
- Backend Developer
- DevOps Engineer
- MERN Stack Developer

---

## ⚙️ How It Works

1. The user enters their technical skills.
2. The program cleans and processes the input.
3. The user's skills are compared against each career's required skills.
4. A match percentage is calculated using:

```text
Match Percentage = (Matched Skills / Total Required Skills) × 100
```

5. Careers are sorted from the highest compatibility to the lowest.
6. The program displays:
   - Career Name
   - Match Percentage
   - Skills Already Known
   - Skills to Learn

---

## ▶️ Example

### Input

```text
Enter your skills:
HTML, CSS, JavaScript
```

### Output

```text
🏆 Career: Frontend Developer
📊 Match Percentage: 75.00%

✔ Skills You Have
HTML
CSS
JavaScript

❌ Skills You Should Learn
React

-----------------------------------

🏆 Career: MERN Stack Developer
📊 Match Percentage: 50.00%

✔ Skills You Have
HTML
CSS
JavaScript

❌ Skills You Should Learn
React
Node.js
MongoDB
```

---

## 📁 Project Structure

```
AI-Tech-Stack-Recommendation-System/
│
├── main.py
└── README.md
```

---

## 🧠 Concepts Used

- Dictionaries
- Nested Dictionaries
- Lists
- Loops
- Nested Loops
- Functions
- Conditional Statements
- String Manipulation
- Sorting
- Python Lambda Functions
- User Input Validation

---

## 🚀 Future Improvements

Some features that can be added in future versions:

- Graphical User Interface (Tkinter)
- Skill proficiency levels (Beginner, Intermediate, Advanced)
- Career descriptions
- More software engineering career paths
- Machine Learning based recommendations
- Reading career data from a database or CSV file
- Export recommendations as a PDF report

---

## 🎯 Learning Outcomes

Through this project, I learned:

- How recommendation systems work at a basic level.
- How to compare user input with stored data.
- How to organize data using dictionaries and lists.
- How to calculate compatibility percentages.
- How to sort data using Python's `sorted()` function and `lambda`.
- How to build an interactive command-line application.

---

## 👩‍💻 Author

**Nayab Maryam**

Software Engineering Student

DecodeLabs AI Internship - Week 3 Project
