from flask import Flask, request, jsonify

app = Flask(__name__)

LIST = [
    {"name": "brian", "email": "brin@hotmail.com"},
    {"name": "bunyod", "email": "bun@hotmail.com"},
    {"name": "joyson", "email": "joy@hotmail.com"},
]

@app.route("/get-user")
def get_user():
    user_data = {

    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
