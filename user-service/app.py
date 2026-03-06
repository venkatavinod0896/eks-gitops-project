from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Vinod", "email": "vinod@example.com"},
    {"id": 2, "name": "Kiran", "email": "kiran@example.com"}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "user-service"
    }), 200

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email
    }

    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)