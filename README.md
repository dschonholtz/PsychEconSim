# An Economic Market Simulator

The original purpose of this project was to simulate simple markets
with buyers and sellers. Then to slowly add in psychological factors and to make
the markets more complex.

The long term goal would be to make extremely accurate economic simulations that
not based on inherently flawed macro models, but instead to base the simulation
on as accurate as possible individual agents. 

Then to see if macro economic principle arise from those agents when interacting
with each other.

## How to set up and run.

This is a python project and has been tested on python 3.8.

1. Install Python 3.x
1. cd into the top level of this directory
1. (Optional) Set up a virtual python env
1. run 

        pip install -r requirements.txt
        
1.  Run 

        python main.py
        

## The long term goal for this project

1. Have a flask web server be one of the controllers for this app.
1. Have a react/vue app that calls into the python app. 
1. Have development all running in a kubernetes cluster that can also
seemlessly and effortlessly deploy it.
