from flask import Flask, render_template_string, request
import requests
app = Flask(__name__)

form = """
<form action="/submit" method="post">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name"><br>
  <label for="question">What is your experience with programming languages such as Java, C++, or Python?</label><br>
  <textarea id="question1" name="question1"></textarea><br>

  <label for="question">Can you explain the difference between a static and a dynamic website?</label><br>
  <textarea id="question2" name="question2"></textarea><br>

  <label for="question">Can you describe a technical challenge you faced and how you overcame it?</label><br>
  <textarea id="question3" name="question3"></textarea><br>

  <label for="question">What are your long-term career goals?</label><br>
  <textarea id="question4" name="question4"></textarea><br>

  <label for="question">Have you worked with API integrations before? If so, can you give an example?</label><br>
  <textarea id="question5" name="question5"></textarea><br>

  <label for="question">How do you ensure the security of a web application?</label><br>
  <textarea id="question6" name="question6"></textarea><br>

  <label for="question">How do you handle version control in your projects?</label><br>
  <textarea id="question7" name="question7"></textarea><br>

  <label for="question">Why are you interested in this position?</label><br>
  <textarea id="question8" name="question8"></textarea><br>

  <label for="question">How do you continue to learn and grow in your career?</label><br>
  <textarea id="question9" name="question9"></textarea><br>

  <label for="question">How do you handle stress and pressure in the workplace?</label><br>
  <textarea id="question10" name="question10"></textarea><br>

  <label for="question">How do you handle conflicts or disagreements with coworkers or superiors?</label><br>
  <textarea id="question11" name="question11"></textarea><br>

  <label for="question">How do you handle feedback, both positive and negative?</label><br>
  <textarea id="question12" name="question12"></textarea><br>

  <label for="question">Can you give an example of a project you took ownership of and saw through to completion?</label><br>
  <textarea id="question13" name="question13"></textarea><br>

  <label for="question">How do you prioritize tasks and manage your time effectively?</label><br>
  <textarea id="question14" name="question14"></textarea><br>

  <input type="submit" value="Submit">
</form> 
"""

# def hr():
#     tech=["What is your experience with programming languages such as Java, C++, or Python?",
#     "How do you handle debugging and problem-solving in your projects?",
#     "Can you explain the difference between a static and a dynamic website?",
#     "How do you ensure the security of a web application?",
#     "Have you worked with databases before? If so, which ones and in what capacity?",
#     "How do you keep up with new technologies and industry best practices?",
#     "Can you describe a technical challenge you faced and how you overcame it?",
#     "How do you handle version control in your projects?",
#     "Have you worked with API integrations before? If so, can you give an example?",
#     "Can you explain the difference between agile and waterfall project management methodologies?"]
#     hrq=["Why are you interested in this position?",
#     "What are your long-term career goals?",
#     "Can you tell me about a time when you had to work in a team and what role you played?",
#     "How do you handle stress and pressure in the workplace?",
#     "How do you handle conflicts or disagreements with coworkers or superiors?",
#     "Can you give an example of a time when you had to adapt to a new situation or challenge?",
#     "How do you prioritize tasks and manage your time effectively?",
#     "How do you handle feedback, both positive and negative?",
#     "Can you give an example of a project you took ownership of and saw through to completion?",
#     "How do you continue to learn and grow in your career?"]
#     x=random.sample(range(1,11),5)
#     form = """
#     <form action="/submit" method="post">
#       <label for="name">Name:</label><br>
#       <textarea id="name" name="name"><br>
#       <label for="question">f'{x[0]}'</label><br>
#       <textarea id="question" name="question"><br>
#       <input type="submit" value="Submit">
#     </form> 
#     """





@app.route('/')
def hr_questions():
    #hr()
    return render_template_string(form)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    q1 = request.form['question1']
    q2 = request.form['question2']
    q3 = request.form['question3']
    q4 = request.form['question4']
    q5 = request.form['question5']
    q6 = request.form['question6']
    q7 = request.form['question7']
    q8 = request.form['question8']
    q9 = request.form['question9']
    q10 = request.form['question10']
    q11 = request.form['question11']
    q12 = request.form['question12']
    q13 = request.form['question13']
    q14 = request.form['question14']
    data={
        'nameofcandidate':name,
        'question1':q1,
        'question2':q2,
        'question3':q3,
        'question4':q4,
        'question5':q5,
        'question6':q6,
        'question7':q7,
        'question8':q8,
        'question9':q9,
        'question10':q10,
        'question11':q11,
        'question12':q12,
        'question13':q13,
        'question14':q14,

    }
    database_url='https://itmupmzkwnbtvvihasvz.supabase.co'
    api_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml0bXVwbXprd25idHZ2aWhhc3Z6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzMxNjk2OTAsImV4cCI6MTk4ODc0NTY5MH0.9kwDA3xp-v2LXHw_mYAGOFdV11aEWiRxoGSavhEtifk'
    r = requests.post(f'{database_url}/public/users', json=data, headers={'Authorization': api_key})
    #print(r.status_code)
    return 'Form Submitted Succes'
    # return f'Thank you for your submission, {name}! Your current salary is {q1}.'
if __name__ == '__main__':
     app.run(debug=True)