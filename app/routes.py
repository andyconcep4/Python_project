from app import app
from flask import render_template, request
from app.models import model, formopener, index
from app.models.index import getMeme, getPicture

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/pictures', methods =["GET", "POST"])
@app.route('/pictures.html', methods =["GET", "POST"])
def page2():
    if request.method == "POST":
        userdata = request.form.to_dict()
        # Get winning category
        winner=getMeme(userdata['question1'], userdata['question2'], userdata['question3'],userdata['question4'])
        # Get the winning image
        winner=getPicture(winner)
        
        return render_template('pictures.html', winner=winner)
        
    
    
    
    # send what person typed to model and get a return from the model
    
    # whatever we get from the model, send it to a template
    
    answer = model.firstResult()
    
    return "page2 goes here"
