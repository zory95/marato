# Bits per la Marató 
This is a machine learning based project to predict covid cases based on the simpthoms 
There are multiple models:

- Cluster contains a clustering model
- R contains the R scripts with a Linear Regression
- ruben contains a Neural Network
- django-marato-masbaratillas contains a Django project with to run an interface for predicting new data

## Running the Django project
- Get into the directory
- Install the requirements by: `pip install -r requirements.txt`
- Run migrations : `python manage.py migrate`
- Run the server: `python manage.py runserver`

Visit http://localhost:8000/ for accessing the website

