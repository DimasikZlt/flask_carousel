from flask import Flask, render_template

app = Flask(__name__)


@app.route('/carousel')
def index():
    images = (
        'mars1.jpg',
        'mars2.jpg',
        'mars3.jpg',
        'mars4.jpg',
        'mars5.jpg',
        'mars6.jpg',
    )
    return render_template('carousel.html', title='Пейзажи Марса', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
