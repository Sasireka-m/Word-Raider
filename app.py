from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Load 5-letter words
def load_words():
    word_bank = []
    with open("words.txt") as f:
        for line in f:
            word = line.strip().lower()
            if len(word) == 5 and word.isalpha():
                word_bank.append(word)
    return word_bank

words = load_words()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'word' not in session:
        session['word'] = random.choice(words)
        session['turns'] = 0
        session['max_turns'] = 5
        session['misplaced'] = []
        session['incorrect'] = []
        session['message'] = ''
        session['history'] = []

    if request.method == 'POST':
        guess = request.form['guess'].lower()
        word = session['word']
        turns = session['turns']

        feedback = []
        misplaced = session['misplaced']
        incorrect = session['incorrect']

        if len(guess) != 5 or not guess.isalpha():
            session['message'] = 'Please enter a valid 5-letter word.'
            return redirect(url_for('index'))

        for i, c in enumerate(guess):
            if c == word[i]:
                feedback.append(c)
                if c in misplaced:
                    misplaced.remove(c)
            elif c in word:
                feedback.append('_')
                if c not in misplaced:
                    misplaced.append(c)
            else:
                feedback.append('_')
                if c not in incorrect:
                    incorrect.append(c)

        session['history'].append({'guess': guess, 'feedback': feedback})
        session['turns'] += 1

        if guess == word:
            session['message'] = 'Congratulations, you win!'
        elif session['turns'] >= session['max_turns']:
            session['message'] = f'Sorry, you lost. The word was {word}.'

    return render_template('index.html',
                           history=session['history'],
                           misplaced=session['misplaced'],
                           incorrect=session['incorrect'],
                           message=session['message'],
                           turns_left=session['max_turns'] - session['turns'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
