#!/usr/bin/env bash
set -e

usage() {
  echo "Test that the docker image can be run, and API has started succesfully."
  echo
  echo "Usage: $0 <image_tag>"
  echo
  echo "Arguments:"
  echo "  <image_tag>   The Docker image tag to test"
  echo
  echo "Options:"
  echo "  -h, --help    Show this help message and exit"
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

# Require IMAGE_TAG
if [[ $# -lt 1 ]]; then
  echo "Error: <image_tag> is required."
  usage
  exit 1
fi

IMAGE_TAG="$1"

NAME_PROJECTION_STORAGE=projection-storage

function cleanup {
    echo "Cleaning up"
    docker kill $NAME_PROJECTION_STORAGE > /dev/null || true
}

trap cleanup EXIT

docker run --rm -d \
    -p 8000:8000 \
    --name $NAME_PROJECTION_STORAGE $IMAGE_TAG

function retry() {
    local -r -i max_attempts="$1"; shift
    local -i attempt_num=1
    until [[ $($@) == '{"message":"Hello World"}' ]];
    do
        if ((attempt_num==max_attempts))
        then
            echo "Attempt $attempt_num failed and there are no more attempts left!"
            return 1
        else
            echo "Attempt $attempt_num failed! Trying again in $attempt_num seconds..."
            sleep $((attempt_num++))
        fi
    done
    echo "SUCCESS"
    exit 0
}

retry 10 curl --silent http://localhost:8000
