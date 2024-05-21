#!/usr/bin/env bash

IMAGE=project-rvizweb

docker rmi ${IMAGE} -f
./build.sh
