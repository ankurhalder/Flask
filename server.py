from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return {"message": "Hello World"}


print("hello world")


# To run the server use the following command
# flask --app server --debug run
# curl -X GET -i -w '\n' localhost:5000