'''
This is the main file for the EnSys chatbot. It initializes the Flask app and loads the chatbot with the API key.
'''
import nltk
nltk.download('vader_lexicon')
from flask import Flask
from routes import initialize_routes
from bot import EnSysBot, load_config

# Load environment variables and get the API key
try:
    api_key = load_config()
    engine ="ft:gpt-3.5-turbo-0125:ensys:empatheticd:9XQSt7AX"
    bot = EnSysBot(engine, api_key)
except Exception as e:
    raise e

# Initialize Flask app
app = Flask(__name__)

# Initialize routes
initialize_routes(app, bot)

if __name__ == '__main__':
    app.run(debug=True)
