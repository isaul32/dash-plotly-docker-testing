# Dash Plotly Docker Testing

This repository is for testing how Dash Plotly visualization framework can be dockerized.

## Technologies

- Docker
- NGINX
- Dash
- Dash for R

## Architecture

![Architecture diagram](/architecture-diagram.drawio.png)

## User guide

Build & run containers:

```console
docker compose up --build -d
```

Remove the stack:

```console
docker compose down
```

## Dash pages

- http://dash.localhost:8080/
- http://dash.localhost:8080/archive
- http://dash.localhost:8080/analytics

## Dash for R pages

- http://dashr.localhost:8080/

## Useful links

- [Dash Python User Guide](https://dash.plotly.com/)
- [Dash R User Guide](https://dash.plotly.com/r)
- [Deploying Dash Apps](https://dash.plotly.com/deployment)
- [Multi-Page Apps and URL Support](https://dash.plotly.com/urls)
