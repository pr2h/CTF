# Welcome function
def hujambo():
    # Release Date : 23 May 2024
    print '''
##################################################
# Tool    : Secretive Secrets (CTF)              #
# Version : 1.0                                  #
# Profile : https://github.com/pr2h/             #
# Coded with Python 3                            #
##################################################
    '''
    
from flask import Flask, render_template, request
from waitress import serve
 
app = Flask(__name__) 

@app.route('/', methods=['GET'])
def home():         
    return render_template('index.html')

@app.route('/damnsecretfolderdontopen', methods=['GET']) 
def damnsecretfolderdontopen():
    return render_template('secretestfile')

@app.route('/companysecrets', methods=['GET', 'POST'])
def companysecrets():
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            return('Invalid username')
        elif request.form['password'] != 'qwerty':
            return('Invalid password')
        else:
            return('Critical Folder Name First Half : ZGFtbnNlY3JldG')
           
    return render_template('login.html')

@app.route('/robots.txt', methods=['GET']) 
def robots(): 
    return('User-agent: *<br>Disallow: /companysecrets')

@app.route('/admin', methods=['GET']) 
def admin():
    return('NOTE to developer: Delete the hundred subdirectories (1, 2 and so on) while moving to prod!')

@app.route('/admin/<int:number>', methods=['GET']) 
def admin_subfolders(number):
    if number == 56:
        return('Critical Folder Name Second Half : ZvbGRlcmRvbnRvcGVu')
    else:
        return('This is a test file')

if __name__ == '__main__': 
    #app.run(host='0.0.0.0', port=80)
    serve(app, host='0.0.0.0', port=8578, threads=100)
