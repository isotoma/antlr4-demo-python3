# antlr4-demo-python3

## Get ANTLR

Only once, get the JAR for antlr:

    curl -o antlr-4.13.1-complete.jar https://www.antlr.org/download/antlr-4.13.1-complete.jar

You'll need java if not already installed

    sudo apt install default-jre

## Running ANTLR4 on the grammar file

You only need to do this if you change the grammar file `Demo.g4`.

    `./antlr4.sh`

## Python setup

    pyenv local 3.12
    pip install poetry # if not already
    poetry self add poetry-plugin-shell

    poetry install
    poetry shell
    
## Running a program

To execute a program in the Demo language

    ./democli program1.demo


## ANTLR debugging

You can view the tree - TBC
