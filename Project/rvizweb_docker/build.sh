#!/usr/bin/env bash

IMAGE=project-rvizweb

pushd "$(dirname "${BASH_SOURCE[0]}")"
docker build -t ${IMAGE} "$@" .
popd
