from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is a simple Flask app."

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name.capitalize()}!"

@app.route("/add", methods=["GET"])
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/json", methods=["POST"])
def json_example():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"message": f"Welcome, {name}!"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

