from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def welcome():
    return render_template("index.html")
    
@app.route('/quiz1')
def quiz1():
    return render_template("quiz1.html")

@app.route('/quiz2')
def quiz2():
    return render_template("quiz2.html")
    
@app.route("/article")
def article():
    return render_template("article.html")

    
@app.route('/results1', methods=['GET','POST'])
def results1():
    if request.method=='GET':
        return "Please answer all questions!"
    else:
        #this is where to open the form, access items, process
        userdata = formopener.dict_from(request.form)
        print(userdata)
        quizresults = model.quiz1results(userdata["frequency"], userdata["will"])
        print(quizresults)
        level = quizresults[0]
        genexp = quizresults[1]
        frequ = quizresults[2]
        selfwww = quizresults[3]
        imageimage = quizresults[4]
        return render_template('results1.html', level = level, genexp = genexp, frequ = frequ, selfwww = selfwww, imageimage = imageimage)
    