import json
import requests
import os
os.system('pip install cherrypy')
import cherrypy

class Sin:
    @cherrypy.expose
    def index(self):
        return self.html()

    def html(self):
        return """
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <title>palestine robot</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #000;
                    color: #0f0;
                    text-align: center;
                    padding: 50px;
                    animation: fadeIn 2s ease-in-out;
                }
                h1 {
                    color: #0ff;
                    text-shadow: 2px 2px 10px #00f;
                    animation: glow 1.5s infinite alternate;
                }
                input[type="text"], input[type="submit"] {
                    padding: 10px;
                    margin: 10px;
                    border: 1px solid #0f0;
                    border-radius: 5px;
                    background: #111;
                    color: #0f0;
                    transition: 0.3s;
                }
                input[type="text"]:focus, input[type="submit"]:hover {
                    background: #222;
                    box-shadow: 0 0 10px #0f0;
                }
                a {
                    color: #0ff;
                    text-decoration: none;
                    transition: color 0.3s;
                }
                a:hover {
                    color: #fff;
                }
                .result-container {
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #222;
                    border-radius: 10px;
                    border: 1px solid #0f0;
                    color: #fff;
                    max-width: 80%;
                    margin-left: auto;
                    margin-right: auto;
                    display: none;
                }
                @keyframes glow {
                    from {
                        text-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 20px #0ff;
                    }
                    to {
                        text-shadow: 0 0 20px #0ff, 0 0 30px #0ff, 0 0 40px #0ff;
                    }
                }
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                    }
                    to {
                        opacity: 1;
                    }
                }
            </style>
        </head>
        <body>
        <center>
        <hr>
        <mark><a href="https://t.me/omegpt">ذكاء اصطناعي خاص بدولة فلسطين</a></mark>
        <hr>
            <h1>اسأل اي سؤال في بالك عن فلسطين ؟</h1>
            <form method="post" action="send">
                <input type="text" name="email" placeholder="اكتب سؤالك هنا" required>
                <input type="submit" value="ارسال إلى الروبوت">
            </form>
            <div id="result-container" class="result-container">
                <p id="result-text"></p>
            </div>
        </center>         
        </body
