#!/usr/bin/env bash

IMAGE=rvizweb
# docker run -it --rm -p 8001:8001 -p 9090:9090 -p 9999:9999 "${IMAGE}"
docker run -it --privileged --rm --network="host" "${IMAGE}"
