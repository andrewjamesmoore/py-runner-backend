# PyRunner Backend

Backend services for PyRunner — the server-side components that support the PyRunner frontend. This repository contains the application code, a Dockerfile, a `docker-compose.yml` for local development, an Nginx configuration, and Terraform scripts for infrastructure provisioning.

See the frontend repo here: [https://github.com/andrewjamesmoore/py-runner](https://github.com/andrewjamesmoore/py-runner)

## Table of contents

* [About](#about)
* [Features](#features)
* [Tech stack](#tech-stack)
* [Quick start (docker-compose)](#quick-start-docker-compose)
* [Development (local Python)](#development-local-python)
* [Security and limits](#security-and-limits)
* [Deployment](#deployment)
* [Project structure](#project-structure)
* [License and author](#license-and-author)

---

## About

This repository provides the backend for the PyRunner project. It is intended to be deployed as a containerized service behind Nginx and managed via Terraform for infrastructure. The backend implements the server-side API and any persistence or background jobs required by the frontend.

Note: the exact runtime entrypoint and exposed endpoints are defined in the `app/` folder and the `Dockerfile`; consult those files to confirm the application server and startup command.

## Features

* Containerized Python backend with a Dockerfile
* Local orchestration with `docker-compose.yml` for development
* Nginx configuration for reverse proxying and TLS termination
* Terraform scripts for provisioning infrastructure
* `requirements.txt` lists Python dependencies

## Tech stack

* Python (application code)
* Docker / Docker Compose
* Nginx (reverse proxy)
* Terraform (infrastructure as code)

## Quick start (docker-compose)

The fastest way to run the backend locally is with Docker Compose.

```bash
# clone the repo
git clone https://github.com/andrewjamesmoore/py-runner-backend.git
cd py-runner-backend

# build and run
docker-compose up --build
```

The compose file included in the repository defines the service(s) and supporting containers — check `docker-compose.yml` for service names, exposed ports, and environment variables.

## Development (local Python)

To iterate on the Python code locally without Docker:

```bash
# create virtualenv
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Security and limits

* Treat `SECRET_KEY` and DB credentials as secrets — do not commit them to source control.
* Limit inbound access to administrative endpoints; prefer internal network access for management routes.
* If the backend executes or evaluates code (e.g. for scheduled tasks or code execution support), ensure strict sandboxing and resource limits — prefer delegating execution to isolated workers or third-party sandboxes.
* Use TLS (nginx) in front of the service in production.

## Deployment

Recommended deployment flow:

1. Build a production image using the included `Dockerfile`.
2. Push the image to a container registry.
3. Provision infrastructure via the `terraform/` scripts in this repo (adjust to your cloud provider and state backend).
4. Deploy containers to the target hosts or container platform and configure Nginx to proxy traffic.

The repo includes an `nginx/` folder and `terraform/` folder to help with these steps — review and adapt them before production use.

## Project structure

The repository follows a simple layout; adapt to the project as needed:

```
.github/workflows/  # CI workflows
app/                # application source
nginx/              # nginx config and assets
terraform/          # infra-as-code modules and configs
Dockerfile
docker-compose.yml
requirements.txt
```

## License and author

License: MIT

Author: [https://github.com/andrewjamesmoore](https://github.com/andrewjamesmoore)
