from flask import Flask, request, jsonify

app = Flask(__name__)

# Route GET đơn giản
@app.route("/")
def home():
    return "Xin chào từ Python Flask Web Server!"

# Route nhận POST JSON để xử lý vào lệnh MT5 chẳng hạn
@app.route("/order", methods=["POST"])
def order():
    data = request.json
    print("Nhận được lệnh:", data)
    # Ở đây bạn có thể gọi lệnh MT5 từ Python, ví dụ order_send(...)
    return jsonify({"status": "Đã nhận", "order": data})

# Chạy web server tại localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)