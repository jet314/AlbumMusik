from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/album/<int:album_id>')
def album(album_id):
    # Sebagai contoh, kita buat album dengan ID
    albums = {
        1: {'title': 'Album 1', 'description': 'Deskripsi Album 1', 'tracks': ['Lagu 1', 'Lagu 2', 'Lagu 3']},
        2: {'title': 'Album 2', 'description': 'Deskripsi Album 2', 'tracks': ['Lagu 4', 'Lagu 5', 'Lagu 6']},
    }
    album = albums.get(album_id, None)
    if album:
        return render_template('album.html', album=album)
    else:
        return "Album tidak ditemukan", 404

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
