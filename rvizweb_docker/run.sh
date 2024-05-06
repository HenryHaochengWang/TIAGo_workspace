#!/usr/bin/env bash

IMAGE=rvizweb
docker run -it --rm -p 8001:8001 "${IMAGE}"