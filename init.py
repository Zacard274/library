from flask import Flask
import config
from controller.books import books_bp
from controller.user import user_bp
from controller.book_type import book_type_db
from controller.city import city_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(book_type_db, url_prefix='/book_type')
app.register_blueprint(city_bp, url_prefix='/city')


if __name__ == '__main__':
    app.run()