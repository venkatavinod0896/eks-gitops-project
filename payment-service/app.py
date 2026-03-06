from flask import Flask, jsonify, request

app = Flask(__name__)

payments = [
    {"id": 1, "order_id": 1, "amount": 50000, "status": "success"},
    {"id": 2, "order_id": 2, "amount": 1500, "status": "pending"}
]

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "payment-service"
    }), 200

@app.route("/payments", methods=["GET"])
def get_payments():
    return jsonify(payments), 200

@app.route("/payments", methods=["POST"])
def add_payment():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    order_id = data.get("order_id")
    amount = data.get("amount")

    if order_id is None or amount is None:
        return jsonify({"error": "order_id and amount are required"}), 400

    new_payment = {
        "id": len(payments) + 1,
        "order_id": order_id,
        "amount": amount,
        "status": "success"
    }

    payments.append(new_payment)
    return jsonify(new_payment), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)