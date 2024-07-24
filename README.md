# antlr4-demo-python3

## Running ANTLR4 on the grammar file

You only need to do this if you change the grammar file `Demo.g4`.

Only once, get the JAR for antlr:

    curl -o antlr-4.13.1-complete.jar https://www.antlr.org/download/antlr-4.13.1-complete.jar

To run it:

    java -jar antlr-4.13.1-complete.jar -Werror -no-listener -visitor -Dlanguage=Python3 -o demo Demo.g4

This is also provided in the shell script `antlr4.sh`
