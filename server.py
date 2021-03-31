import flask 
import jinja2
import crud
from model import connect_to_db


app = Flask(__name__)
app.secret_key = "SecretKey"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage"""
    return render_template('homepage.html')

@app.route('/about')
def index():
    """take me to about page. project details"""
    return render_template('about.html')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)