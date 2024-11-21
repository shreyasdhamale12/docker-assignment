from flask import Flask, Response

app = Flask(__name__)  # Create the Flask app

@app.route('/')
def hello():
    response = Response("This is DeveOps assignment of Shreyas Dhamale,1062231000")
    return response  # Ensure this line is indented properly with 4 spaces

if __name__ == "__main__":
    app.run(host='0.0.0.0')  # Ensure this line is also indented properly
