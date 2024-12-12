from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Initial content about Imran Khan
content = [
    "Imran Khan is a Pakistani politician and former cricketer who served as the 22nd Prime Minister of Pakistan.",
    "He founded the Pakistan Tehreek-e-Insaf (PTI), a centrist political party, and has been a prominent figure in Pakistani politics.",
    "Before entering politics, Khan was an internationally celebrated cricketer and led Pakistan to its first and only Cricket World Cup victory in 1992."
]

@app.route('/')
def index():
    return render_template('index.html', content=content)

@app.route('/add_blog', methods=['POST'])
def add_blog():
    new_blog = request.form.get('blog_content')
    if new_blog:
        content.append(new_blog)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5001)
