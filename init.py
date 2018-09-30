from flask import Flask
import config
from controller.books import books_bp
from controller.user import user_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(books_bp, url_prefix='/books')

app.register_blueprint(user_bp, url_prefix='/user')


if __name__ == '__main__':
    app.run()

