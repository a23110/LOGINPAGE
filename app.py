"""
Simple deliberately-weak login demo for brute-force practice.
DO NOT use a hardcoded password like this in any real application.
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded 3-digit "password" — intentionally weak, for demo purposes only.
# Chosen to stay in the 450-850 range for this demo.
CORRECT_PASSWORD = "729"

PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Demo Login</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    :root {
      --bg-start: #0f172a;
      --bg-end: #1e293b;
      --panel: rgba(15, 23, 42, 0.72);
      --panel-border: rgba(148, 163, 184, 0.2);
      --text: #e2e8f0;
      --muted: #cbd5e1;
      --input-bg: rgba(15, 23, 42, 0.75);
      --input-border: rgba(96, 165, 250, 0.45);
      --primary: #38bdf8;
      --primary-dark: #0284c7;
      --success: #34d399;
      --error: #f87171;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, var(--bg-start), var(--bg-end));
      color: var(--text);
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      letter-spacing: 0.01em;
    }

    .login-card {
      width: min(92vw, 380px);
      background: var(--panel);
      border: 1px solid var(--panel-border);
      box-shadow: 0 20px 45px rgba(15, 23, 42, 0.45);
      border-radius: 18px;
      padding: 30px 28px 24px;
      backdrop-filter: blur(8px);
    }

    h2 {
      margin: 0 0 22px;
      text-align: center;
      font-weight: 700;
      font-size: 2rem;
      letter-spacing: 0.04em;
    }

    form {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    input {
      width: 100%;
      padding: 14px 14px;
      border-radius: 10px;
      border: 1px solid var(--input-border);
      background: var(--input-bg);
      color: var(--text);
      font-size: 1rem;
      outline: none;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    input::placeholder {
      color: var(--muted);
      opacity: 0.8;
    }

    input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.18);
    }

    button {
      border: none;
      border-radius: 10px;
      padding: 12px 16px;
      background: linear-gradient(135deg, var(--primary), var(--primary-dark));
      color: white;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      box-shadow: 0 10px 20px rgba(2, 132, 199, 0.3);
    }

    button:hover {
      transform: translateY(-1px);
      box-shadow: 0 14px 26px rgba(2, 132, 199, 0.35);
    }

    .message {
      margin-top: 18px;
      text-align: center;
      font-weight: 600;
      font-size: 0.98rem;
      padding: 10px 12px;
      border-radius: 10px;
      background: rgba(15, 23, 42, 0.78);
      border: 1px solid rgba(148, 163, 184, 0.16);
    }

    .message.success {
      color: var(--success);
      border-color: rgba(52, 211, 153, 0.35);
    }

    .message.error {
      color: var(--error);
      border-color: rgba(248, 113, 113, 0.35);
    }
  </style>
</head>
<body>
  <div class="login-card">
    <h2>Demo Login</h2>
    <form method="POST" action="/login">
      <input type="text" name="password" maxlength="3" placeholder="3-digit password" autocomplete="off">
      <button type="submit">Login</button>
    </form>
    {% if message %}
      <p class="message {% if 'successful' in message.lower() %}success{% else %}error{% endif %}">
        <strong>{{ message }}</strong>
      </p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    response = app.make_response(render_template_string(PAGE, message=None))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password", "")
    if password == CORRECT_PASSWORD:
        response = app.make_response(render_template_string(PAGE, message="Login successful!"))
    else:
        response = app.make_response(render_template_string(PAGE, message="Login failed."))
    response.status_code = 200 if password == CORRECT_PASSWORD else 401
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
