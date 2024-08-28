#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Configuration class for Babel
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user_locale = g.get('user', {}).get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    tzname = request.args.get('timezone')
    if not tzname and g.user:
        tzname = g.user.get('timezone')
    try:
        return pytz.timezone(tzname).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    if user_id:
        g.user = users.get(int(user_id))
    else:
        g.user = None

@app.route('/')
def index():
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = format_datetime(current_time)
    return render_template('index.html', current_time=formatted_time)

if __name__ == "__main__":
    app.run(debug=True)

