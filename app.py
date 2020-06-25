from flask import Flask, render_template  # Render template thingie allows you to render html with urls

app = Flask(__name__) #  Creating a Flask object called app
@app.route('/')
def homepage_render():
    return render_template('index.html')


@app.route('/products')
@app.route('services')
def services_render():
    return render_template('services.html')


@app.route('/contact-info')
@app.route('/contact_info')
@app.route('/contact')
@app.route('/get_in_contact')
def contact_render():
    return render_template('contact_info.html')


@app.route('/questions_and_answers')
@app.route('/q_n_a')
def q_n_a_render():
    return render_template('q_n_a.html')


@app.route('/<error: str>')
@app.route('/<error: int>')
@app.route('/<error: float>')
def page_not_found_render():
    return render_template('404_error.html')
