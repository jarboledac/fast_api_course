from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con FastApi" #Title in docs
app.version = "0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': 'En un exuberante planeta...',
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': 'En un exuberante planeta...',
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]

@app.get('/', tags=['home']) #Tags change method title in docs
def message():
    return HTMLResponse('<h1> Hello World! </h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies
    
@app.get('/movies/{id}', tags=['movies'])
def get_movies(id: int):
    for item in movies:
        if item[id] == id:
            return item
        else:
            return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]
     
