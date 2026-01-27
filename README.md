This minimal Flask web API provides simple text utilities via URL path parameters.

## Endpoints
- `GET /`
  - Returns a pretty-printed JSON list of available endpoints.

- `GET /uppercase/<text>`
  - Returns an uppercase version of `<text>`.

- `GET /lowercase/<text>`
  - Returns a lowercase version of `<text>`.

- `GET /charcount/<text>`
  - Returns the character count of `<text>`, excluding spaces.

## Setup (Local)
1. Clone this repo to your local machine
2. Build the docker container:
    ```bash
    docker build -t flask_app .
    docker run -p 5000:5000 flask_app
3. Open the url that appears in terminal

