
# 🕹️ Word Raider - A 5-Letter Word Guessing Game

**Word Raider** is a fun and interactive word-guessing web game where players have to guess a random 5-letter word within 5 tries. It's built using **Python (Flask)** on the backend and **HTML/CSS** on the frontend, with animated styling for a modern user experience.

---

## 🔧 Features

- 🎯 Random word selection from a predefined list (`words.txt`)
- ⏳ 5 chances to guess the word
- 🧠 Feedback system:
  - ✔️ Correct letters in correct position
  - 🔁 Correct letters in wrong position
  - ❌ Incorrect letters
- 🎨 Animated gradient background for an appealing interface
- 🔁 Reset option to play again
- 🧠 Uses Flask session to manage state across attempts

---

## 📁 Project Structure

```
word_raider_web/
│
├── app.py                # Flask backend logic
├── words.txt             # 5-letter word list
│
├── templates/
│   └── index.html        # Frontend UI (HTML)
│
└── static/
    └── style.css         # Styling & background animation
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/word_raider_web.git
cd word_raider_web
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
# Activate virtual environment:
venv\Scripts\activate        # Windows
source venv/bin/activate       # Mac/Linux
```

### 3. Install Required Package

```bash
pip install flask
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Open in Browser

Navigate to:

```
http://127.0.0.1:5000/
```

Enjoy playing Word Raider!

---

## 💡 Future Improvements

- 🗂 Add difficulty levels (easy, medium, hard)
- 🔊 Sound effects for correct/incorrect guesses
- 🧑‍💻 Leaderboard with player scores
- 📱 Make mobile responsive

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and share!

---

## 🙋‍♀️ Author

**Sasireka M**  
Made with ❤️ using Python and Flask
