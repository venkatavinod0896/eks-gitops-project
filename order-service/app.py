from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {"id": 1, "user": "Vinod", "product": "Laptop", "status": "created"},
    {"id": 2, "user": "Kiran", "product": "Mouse", "status": "shipped"}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "order-service"
    }), 200

@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders), 200

@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    user = data.get("user")
    product = data.get("product")

    if not user or not product:
        return jsonify({"error": "user and product are required"}), 400

    new_order = {
        "id": len(orders) + 1,
        "user": user,
        "product": product,
        "status": "created"
    }

    orders.append(new_order)
    return jsonify(new_order), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)