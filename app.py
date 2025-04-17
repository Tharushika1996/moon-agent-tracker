from flask import Flask

# Correct way to name the Flask app
agent_service_app = Flask(_name_)

@agent_service_app.route('/')
def home():
    return "Agent Service is Running!"

if _name_ == "_main_":
    agent_service_app.run(host="0.0.0.0", port=5000)