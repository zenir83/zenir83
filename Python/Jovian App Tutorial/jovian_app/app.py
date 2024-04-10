from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm

app = Flask(__name__)

JOBS = [
    {'id' : 1,
     'title' : 'Data Analyst',
     'location' : ' Zevenhuizen, Zuid - Holland',
     'salaris' : '5000 euro per maand'
    },
    {'id' : 2,
     'title' : 'Medische analyst',
     'location' : 'Gouda, Zuid - Holland',
     'salaris' : '4000 euro per maand'
    },
    {'id' : 3,
     'title' : 'Junior C# developer',
     'location' : 'Brielle, Zuid - Holland',
     'salaris' : '3500 euro per maand'
    },
    {'id' : 4,
     'title' : 'Copywriter',
     'location' : 'Rotterdam, Zuid - Holland',
     'salaris' : '3000 euro per maand'
    },   
    {'id' : 5,
     'title' : 'Python programmer',
     'location' : 'Hybride',
     'salaris' : '4800 euro per maand'
    },
    {'id' : 6,
     'title' : 'Grafisch ontwerper',
     'location' : 'Hybride',
    },
    {'id' : 5,
     'title' : 'Python programmer',
     'location' : 'Rotterdam, hybride',
     'salaris' : '4800 euro per maand'
    }
] 

@app.route("/")
def home(): 
    return render_template('home.html', jobs = JOBS ,
                           company_name = 'Koningsoever')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__== "__main__":
    app.run(host='0.0.0.0', debug=True)

