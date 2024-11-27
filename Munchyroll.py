from flask import Flask, render_template, request, redirect, url_for
from backend.Database.dbFunc import obtenir_connection, fermer_connection
from backend.Database.AdminDAO import AdminDAO
from backend.Database.MemberDAO import MemberDAO
from backend.Database.AnimeDAO import AnimeDAO
from backend.Class_Domain.User import User
from backend.Database.AnimeDAO import AnimeDAO
from backend.Database.EpisodeDAO import EpisodeDAO
from backend.Database.SeasonDAO import SeasonDAO
from backend.Database.CommentDAO import CommentDAO

app = Flask(__name__, template_folder='frontend', static_folder='frontend')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        conn = obtenir_connection()
        if AdminDAO.verifyAdmin(conn, name, password):
            fermer_connection(conn)
            return render_template('indexAdmin.html')
        elif MemberDAO.verifyMember(conn, name, password):
            logIn_member = MemberDAO.get_member_by_username(conn, name)
            fermer_connection(conn)
            print("Login member id : ", logIn_member.getMember_id())
            return render_template('index.html', logIn_member=logIn_member)
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard/<member_id>', methods=['GET', 'POST'])
def dashboard(member_id):
    conn = obtenir_connection()
    animeList = AnimeDAO.getAll_anime(conn)
    fermer_connection(conn)
    return render_template('Dashboard.html', member_id=member_id, animeList=animeList)

# @app.route('/favAnimes')
# def favAnimes():
#     return render_template('Animes.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('AboutUs.html')

@app.route('/animeList')
def animeList():
    conn = obtenir_connection()
    animes = AnimeDAO.getAll_anime(conn)
    fermer_connection(conn)
    return render_template('AnimeList.html', animes=animes)

@app.route('/addAnime', methods=['POST', 'GET'])
def add_anime():
    if request.method == 'POST':
        anime_name = request.form['anime_name']
        anime_desc = request.form['anime_description']
        anime_raiting = request.form['anime_raiting']
        anime_types = request.form['anime_types'].split(',')
        anime_image = request.form['anime_image']
        anime_release_date = request.form['anime_release_date']
        conn = obtenir_connection()
        AnimeDAO.add_anime(conn, anime_name, anime_desc, anime_raiting, anime_types, anime_image, anime_release_date)
        fermer_connection(conn)
        return redirect(url_for('animeList'))

@app.route('/deleteAnime/<anime_name>', methods=['POST'])
def delete_anime(anime_name):
    conn = obtenir_connection()
    AnimeDAO.delete_anime(conn, anime_name)
    fermer_connection(conn)
    return redirect(url_for('animeList'))

@app.route('/search_anime', methods=['GET'])
def search_anime():
    search = request.args.get('search-anime')
    conn = obtenir_connection()
    animes = AnimeDAO.search_anime(conn, search)
    fermer_connection(conn)
    return render_template('AnimeList.html', animes=animes)

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
    users = MemberDAO.searchMember(conn, search)
    fermer_connection(conn)
    return render_template('Users.html', users=users)

@app.route('/animePage/<anime_name>')
def animePage(anime_name):
    conn = obtenir_connection()
    anime = AnimeDAO.get_anime(conn, anime_name)
    fermer_connection(conn)
    return render_template('AnimePage.html', anime=anime)

@app.route('/addSeason/<anime_name>', methods=['POST', 'GET'])
def add_season(anime_name):
    if request.method == 'POST':
        season_name = request.form['season_name']
        season_release_date = request.form['season_release_date']
        conn = obtenir_connection()
        print(anime_name)
        SeasonDAO.add_season(conn, season_name, anime_name, season_release_date)
        fermer_connection(conn)
        return redirect(url_for('animePage', anime_name=anime_name))
    
@app.route('/addEpisode/<anime_name>', methods=['POST', 'GET'])
def add_episode( anime_name):
    if request.method == 'POST':
        conn = obtenir_connection()
        episode_name = request.form['episode_name']
        episode_reiting = 0.0
        episode_like = 0
        episode_dislike = 0
        episode_image = request.form['episode_image']
        episode_season_name = request.form['episode_season_name']
        episode_season_id = SeasonDAO.get_season_id_by_season_name_and_anime_name(conn, episode_season_name, anime_name)
        episode_release_date = request.form['episode_release_date']
        EpisodeDAO.add_episode(conn, episode_name, episode_reiting, episode_like, episode_dislike, episode_image, episode_season_id, episode_release_date)
        fermer_connection(conn)
        return redirect(url_for('animePage', anime_name=anime_name))
    
