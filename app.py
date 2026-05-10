from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "DevOps Project Successfully Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
return "Webhook CI/CD Working"
