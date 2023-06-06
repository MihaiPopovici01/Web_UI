from flask import Blueprint, render_template, flash, request, redirect, url_for, json, session
import requests


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

# @views.route('/add-disciplina', methods=['GET','POST'])
# def addDisciplina():

#     profesori = InfoProfessor.query.order_by(InfoProfessor.id).all()

#     if(request.method == 'POST'):
#         name = request.form.get('nume')
#         prof_curs_id = request.form.get('profesor_curs')
#         prof_lab_id = request.form.get('profesor_lab')

#         new_dis = Disciplina(nume = name, prof_curs_id = prof_curs_id, prof_lab_id = prof_lab_id, an = 1 )
#         db.session.add(new_dis)
#         db.session.commit()
        
#         flash("Disciplina a fost adaugata cu succes", category='success')

    

#     return render_template("addDisciplina.html", user= current_user, profesori = profesori )


# @views.route('/info')
# def info():

#     student = InfoStudent.query.filter_by(id_student=current_user.id).first()

#     return render_template("studentInfo.html", user= current_user, student = student)

# @views.route('/materii-prof')
# def materii_prof():
#     user = InfoProfessor.query.filter_by(id_prof=current_user.id).first()
#     list = Disciplina.query.filter_by(prof_curs_id = user.id).order_by(Disciplina.id).all()
#     list1 = Disciplina.query.filter_by(prof_lab_id = user.id).order_by(Disciplina.id).all()
#     return render_template("materiiProf.html", user= current_user, materii1 = list, materii2 =list1 )


@views.route('/materii')
def materii():
    req = requests.get('http://api.local:8888/disciplines')
    data = req.json()
    return render_template("materii.html", data=data)

# @views.route('/alege-disciplina', methods=['GET','POST'])
# def alegeDisciplina():
#     user = InfoStudent.query.filter_by(id_student=current_user.id).first()
#     list = Disciplina.query.filter_by(an = user.an).order_by(Disciplina.id).all()

#     if(request.method == 'POST'):
#         disciplina_id = request.form.get('disciplina')
#         disciplina_stud = InfoDisciplina.query.filter_by(student_id=current_user.id, disciplina_id = disciplina_id).first()

#         disciplina= json.dumps(disciplina_stud)
#         session['disciplina'] = disciplina

#         return redirect(url_for('views.materieInfo', disciplina = disciplina))

    

#     return render_template("alegeMaterie.html", user= current_user, discipline = list )

# @views.route('/materie-info', methods=['GET'])
# def materieInfo():

#     disciplina = session['disciplina']
#     return render_template("materieInfo.html", user= current_user,  disciplina = json.loads(disciplina))