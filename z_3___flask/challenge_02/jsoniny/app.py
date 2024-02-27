from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
    data = {'result':'success', 'data': {"feed1":"data", "feed2":"data2"}}
    return data

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    # return jsonify({'result':'success', 'data': {"feed1":"data"}})
    return jsonify({'result':'success', 'data': {"feed1":"data"}})

@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    print(name, age)
    return jsonify({'result':'success'})