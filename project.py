from flask import Flask, jsonify, request;

app = Flask(__name__)

data = [
    {
        'Name':'Pastoral Law',
        'Contact No.':'9867530000',
        'ID':1
    },
    {
        'Name':'Handsome Bonus',
        'Contact No.':'9867767766',
        'ID':2
    },
    {
        'Name':'Exclusive Ear',
        'Contact No.':'9876546578',
        'ID':3
    },
]

@app.route('/')
def main_boy():
    return 'I am a main page.'

@app.route('/add-contact', methods=['POST'])
def adddata():
    if not request.json:
        return jsonify({
            'status':'error',
            'message': 'what do you think you are doing?'
        },400)
    new_data={
        'Name':request.json.get('name'),
        'Contact No.':request.json.get('contact'),
        'ID':request.json.get('id')      
    }
    data.append(new_data)
    return jsonify({
        'status':'OK',
        'message':'Task Added'
    })

@app.route('/get-persons')
def data_seeing():
    return jsonify({
        'data': data
    })

if (__name__ == '__main__'):
    app.run(debug='True')

