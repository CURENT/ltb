#!/usr/bin/env bash

tag=ltb:${TAG:-$USER}
name=ltb_$USER
target=base
data=/Users/hcui7/tmp
registry=ltb.curent.utk.edu:5000
xauth=
entrypoint=
ipc=
net=host
user=1
cwd=1
interactive=1
script=
port=8810
pipindex=
piptrustedhost=

[ -f env.sh ] && . env.sh

build() {
    # Build the Docker image
    echo "Building Docker image $tag..."
    docker build \
        ${target:+--target $target} \
        ${pipindex:+--build-arg PIP_INDEX_URL=$pipindex} \
        ${piptrustedhost:+--build-arg PIP_TRUSTED_HOST=$piptrustedhost} \
        -t $tag .
}

agvis() {
    tmux send-keys -t0 "docker run -u root --rm -t -v /tmp:/tmp -v `pwd`/agvis/static:/srv -p 8810:8810 $tag agvis run --static /srv --port $((port+0))"
    }

dev() {
    google-chrome --incognito http://localhost:8810/ 2> /dev/null > /dev/null &!
    
    tmux split-window -v
    tmux split-window -v
    tmux select-layout tiled
    tmux send-keys -t0 "docker run -u root --rm -t -v /tmp:/tmp -v `pwd`/agvis/static:/srv -p 8810:8810 $tag agvis run --static /srv --port $((port+0))" Enter
    tmux send-keys -t1 "docker run --rm -t -v /tmp:/tmp -p 8818:8818 $tag dime -vv -l unix:/tmp/dime2 -l ws:$((port+8))" Enter
    tmux send-keys -t2 "docker run -u root --rm -t -v /tmp:/tmp -v `pwd`/agvis/cases:/home/cui/work $tag andes run wecc.xlsx -r tds --dime-address ipc:///tmp/dime2"
}

clean() {
    echo "Stopping and removing all Docker containers and images..."
    if [ -n "$(docker ps -aq)" ]; then
        docker stop $(docker ps -aq)
    fi
    if [ -n "$(docker ps -q)" ]; then
        docker kill $(docker ps -q)
    fi
    if [ -n "$(docker images -a -q)" ]; then
        docker rmi $(docker images -a -q)
    fi

    echo "Stopping all tmux sessions..."
    tmux kill-server

    echo "Removing DiME Unix domain sockets..."
    if [ -e "/tmp/dime" ]; then
        rm /tmp/dime
    fi
    if [ -e "/tmp/dime2" ]; then
        rm /tmp/dime2
    fi

    echo "Cleaning completed."
}

"$@"
