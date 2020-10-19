# Setup 

## Setup a virtual env
cd into the server folder, and create a virtual env. Using the default venv that is packed with python: 

    python -m venv <name_of_your_venv>

## Activate venv 
Run the following command to activate your venv if created using the above step. If you created it using a different venv, then you need to look that up.

    venv/Scripts/activate

## Install Requirements
Make sure you have python3 installed. 

cd into the `server` folder and run the following command to install the dependencies: 
    
    pip install -r requirements.txt

# Run
Start the server: 
    
    python3 server.py
 