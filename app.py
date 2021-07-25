from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Model
class Medication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medName = db.Column(db.String(100), nullable=False)
    medDose = db.Column(db.String(100), nullable=False)
    medRoute = db.Column(db.String(50), nullable=False)
    medFrequency = db.Column(db.String(50), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id




@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
       med_content = request.form['content']
       new_medication = Medication(Medication)
    try:
           db.session.add(new_medication)
           db.session.commit()
           return redirect('/')
    except:
            return "There was an error adding to the database"

    else:
            medications = Medications.query.order_by(Medication.date_created).all()
            return render_template('index.html', medications = medications)


if __name__ == ("__main__"):
    app.run(debug = True) #do not use true in development