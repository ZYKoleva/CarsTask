# CarsTask

This repository contains application that reads data file in json format, performs operations on the dataset 
and prints the results in the console.
Logs are generated for every operation and saved in app_logs.log file.

When app is run, the below operations are being performed in the following order:
* reading .json file from specified location and loading data as pd.DataFrame
* get_unique_number for values in specified df[column]
* get_average for values for specified df[column]
* get_top_max n values for specified df[column]
* get_count_by_value for specified df[column]
* get_count_by_year for specified[datetime_column]
* saving dataset as csv file to a specified location

The parameters that are being passed to the functions are defined in config/config.yaml section: functions_params

#### Repository Structure    

````commandline

├───app
│      main.py 
│      __init__.py
│
├───config
│       config.yaml # contains configuration settings for the data file, functions params, output file details
│
├───logs
│       app_logs.log # log file containing app logs
│
├───output
│       cars.csv # output data file
│
├───raw_data
│       cars.json # input data file
│
└───utils
│       handler.py # DataHandler class with methods for performing various operations
│       helper.py # FilesHelper class with methods for reading from and writing to files
│       logger.py # Logger class for managing file and console loggers
│       __init__.py
│   .gitignore
│   pyvenv.cfg
│   README.md
│   requirements.txt
│   setup.cfg
│   setup.py

````      

#### Setup commands

```commandline
# clone the repository
git clone https://github.com/ZYKoleva/CarsTask.git    

# cnahge dir to project root
cd CarsTask    

# create virtual environment
python -m venv venv    

# activate env
venv/Script/activate    

# run setup.py
pip install -e .    

# run app from within root dir
run-app
```

#### Run Pytests
````commandline
# within root dir, run below command
pytest -vs # Ensure that the logger.propagate = True in the logger.py file
````