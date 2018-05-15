# NFLPredictor

## Assumptions
The following assumes the person checking out the NFL Predictor program is working on a machine with python 2.7 and virtualenv installed.  If the developer/user wishes to interact with the program via an interface, then they will need to also checkout and set up the predictorui program also found on this github account.   

## Setting Up and Running
To run the NFL Predictor program, first check out the project, move into the root directory, then create a virtual environment called venv in the project's directory.
```
cd NFLPredictor
virtualenv venv
```

Next, activate the virtual environment with the following command. 
```
source venv/bin/activate
```   

After running the above command, if successful you will see "(venv)" before your terminal promp.  Next, within the root of the project (same directory as the requirements.txt file) install the required project dependencies by running the following:
```
pip install -r requirements.txt
```

Finally, in the project's root (the same directory as app.py) run the following:
```
python app.py
```

The app should now be listening for requests at localhost:5000

## Deactivating the Virtual Environment
To deactivate the venv virtual environment, run the following command from the project's root directory.
```
deactivate
``` 