
import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['attempts'] = 10
    session['secret_number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['attempts'] -= 1
    if guess == session['secret_number']:
        message = "Congratulations! You guessed the number!"
        return render_template('result.html', message=message)
    elif guess > session['secret_number']:
        message = "Your guess is too high. Try again."
    else:
        message = "Your guess is too low. Try again."
    if session['attempts'] == 0:
        message = f"Sorry, you've run out of attempts. The secret number was {session['secret_number']}."
        return render_template('result.html', message=message, lost=True)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
