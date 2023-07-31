from flask import Flask, jsonify, request
import tensorflow
from tensorflow.keras.models import load_model
import numpy as np 

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def return_text():

    model2 = load_model('model2/')

    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    num3 = float(request.args.get('num3', 0))
    num4 = float(request.args.get('num4', 0))
    num5 = float(request.args.get('num5', 0))

    arr = np.array([num1,num2,num3,num4,num5])
    array = np.reshape(arr,(1,5,1,1))
    #array = np.array([[[[num1]], [[num2]], [[num3]], [[num4]], [[num5]]]])
    
    num_predict = model2.predict(array).flatten()

    result = {
        'prediction': str(num_predict[0])
    }
    
    # result = {
    #     'num1': num1,
    #     'num2': num2,
    #     'num3': num3,
    #     'num4': num4,
    #     'num5': num5
    # }
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)  # Change the port if needed