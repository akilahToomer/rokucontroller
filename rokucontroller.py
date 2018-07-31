from flask import Flask

app = Flask(__name__)
ask = Ask(app, "/roku controller")

if __name__ == '__main__':
    app.run(debug=True)

@ask.launch
def start_skill():
    welcome_message = 'Welcome to your roku controller'
    return question(welcome_message)

@ask.intent("YesIntent")
def yes_intent():
    return statement('Action continued')

@ask.intent("NoIntent")
def no_intent():
    return statement('Action canceled')
