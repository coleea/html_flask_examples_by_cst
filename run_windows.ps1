# flask_run.ps1

# Set environment variables
$env:FLASK_ENV = "development"
$env:FLASK_APP = "routes"

# Activate virtual environment
pipenv shell

# Start Flask app
pipenv run flask run
