import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session handling

# Function to load questions from CSV
def load_questions():
    questions = []
    with open('Questions.csv', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]  # Read and strip lines, ignoring empty ones
        for i in range(0, len(lines), 6):  # Increment by 6 for each question block
            question_text = lines[i+2].split(':', 1)[1].strip() if ':' in lines[i+2] else lines[i+2]
            option_a = lines[i+3].split(')', 1)[1].strip() if ')' in lines[i+3] else lines[i+3]
            option_b = lines[i+4].split(')', 1)[1].strip() if ')' in lines[i+4] else lines[i+4]
            answer = lines[i+5].split(':', 1)[1].strip() if ':' in lines[i+5] else lines[i+5]
            questions.append({
                'Category': lines[i],
                'Question': question_text,
                'A': option_a,
                'B': option_b,
                'Answer': answer
            })
    return questions

@app.route("/", methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        submitted_answers = request.form
        questions = session.get('questions', [])
        score = 0
        incorrect_questions = []
        category_scores = {}
        for i, question in enumerate(questions, start=1):
            user_answer = submitted_answers.get(f'question{i}')
            category = question['Category']
            if category not in category_scores:
                category_scores[category] = {'correct': 0, 'total': 0}
            category_scores[category]['total'] += 1
            if user_answer == question['Answer']:
                score += 1
                category_scores[category]['correct'] += 1
            else:
                question['UserAnswer'] = user_answer
                incorrect_questions.append(question)
        percentage = (score / len(questions)) * 100
        category_percentages = {category: scores['correct'] / scores['total'] * 100 for category, scores in category_scores.items()}
        return render_template('results.html', score=score, total=len(questions), percentage=percentage,
                               incorrect_questions=incorrect_questions, category_percentages=category_percentages)
    else:
        questions = load_questions()
        random.shuffle(questions)
        questions = questions[:30]  # Limit to 30 random questions
        session['questions'] = questions
        return render_template('index.html', questions=questions)

if __name__ == "__main__":
    app.run(debug=True)