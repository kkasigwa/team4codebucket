#!/bin/bash

docker-start() {
    # doci="55ac4ee96fd5"
    if [ "$1" == "" ]; then
        echo "usage: <docker container id>"
    else
        doci="$1"
        docker start $doci
        docker exec -it $doci /bin/bash
    fi
}

docker-start() {
    # doci="55ac4ee96fd5"
    if [ "$1" == "" ]; then
        echo "usage: <docker container id>"
    else
        doci="$1"
        docker stop $doci
        docker rm $doci
    fi
}
