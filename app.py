## create a simple flask application
# Flask is the used to build web pages which are less 


from flask import Flask,redirect,url_for,render_template,request
# app.route is the decorater from the arugument it will direct the route or ways for the respective / back slash webpages.
# redirect, url_for are modules from flask package will get the total webpage 
# render_template - will also redirect to webpage but that webpage should be in the local folder with name templates (case sentive) 
# - otherwhy not found error pops up

app = Flask(__name__)

@app.route("/")  # route will assign differents urls
def home():
    return "Hello world!"

@app.route("/welcome")
def welcome():
    return "Welcome to the flask tutorial!"
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    return "this person has passed and the score is "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "this person has failed and the score is "+ str(score)

@app.route("/calculate",methods=["POST", "GET"])
def calculate():
    ### Get - whenever user is giving url, then method get
    ### Push - Whenever user is giving data or entering info in the webpage 
    if request.method == "GET": # request is import to state which method is requested whether push or get
        return render_template("calculate.html")
    else: 
        maths = float(request.form["maths"]) # request from gives the varaible values given by user 
        science = float(request.form["science"])
        history = float(request.form["history"])
    
        avg_marks= (maths+science+history)/3
        
        ### method 1: accessing HTML page: Using render_template which is resulted through other html page
        return render_template("result.html",results=avg_marks) # This is using the render_template --> which is used to call sent to html page
        
        ### method 2: accessing through route: Using redirect, url_for  
        """result="" 
        if avg_marks>=50:
            result="success"
        else:
            result="fail"
        return redirect(url_for(result, score=avg_marks))"""


## this is the entry point of the whole program
## flask related program is difined before main program to get loaded early, so it can't be included in the main body.

if __name__=="__main__": # (caling app for run and telling to this as starting point)
    app.run() # debug =  true ---> will restart the total app