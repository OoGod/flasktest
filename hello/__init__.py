from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)
#app.secret_key = 'your_secret_key'  # CSRF 保护需要的密钥
app.secret_key = os.urandom(24)  # 生成一个随机的 24 字节密钥


from hello import views
