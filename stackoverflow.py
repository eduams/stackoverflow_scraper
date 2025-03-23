import requests
from bs4 import BeautifulSoup
import json
import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    data_hora TEXT,
    url TEXT,
    usuario TEXT,
    titulo TEXT,
    likes INTEGER,
    comentarios INTEGER,
    tags TEXT
)
""")

res = requests.get("https://stackoverflow.com/questions/")
soup = BeautifulSoup(res.text,"html.parser")
questions = soup.select(selector=".s-post-summary")
dados_posts = []

for x in questions:
    post = {
        "data_hora": x.select(".s-user-card--time span")[0]["title"],
        "url": x.select(".s-link")[0]['href'],
        "usuario": x.select(".s-user-card--link")[0].text.strip(),
        "titulo": x.select(".s-post-summary--content-title")[0].text.strip(),
        "likes": int(x.select(".s-post-summary--stats-item")[0].text.split()[0]),
        "comentarios": int(x.select(".s-post-summary--stats-item")[1].text.split()[0]),
        "tags": [tag.text.strip() for tag in x.select(".s-post-summary--meta-tags .s-tag")]
    }
    dados_posts.append(post)

for item in dados_posts:
    cursor.execute('''
        INSERT INTO posts (data_hora, url, usuario, titulo, likes, comentarios, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        item['data_hora'],
        item['url'],
        item['usuario'],
        item['titulo'],
        item['likes'],
        item['comentarios'],
        json.dumps(item['tags'])
    ))

conexao.commit()
conexao.close()

def get_all_data():
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM posts')
    rows = cursor.fetchall()
    conexao.close()
    for row in rows:
        print(row)
    return

def get_users():
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT usuario FROM posts')
    rows = cursor.fetchall()
    conexao.close()
    for row in rows:
        print(row[0])
    return

def get_posts_more_5_likes():
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    cursor.execute('SELECT titulo, usuario, likes FROM posts WHERE likes < 0')
    rows = cursor.fetchall()
    conexao.close()
    for row in rows:
        print("Título do post: ", end="")
        print(row[0])
        print("Usuário: ", end="")
        print(row[1])
        print("Likes: ", end="")
        print(row[2])

    return

print("Escolha uma das consultas abaixo:")
selection = int(input("1 - Todos os dados | 2 - Apenas os usuários | 3 - Posts com likes negativos: "))
if selection == 1:
    get_all_data()
elif selection == 2:
    get_users()
elif selection == 3:
    get_posts_more_5_likes()