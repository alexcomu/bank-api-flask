# BANK API - Flask Project

## Requirements

You'll need MongoDB and Flask.

## Install

Clone the repo, create a virtualenv and install the requirements:

    git clone https://github.com/alexcomu/bank-api-flask.git
    cd bank-api-flask
    virtualenv envFlask
    source envFlask/bin/activate
    pip install -r requirements

## Run

Just:

    python app.py

## Route

Only 3 routes:

    http://localhost:5000/ 
    http://localhost:5000/banks
    http://localhost:5000/data/BANK_ID

# API

Project's APIs accept only **GET** Method.

### BANKS

URL Example

    http://localhost:5000/banks

Response Example

    {
    "data": [
        {
            "BANK": "bank pippo", 
            "BANK_ID": 0
        }, 
        {
            "BANK": "bank pluto", 
            "BANK_ID": 1
        }, 
        {
            "BANK": "bank minny", 
            "BANK_ID": 2
        },
        ... 
        ]
    }


### DATA

URL Example

    http://localhost:5000/banks

Response Example

    {
      "bank": {
        "BANK": "bank pippo", 
        "BANK_ID": 0
      }, 
      "data": [
        {
          "BANK": "bank pippo", 
          "BANK_COUNTRY": "Austria", 
          "COUNTRY_EXPOSURE": "12.08", 
          "EXPOSURE_COUNTRY": "Austria", 
          "GDP_2012_EURO": "309,900.90", 
          "MILLIONS_EUROS": "931.71"
        }, 
        {
          "BANK": "bank pippo", 
          "BANK_COUNTRY": "Austria", 
          "COUNTRY_EXPOSURE": "0.21", 
          "EXPOSURE_COUNTRY": "Belgium", 
          "GDP_2012_EURO": "376,840.00", 
          "MILLIONS_EUROS": "16.32"
        }, 
        {
          "BANK": "bank pippo", 
          "BANK_COUNTRY": "Austria", 
          "COUNTRY_EXPOSURE": "4.20", 
          "EXPOSURE_COUNTRY": "Bulgaria", 
          "GDP_2012_EURO": "39,667.70", 
          "MILLIONS_EUROS": "324.11"
        },
        ...
      ]
    }