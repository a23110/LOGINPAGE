# Hosting the demo login page for free

## Option A: Replit
1. Go to replit.com and create a new **Python** Repl.
2. Upload `app.py` and `requirements.txt` (or paste their contents into new files with those names).
3. Open the Replit shell and run: `pip install -r requirements.txt`
4. Click **Run**. Replit will give you a public URL like
   `https://your-repl-name.your-username.repl.co`
5. Your login form is at that URL, and the POST endpoint your brute-force
   script should target is `https://your-repl-name.your-username.repl.co/login`.

Note: Replit's free tier may put the app to sleep when idle — visit the URL
once in a browser to wake it up before running your script.

## Option B: PythonAnywhere
1. Create a free account at pythonanywhere.com.
2. Go to the **Files** tab and upload `app.py`.
3. Go to the **Web** tab, click **Add a new web app**, choose **Flask**,
   and point it at your `app.py` (the wizard walks you through this).
4. Reload the web app. Your site will be live at
   `https://your-username.pythonanywhere.com`
5. The login endpoint for your script will be
   `https://your-username.pythonanywhere.com/login`

## Either way
Once it's live, plug the `/login` URL into the `URL` variable in
`brute_force.py` and run the script from your own machine.
