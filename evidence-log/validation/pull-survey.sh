#!/bin/sh
# Pull latest survey responses from the published Google Sheet.
curl -sfL "https://docs.google.com/spreadsheets/d/e/2PACX-1vRtw4ef2mjK-szcbV3bV_ycFMtH42IgA_urPyedDD2sbbJHjRrRFvgBN2UHhLzYN6qJpSqgsa9GnzmO/pub?output=csv" \
  -o "$(dirname "$0")/survey-responses.csv" && echo "survey-responses.csv updated"
