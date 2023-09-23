# Rinha de Compiler Solution by Quatroka(python-version)

> Disclaimer: Attention: this code should not be considered for real production cases. Made in a few hours "4 fun" and curiosity.

![GIF](banner.gif)

Hello, this is another solution to participate in the [Rinha de Compiladores](https://github.com/aripiprazole/rinha-de-compiler).
It was great to learn and see how far I could go
 without ever having studied computer science
 (and without having done computer science).

## Build image

    docker build . --tag=quatroka/rinha-solution:0.1

## Mount files on docker and execute

    docker run --volume <host_files>:/usr/src/app/files --rm quatroka/rinha-solution:0.1 <rinha_filepath_to_execute>

    # Ex:
    docker run --volume ./files:/usr/src/app/files --rm quatroka/rinha-solution:0.1 files/rinha_examples/fib.rinha.json

### Execute unit testing

    # install python unit test dependency
    $ pip install -r requirements.txt
    #OR
    $ pip install pytest

    # Execute tests
    $ pytest

### Run locally

    python -m main <filepath>
    # Ex:
    python -m main files/rinha_examples/fib.rinha.json
