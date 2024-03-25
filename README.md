# Health Tracker

Health Tracker is a web application designed to help users monitor their daily intake of water, track blood pressure readings, and record exercise time. This README provides an overview of the project and instructions for installation, usage, contributing, and licensing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Register and sign in securely to track your health data.
- **Track Health Metrics**: Record your daily intake of water, blood pressure readings, and exercise time.
- **Dashboard**: View summaries and visualizations of your health data over time.

## Installation

To run the Health Tracker application locally, follow these steps:

1. Clone the repository:

   ```bash
   $ git clone https://github.com/basavaadarsh/Health-Tracker.git
   ```
2. Navigate to the project directory:

   ```
   $ cd health-tracker
   ```
  3.Set up a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
 
   4.Install dependencies:

   ```
    pip install -r requirements.txt
   ```
  5.Set up environment variables:
    Create a .env file in the root directory and add the following:

   ```
   SECRET_KEY=your_secret_key
   DATABASE_URI=sqlite:///database.db
   ```
  Replace your_secret_key with a secret key for Flask session security.

  6. Initialize the database:

   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Usage
Usage
1. Start the Flask development server:
   ```
   $ python run.py
   ```
2. Open your web browser and go to http://localhost:5000 to access the Health Tracker application.

3. Register a new account or sign in with your existing credentials.

4. Begin tracking your health metrics by adding data for water intake, blood pressure, and exercise tim


## Contributing

Contributions are welcome! If you want to contribute to Health Tracker, please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/improvement).

3. Make your changes.

4. Commit your changes (git commit -am 'Add new feature').

5. Push to the branch (git push origin feature/improvement).

6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

### MIT License

MIT License

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

   



