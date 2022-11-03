import flask
 
import numpy as np
import pickle
 
model = pickle.load(open('model/fp1.pkl', 'rb'))
 
app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
 
 
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    # int_features = [int(x) for x in flask.request.form.values()]
    int_features = [int(x) for x in flask.request.form.values()]
    print(int_features, 'scnjnfrneduncnuvf') # [1, 2, 4] scnjnfrneduncnuvf
    final_features = [np.array(int_features)]
    print(final_features, 'scnjnfrneduncnuvf') # [array([1, 2, 4])] scnjnfrneduncnuvf
    prediction = model.predict(final_features)
    
    output = {0: 'not placed', 1: 'placed'}
    
    return flask.render_template('main.html', prediction_text='Transportation Prices :  ${:.2f}'.format(prediction[0]))
   
 
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
