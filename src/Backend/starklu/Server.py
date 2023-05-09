# 导入所需的模块和函数
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/api/data", methods=["GET"])
def read_data():
    city_dict = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        sal_data = json.load(file)
        for location in sal_data.keys():
            if sal_data.get(location).get('gcc')[1] != 'r':
                city_dict[location] = sal_data.get(location).get('gcc')
    return city_dict


@app.route("/api/home", methods=["GET"])
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
    file_name = 'sal.json'
    app.run(debug=True)
