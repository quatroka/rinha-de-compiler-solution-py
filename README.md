# Rinha de Compiler Solution by Quatroka(python-version)

## Build image

    docker build . --tag=quatroka/rinha-solution:0.1

## Mount files on docker and execute

    docker run -it --volume <host_files>:/usr/src/app/files --rm quatroka/rinha-solution:0.1 <rinha_filepath_to_execute>.json

    # Ex:
    docker run -it --volume ./files:/usr/src/app/files --rm quatroka/rinha-solution:0.1 files/generated_by_me/fib10.rinha.json
