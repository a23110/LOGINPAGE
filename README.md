# LOGINPAGE

This project contains a simple Flask demo login page and a brute-force tester for the demo app.

## Live Render site

https://loginpage-c75v.onrender.com/

## Login endpoint

https://loginpage-c75v.onrender.com/login

## Run the brute-force script on Windows CMD

From the project folder:

```cmd
cd /d "PATH_TO_YOUR_PROJECT_FOLDER"
set LOGIN_URL=https://loginpage-c75v.onrender.com/login
python brute_force.py
```

If Python is not recognized, use the full path:

```cmd
cd /d "PATH_TO_YOUR_PROJECT_FOLDER"
set LOGIN_URL=https://loginpage-c75v.onrender.com/login
"C:\Users\YourUser\AppData\Local\Programs\Python\Python311\python.exe" brute_force.py
```

## One-line version

```cmd
cd /d "PATH_TO_YOUR_PROJECT_FOLDER" && set LOGIN_URL=https://loginpage-c75v.onrender.com/login && python brute_force.py
```

## Manual test

You can also test the site directly:

```cmd
curl -X POST "https://loginpage-c75v.onrender.com/login" -d "password=729"
```

This demo is intentionally vulnerable and meant only for educational use against a site you own or are authorized to test.
