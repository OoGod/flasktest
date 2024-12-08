from hello import app
from hello.forms import MyForm
from flask import Flask, render_template, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # 处理表单数据
        name = form.name.data
        return redirect(url_for('success', name=name))
    return render_template('index.html', form=form)

@app.route('/success/<name>')
def success(name):
    return f'Hello, {name}!'