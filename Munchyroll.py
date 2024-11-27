from flask import Flask, render_template, request, redirect, url_for
from backend.Database.dbFunc import obtenir_connection, fermer_connection
from backend.Database.AdminDAO import AdminDAO
from backend.Database.MemberDAO import MemberDAO
from backend.Class_Domain.User import User

app = Flask(__name__, template_folder='frontend', static_folder='frontend')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if AdminDAO.verifyAdmin(obtenir_connection(), name, password):
            return render_template('indexAdmin.html')
        elif MemberDAO.verifyMember(obtenir_connection(), name, password):
            return render_template('index.html')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')

@app.route('/favAnimes')
def favAnimes():
    return render_template('Animes.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('AboutUs.html')

@app.route('/animeList')
def animeList():
    return render_template('AnimeList.html')

@app.route('/UserList')
def userList():
    conn = obtenir_connection()
    users = MemberDAO.getAll_Members(conn)
    fermer_connection(conn)
    return render_template('Users.html', users=users)

@app.route('/deleteUser/<member_id>', methods=['POST'])
def delete_user(member_id):
    conn = obtenir_connection()
    MemberDAO.delete_member(conn, member_id)
    fermer_connection(conn)
    return redirect(url_for('userList'))

@app.route('/search_user', methods=['GET'])
def search_user():
    search = request.args.get('search-user')
    conn = obtenir_connection()
    users = MemberDAO.getAll_Members(conn)
    listtosend = []
    fermer_connection(conn)
    for user in users:
        if user.username.lower().startswith(search.lower()):
            listtosend.append(user)
    return render_template('Users.html', users=listtosend)

@app.route('/animePage')
def animePage():
    return render_template('AnimePage.html')

@app.route('/episodePage')
def episodePage():
    return render_template('Episodes.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        confirmPasword = request.form['confirm-password']
        if password == confirmPasword:
            conn = obtenir_connection()
            if MemberDAO.add_member(conn, name, User.get_hash_password(password)):
                fermer_connection(conn)
                return render_template('login.html')
            else:
                return render_template('Register.html', error = 'User already exists')
        else:
            return render_template('Register.html', error = 'Passwords do not match')
    return render_template('Register.html')  
    


if __name__ == '__main__':
    app.run(debug=True)