# Flask Internationalization and Localization

## Project Overview

This project demonstrates the implementation of internationalization (i18n) and localization (l10n) in a Flask web application using Flask-Babel. The application allows users to view content in different languages and formats based on their locale and preferences.

## Requirements

- **Operating System:** Ubuntu 18.04 LTS
- **Python Version:** Python 3.7
- **Pycodestyle:** Code should adhere to pycodestyle (version 2.5)
- **Flask:** A micro web framework used to build this application.
- **Flask-Babel:** A Flask extension for i18n and l10n support.
- **Pytz:** A module for working with time zones.
- All Python files should be executable and start with `#!/usr/bin/env python3`.

## Project Structure

- `0-app.py`: Basic Flask app with a single route `/`.
- `1-app.py`: Flask app with basic Babel setup, configuring English and French as available languages.
- `2-app.py`: Implements locale selection based on the request headers.
- `3-app.py`: Adds translation support in templates using Flask-Babel and message catalogs.
- `4-app.py`: Implements locale switching using URL parameters.
- `5-app.py`: Mocks a user login system to display user-specific locale settings.
- `6-app.py`: Prioritizes locale selection based on user settings.
- `7-app.py`: Infers and sets the correct timezone for the user.
- `8-app.py`: Displays the current time based on the inferred timezone.

## Usage

1. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt

