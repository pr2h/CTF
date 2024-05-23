# Secretive Secrets (CTF)

# Program made with Python 3 by pr2h

# For person conducting the CTF:</b>

1. Download the files from github.
2. Make sure you have Python 3
3. Install required libraries:<br>
pip3 install flask<br>
pip3 install waitress
4. Run the program:
python3 server.py

# For people trying to solve the CTF, following is the procedure (psst... don't see before solving it, or check only if you are struck):

1. Run nmap on the server where the CTF is hosted:
nmap -Pn -n --open -p- <hostname/IP of server> -oN tcp.txt

Find that the server is running on 8578 with nmap using above command.

2. See the souce code of index page and identify the comment:
<!-- comments: Yet to do, create an 'admin' dir and protect it since it is critical -->

This means admin folder is critical. It says it hasn't been created. But let's see.

Going forward I am assuming server is hosted on 10.10.10.100

3. Browse to 'http://10.10.10.100:8578/admin' and find the note:

NOTE to developer: Delete the hundred subdirectories (1, 2 and so on) while moving to prod!

4. There seem to be hundred directories. Let's try with some sample values:
http://10.10.10.100:8578/admin/random (Page is not found)
http://10.10.10.100:8578/admin/1 (There is some page)

Run Intruder with '1' as variable in above URL. Payloads will be 1 to 100, since the previous page says there are 100 subdirectories.

5. Observe that the length of http://10.10.10.100:8578/admin/56 is different from others.

6. Open it! We get:

Critical Folder Name Second Half : ZvbGRlcmRvbnRvcGVu

7. Great! Time to find the 1st half. Goto http://10.10.10.100:8578/robots.txt and find:

User-agent: *
Disallow: /companysecrets

8. Goto http://10.10.10.100:8578/companysecrets, there seems to be a login

9. Try random username and password.

10. You get Invalid username. So application has username enumeration

11. Keep trying various usernames. Ultimately, 'admin' will work, it is very common username and considering this page is /admin, haha.

12. Next brute force the password with Intruder, password is a common password qwerty. After finding it, login and get:

Critical Folder Name First Half : ZGFtbnNlY3JldG

13. Now, let's combine the strings to get the full folder name:

ZGFtbnNlY3JldGZvbGRlcmRvbnRvcGVu

14. This is clearly a base64 encoded string, which decodes to :
damnsecretfolderdontopen

15. Goto http://10.10.10.100:8578/damnsecretfolderdontopen and capture the flag
