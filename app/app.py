from flask import Flask

agent_service_app = Flask(__name__)  


@agent_service_app.route('/')
def home():
    return "Agent Service is Running!"

if __name__ == "__main__":
    agent_service_app.run(host="0.0.0.0", port=5000)