from flask import Flask, render_template  # Render template thingie allows you to render html with urls

app = Flask(__name__) #  Creating a Flask object called app or our localhost server
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


error = [
    {

    }
]

#  404 errors handler
@app.errorhandler('404')
def not_found_render(e):
    return render_template('not_found_error.html')
    error.append({404: 404})