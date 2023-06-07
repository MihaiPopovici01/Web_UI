from flask import Blueprint, render_template, flash, request, redirect, url_for, json, session
import requests


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/add-disciplina', methods=['GET','POST'])
def addDisciplina():

    if(request.method == 'POST'):
        dictToSend= {
            'Name' : request.form.get('nume'),
            'Prof_Name' : request.form.get('nume_prof'),
            'Room' : request.form.get('sala'),
            'Cours_Start_Hour' : request.form.get('ora_inceperii'),
            'Year' : request.form.get('anul'),
            'Semester' : request.form.get('semestrul')
        }
        res = requests.post('http://api.local:8888/disciplines/add', json=dictToSend)

        flash("Disciplina a fost adaugata cu succes", category='success')

    return render_template("addDisciplina.html")

@views.route('/update-disciplina/<disciplina_id>', methods=['GET','POST'])
def updateDisciplina(disciplina_id):

    url = "http://api.local:8888/disciplines/" + str(disciplina_id)
    req = requests.get(url)
    data = req.json()

    if(request.method == 'POST'):

        if request.form.get('delete') == 'DELETE':
            res = requests.delete(url)

        
        dictToSend= {
            'Name' : request.form.get('nume'),
            'Prof_Name' : request.form.get('nume_prof'),
            'Room' : request.form.get('sala'),
            'Cours_Start_Hour' : request.form.get('ora_inceperii'),
            'Year' : request.form.get('anul'),
            'Semester' : request.form.get('semestrul')
        }
        url = "http://api.local:8888/disciplines/" +  str(disciplina_id)
        res = requests.put(url, json=dictToSend)

        flash("Disciplina a fost modificata cu succes", category='success')

    return render_template("updateDisciplina.html", data=data)

@views.route('/events')
def events():
    req = requests.get('http://api.local:8888/events')
    data = req.json()
    return render_template("events.html",  events=data)

@views.route('/materii')
def materii():
    req = requests.get('http://api.local:8888/disciplines')
    data = req.json()
    return render_template("materii.html", data=data)

@views.route('/study_groups')
def study_groups():
    req = requests.get('http://api.local:8888/study_groups')
    data = req.json()
    return render_template("studyGroups.html",  data=data)


@views.route('/users')
def users():
    req = requests.get('http://api.local:8888/users')
    data = req.json()
    return render_template("users.html", users=data)