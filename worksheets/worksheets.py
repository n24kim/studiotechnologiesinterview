#! /usr/bin/env python

import random
import flask

app = flask.Flask(__name__)

NUM_QUESTIONS = 10

def generate_question():
    '''Generate two random numbers to be multiplied'''
    n1 = random.randint(1, 12)
    n2 = random.randint(1, 12)
    return {'n1': n1, 'n2': n2}

@app.route('/', methods=['GET', 'POST'])
def hello():
    incorrect_questions = None
    if flask.request.method == 'POST':
        incorrect_questions = []
        for i in range(NUM_QUESTIONS):
            n1 = flask.request.form.get('question{}n1'.format(i+1))
            n2 = flask.request.form.get('question{}n2'.format(i+1))
            answer = flask.request.form.get('question{}answer'.format(i+1))
            try:
                n1 = int(n1)
                n2 = int(n2)
                answer = int(answer)
            except (TypeError, ValueError):
                incorrect_questions.append(i+1)
            else:
                if answer != n1 * n2:
                    incorrect_questions.append(i+1)

    output = []
    questions = [generate_question() for i in range(NUM_QUESTIONS)]
    return flask.render_template(
        'index.html',
        questions=questions,
        incorrect_questions=incorrect_questions
    )

if __name__ == '__main__':
    app.run(debug=True)

