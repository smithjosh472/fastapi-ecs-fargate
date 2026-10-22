# fastapi-ecs-fargate

A small FastAPI service, containerised with Docker, being built as a hands-on cloud project. The end goal is to deploy it to AWS ECS Fargate using Terraform, with GitHub Actions handling the build and deploy pipeline.

## What it does

The API has two endpoints:

| Endpoint | Description |
| --- | --- |
| `GET /` | Returns a greeting message |
| `GET /health` | Returns `{"status": "ok"}`. Used for health checks, including by AWS later |

## Tech stack

- Python 3.12 and FastAPI, served by Uvicorn
- Docker (slim base image, non-root user)
- Planned: AWS ECR, ECS Fargate, Terraform, GitHub Actions

## Run it locally with Docker

Requires Docker Desktop.

```bash
git clone https://github.com/smithjosh472/fastapi-ecs-fargate.git
cd fastapi-ecs-fargate
docker build -t fastapi-ecs-fargate:local .
docker run --rm -p 8000:8000 --name api fastapi-ecs-fargate:local
```

In a second terminal:

```bash
curl -i http://localhost:8000/health
```

You should see `HTTP/1.1 200 OK` and `{"status":"ok"}`. Interactive API docs are at http://localhost:8000/docs.

## Run it locally without Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Work in progress

- [x] FastAPI app with `/` and `/health`
- [x] Dockerfile (slim image, non-root user)
- [ ] Push the image to AWS ECR by hand
- [ ] Infrastructure as code with Terraform (ECS Fargate service)
- [ ] CI/CD with GitHub Actions (build, push, deploy)
