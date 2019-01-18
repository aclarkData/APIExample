from flask import Flask,request,jsonify,Response,render_template
from functools import wraps
import numpy as np

app = Flask(__name__)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'block' and password == 'science'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def squared(number):
    '''Function to square a number. Could be a complicated ML model'''
    squared = np.square(number)
    return squared

@app.route("/")
@requires_auth
def index():
    return render_template('index.html')

@app.route("/health")
def health():
    return 'Healthy'

@app.route('/result', methods=['POST'])
@requires_auth
def result():
    '''
    Route for UI
    '''
    try:
        # Get the data from the index page
        number=request.form['number']
        number = float(number)
        print(number)

        # call functionResultAPI
        Result = squared(number)

        return render_template('result.html', Result=Result)

    except:
        render_template('error.html')

@app.route('/square', methods=['POST'])
@requires_auth
def squareAPI():
    '''
    Example API call:
        Curl:

        curl -X POST -H "Content-Type: application/json"  -u "block:science*" -d '{
        "number": ".5"
        }' http://localhost:8000/square


        Python:
        import requests

        headers = {
            'Content-Type': 'application/json',
            }

        data = '{"number": "5"}'

        response = requests.post('http://localhost:80/square', headers=headers,squareAPI data=data,auth=('block', 'science'))
        response.json()[0]['Result']

    '''

    try:
        # Get the data from the upload
        number = request.get_json()['number']
        number = float(number)
        # call function
        Result = squared(number)

        Result = [{'Result':Result}]
        print(Result)
        return jsonify(Result)

    except:
        return jsonify([{'Result':'Oops, something happened. Please try again'}])


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 404

@app.errorhandler(405)
def page_not_found2(e):
    # note that we set the 405 status explicitly
    return render_template('error.html'), 405

@app.errorhandler(500)
def page_not_found3(e):
    # note that we set the 500 status explicitly
    return render_template('error.html'), 500

if __name__ == "__main__":
     app.run(host='localhost', port=8000,debug=True)
