import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API working.. </h1>'


@app.route('/predict',methods=['GET','POST'])
def predict():
    import joblib
    model = joblib.load('fire_prediction.ml')
    fireoutcome = model.predict([[int(request.args['Oxygen']),
                            int(request.args['Temperature']),
                            int(request.args['Humidity'])
                           ]])
    return str(round(fireoutcome[0],2))


if __name__ == "__main__":
    app.run(debug=True)