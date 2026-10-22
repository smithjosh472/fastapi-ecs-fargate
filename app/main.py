from fastapi import FastAPI

app = FastAPI (title="fastapi-ecs-fargate")


@app.get("/")
def root():
	return {"message": "Hello from fastapi-ecs-fargate"}

@app.get("/health")
def health():
	return {"status": "ok"}
