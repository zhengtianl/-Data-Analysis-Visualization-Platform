from flask import Flask, jsonify

app = Flask(__name__)

# define API endpoint
@app.route('/api/data')
def get_data():
  data = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com'
  }
  return jsonify(data)

# start server
if __name__ == '__main__':
  app.run(debug=True)
  
  


