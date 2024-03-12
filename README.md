# ELT-Data-Pipeline-Postgres-Python-Streamlit

## Initial Setup:
Clone repo and create a virtual environment
```
$ git clone https://github.com/Nalito/ELT-Data-Pipeline-Postgres-Python-Streamlit.git
$ cd ELT-Data-Pipeline-Postgres-Python-Streamlit
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask pandas numpy streamlit scikit-learn requests psycopg2
```

## Fetching Employee Happiness Data From API and Storing it in Postgres Database
In your terminal, run
```
$ (venv) python employee_api.py
```
This will create an API that can be used to generate a specified number of employee data. 

<b>Simulated Employee Data</b>
1. ID: Unique identifier for the employee.
2. Occupation: Randomly selected from a list of job titles. ['HR Manager', 'Software Engineer', 'AI Engineer', 'BI Analyst', 'Mobile Developer', 'QA Engineer']
3. Salary: Randomly generated salary ranging from 100,000 to 750,000.
4. Level: Randomly selected from 'Junior', 'Intermediate', or 'Senior'.
5. Paid Vacation: Randomly selected boolean value indicating whether the employee receives paid vacation.
6. Happiness: Randomly generated happiness score, based on salary, level, and paid vacation status ranging from 1 to 5.

While the Flask server is still running, run ingest.py to fetch the data and place it in a Postgres database. 
<i>P.S. You'll have to use your postgres credentials for the code to work. Make use of hidden.py </i>
```
$ (venv) python ingest.py
```
## Model Development
All the steos used to fetch the data from the databse, preprocess it and build the machine learning model are contained in prediction.ipynb.

## Streamlit Deployment
```
$ (venv) streamlit run streamlit_api.py
```

The deployed application is available here: https://employee-happiness-prediction.streamlit.app/ 🤗
