from flask import Flask


app = Flask(__name__)#to let your application be sure sure of the name being called


# @ is called a decorator, reconnects a url to the return value of a funtion
@app.route('/')#a random page on website called home
def home():
    return "This is just the home page"#will return this whenever the app is run, not sure how yet but lets go

@app.route('/mino')
def mino():
    return '<h1>Song Mino is the love of my life.</h1>'

@app.route('/faves/<myFaves>')#how to create a variable
def faves(myFaves):
    return '<h1>One of my faves is %s</h1>' % myFaves

@app.route('/favesAge/<int: myFavesAge>')#how to create an integer variable. You have to do this for ints but not for other data types
def favesAge(myFavesAge):#functions don't have to be the same name
    return '<h1>His age is %s</h1>' % myFavesAge



if __name__ == "__main__":#idek snxvhbjx
    app.run(debug = True)#the app should run
