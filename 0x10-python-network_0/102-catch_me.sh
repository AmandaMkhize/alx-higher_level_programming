#!/bin/bash
# Sends a request to trigger a specific response
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" >/dev/null 2>&1
