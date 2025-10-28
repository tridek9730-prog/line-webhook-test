from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook-test/line-webhook', methods=['POST'])
def line_webhook():
    data = request.get_json()
    print("收到 LINE 訊息：", data)
    return 'OK', 200

if __name__ == '__main__':
    app.run()
