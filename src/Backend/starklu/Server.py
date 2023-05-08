# 导入所需的模块和函数
from flask import Flask, jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS = CORS(app)

# 创建一个用于返回数据的接口
@app.route("/api/data", methods=["GET"])
def get_data():
    # 模拟后端数据
    data = {
        "positive": 100000,
        "negative": 20000,
        "neutral": 60000
    }
    return jsonify(data)

# 启动应用程序
if __name__ == "__main__":
    app.run(debug=True)
