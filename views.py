from todoapp import app

@app.route('/')
def home():
    return '<h1>servidor up!</h1>'