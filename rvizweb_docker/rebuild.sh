#!/usr/bin/env bash

IMAGE=rvizweb

docker rmi ${IMAGE} -f
./build.sh