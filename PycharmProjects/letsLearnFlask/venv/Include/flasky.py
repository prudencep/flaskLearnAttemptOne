from flask import Flask


app = Flask(__name__)#to let your application be sure sure of the name being called



@app.route('/')#a random page on website called home
def home():
    return "This is just the home page"#will return this whenever the app is run, not sure how yet but lets go



if __name__ == "__main__":#idek snxvhbjx
    app.run(debug = True)#the app should run