@app.route('/deleteSeason/<anime_name>', methods=['POST'])
def delete_season(anime_name):
    if request.method == 'POST':
        conn = obtenir_connection()
        season_name = request.form['season_name']
        season_id = SeasonDAO.get_season_id_by_season_name_and_anime_name(conn, season_name, anime_name)
        SeasonDAO.delete_season(conn, season_id)
        fermer_connection(conn)
    return redirect(url_for('animePage', anime_name=anime_name))

@app.route('/deleteEpisode/<anime_name>', methods=['POST'])
def delete_episode(anime_name):
    if request.method == 'POST':
        conn = obtenir_connection()
        episode_name = request.form['episode_name']
        episode_season_name = request.form['episode_season_name']
        episode_season_id = SeasonDAO.get_season_id_by_season_name_and_anime_name(conn, episode_season_name, anime_name)
        episode_id = EpisodeDAO.get_episode_id_by_episode_name_and_season_id(conn, episode_name, episode_season_id)
        EpisodeDAO.delete_episode(conn, episode_id)
        fermer_connection(conn)
    return redirect(url_for('animePage', anime_name=anime_name))
        

@app.route('/animePageMember/<anime_name>/<member_id>')
def animePageMember(anime_name, member_id):
    conn = obtenir_connection()
    anime = AnimeDAO.get_anime(conn, anime_name)
    fermer_connection(conn)
    return render_template('AnimePageMember.html', anime=anime, member_id=member_id)

@app.route('/episodePage/<episode_id>/<member_id>')
def episodePage(episode_id, member_id):
    conn = obtenir_connection()
    episode = EpisodeDAO.get_episode(conn, episode_id)
    season = SeasonDAO.get_season(conn, episode.getSeason_id())
    fermer_connection(conn)
    return render_template('Episodes.html', episode=episode, member_id=member_id,
                           season_name=season.season_name, anime_name=season.getAnime_name(),
                           getUsername=MemberDAO.get_member_username, getConn=obtenir_connection)
    
@app.route('/episodePageAdmin/<episode_id>')
def episodePageAdmin(episode_id):
    conn = obtenir_connection()
    episode = EpisodeDAO.get_episode(conn, episode_id)
    season = SeasonDAO.get_season(conn, episode.getSeason_id())
    fermer_connection(conn)
    return render_template('EpisodeAdmin.html', episode=episode, season_name=season.season_name,
                           anime_name=season.getAnime_name(), getUsername=MemberDAO.get_member_username,
                           getConn=obtenir_connection)
    
@app.route('/delete_comment/<comment_id>/<episode_id>', methods=['POST'])
def delete_comment(comment_id, episode_id):
    conn = obtenir_connection()
    CommentDAO.delete_comment(conn, comment_id)
    fermer_connection(conn)
    return redirect(url_for('episodePageAdmin', episode_id=episode_id))
    
@app.route('/add_comment/<episode_id>/<member_id>', methods=['POST', 'GET'])
def add_comment(episode_id, member_id):
    comment_content = request.form['comment']
    conn = obtenir_connection()
    CommentDAO.add_comment(conn, comment_content, member_id, episode_id, 0, 0)
    fermer_connection(conn)
    return redirect(url_for('episodePage', episode_id=episode_id, member_id=member_id))

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

@app.route('/favAnimes/<member_id>')
def favAnimes(member_id):
    print("Member_id de fav anime : ",member_id)
    conn = obtenir_connection()
    favAnimeName = MemberDAO.get_anime_list(conn, member_id)
    favAnime = []
    for name in favAnimeName:
        favAnime.append(AnimeDAO.get_anime(conn, name))
    fermer_connection(conn)
    return render_template('Animes.html', favAnime=favAnime, member_id=member_id)

@app.route('/deleteFavAnime/<member_id>/<anime_name>', methods=['POST'])
def deleteFavAnime(member_id, anime_name):
    conn = obtenir_connection()
    MemberDAO.delete_anime_to_member(conn, member_id, anime_name)
    fermer_connection(conn)
    return redirect(url_for('favAnimes', member_id=member_id))
    


if __name__ == '__main__':
    app.run(debug=True)