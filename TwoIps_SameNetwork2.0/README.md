## Prereqs
> This program runs on Windows and Linux, made with Python 3.8
> The program should be in the same directory as the InputModule.py file.
> This module is imported to control the users input for purposes of error handling.

## Installation
- Run the setup.py script to build a virtual environment and install all external packages in the created venv.

> Example:<br>
> python3 setup.py "venv name"

- Once virtual env is built traverse to the Scripts directory in the environment folder just created.
- In the Scripts directory, execute the "activate" script to activate the virtual environment.

## Purpose
> The program is designed to determine if two IP addresses are on the same subnet.
> The program begins by prompting the user for two IP addresses and a subnet mask.
> It then determines if the assigned IPs are in the same subnet based off the chosen CIDR.

> A tutorial that explains the development process to version 2 can be found here:<br>
> https://cybr.com/programming-languages-archives/how-i-made-my-python-subnet-calculator-more-efficient-with-40-less-code/