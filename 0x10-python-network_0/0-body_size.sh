#!/bin/bash

<<comment
Script that shows the Content-Length from a HTTP request
comment
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
