# from flask import Flask, render_template_string

# app = Flask(__name__)

# @app.route('/')
# def hr_questions():
#     return render_template_string(form)

# form = """
# <form action="/submit" method="post">
#   <label for="name">Name:</label><br>
#   <input type="text" id="name" name="name"><br>
#   <label for="question1">What is your current salary?</label><br>
#   <input type="text" id="question1" name="question1"><br>
#   <input type="submit" value="Submit">
# </form> 
# """


# '''

# What is your experience with programming languages such as Java, C++, or Python?
# How do you handle debugging and problem-solving in your projects?
# Can you explain the difference between a static and a dynamic website?
# How do you ensure the security of a web application?
# Have you worked with databases before? If so, which ones and in what capacity?
# How do you keep up with new technologies and industry best practices?
# Can you describe a technical challenge you faced and how you overcame it?
# How do you handle version control in your projects?
# Have you worked with API integrations before? If so, can you give an example?
# Can you explain the difference between agile and waterfall project management methodologies?
# '''
# # app = Flask(__name__)
# # @app.route('/')
# # def hr_questions():
# #     return 'Welcome to the HR Questionnaire!'
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     salary = request.form['question1']
#     return f'Thank you for your submission, {name}! Your current salary is {salary}.'
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template_string, request

app = Flask(__name__)

form = """
<form action="/submit" method="post">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name"><br>
  <label for="question1">What is your current salary?</label><br>
  <input type="text" id="question1" name="question1"><br>
  <input type="submit" value="Submit">
</form> 
"""

@app.route('/')
def hr_questions():
    return render_template_string(form)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    salary = request.form['question1']
    return f'Thank you for your submission, {name}! Your current salary is {salary}.'
if __name__ == '__main__':
     app.run(debug=True)