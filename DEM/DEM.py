# Welcome function
def hujambo():
    # Release Date : 16 July 2018
    print '''
##################################################
# Tool    : DEM CTF                              #
# Version : 1.0                                  #
# Profile : https://github.com/pr2h/             #
# Coded with Python 2.7                          #
##################################################
    '''

from flask import Flask, abort, request
import subprocess

app = Flask(__name__)
app.url_map.strict_slashes = False

'''
# Whitelist the public ip(s)
@app.before_request
def limit_remote_addr():
    if request.remote_addr != 'x.x.x.x':
        abort(403)
'''

text = '''<html><b>Directories:</b><br>1. VEdrMGRVbEROR2RNVXpSMFRHbEJkVXhUTkdkTWFVRjA=</br><br>2. VkVkcmQyUkZlSEJSV0ZaTlZYcFNibFJIYXpCa1JYaFVUVWRrVFdGVVVqRlVSMnhDWkZWNFZFNUhaRTFoVlVZd1ZFWk9RbVJWYkVSTlNGSktVWHBDTVZSSGF6QmFNSGh3VVZoV1RWVjZVbTVVUms1Q1pGVjRjRTVJVmtwUmVsSnVWRVpOTUZvd2VIQk5SMlJOVlhwQ2JsUkhZemxRVVQwOQ==</br></html>'''
with open('dirinfo.txt','w') as f:
    f.write(text)
    f.flush()
f.close()

@app.route('/')
def hello():
    return 'Believe me! there is no page called "/secret"'

@app.route('/secret')
def secret():
    return "I don't have any subfolders.. Don't enumerate me further. I warn you!"

@app.route('/pr2hrememberthename')
def pr2hrememberthename():
    return "Yes! You have cracked it.. The world is yours!! Flag = iamhacker1"

@app.route('/secret/<id>')
def secretid(id):
    out=''
    command = ''
    
    if 'script' in id:
        out = "NO script TAGS ALLOWED! DON'T BE MALICIOUS!"

    elif 'cat' in id and 'DEPM' in id:
        out = 'HAHAHA!! YOU CANNOT SEE THE SOURCE CODE'

    elif 'type' in id and 'DEPM' in id:
        out = 'HAHAHA!! YOU CANNOT SEE THE SOURCE CODE'

    elif 'cat *.*' in id or ';' in id or 'type *.*' in id:
        out = 'COMMAND ACCESS DENIED'

    if out!='':
        return('Output :: '+out)

    blacklisted_commands = ['passwd','ifconfig','ipconfig','whoami','hostname','echo','powershell','python','vi','nano','mv','move','cp','copy','man',
                            'mkdir','rm','rmdir','touch','locate','clear','cls','reset','cd','telnet','ssh','ping','php','ftp','tracert','netstat','pathping',
                            'route','arp','nslookup','nbtstat','netsh','getmac']
    allowed_commands = ['ls','cat dirinfo.txt','dir','type dirinfo.txt']

    for command in blacklisted_commands:
        if command == id or command == id.split(' ')[0]:
            out = 'COMMAND ACCESS DENIED'
            return('Output :: '+out)
                
    for command in allowed_commands:
        if command == id:
            out = subprocess.Popen(id, shell=True, stdout=subprocess.PIPE).stdout.read()

    if out == '':
        out = id

    return('Output :: '+out)

app.run(host = '0.0.0.0', port=8080)
