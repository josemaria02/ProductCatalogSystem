# Product-Catalog-System
A simple backend microservice that exposes RESTful APIs for a product catalog system, containerize using Docker, and sets up a CI/CD workflow using GitHub Actions and deploy it in AWS EKS, with logging and monitoring enabled.

## Features
* CRUD for products
* Search by name and category
* Health check at /health
* SQLite backing store
* Dockerized and deployable to EKS
* Basic CI (lint + tests)

## Tech Stack
* FastAPI, Pydantic, Uvicorn
* SQLite
* Pytest
* Docker
* Kubernetes
* GitHub Actions
* Terraform for EKS

## API
Base URL: http://localhost:8000
* GET `/api/v1/products/` — list products with pagination and filters
    Query params: limit (default 10), offset (default 0), name, category
* GET `/api/v1/products/{id}` — get product by id
* POST `/api/v1/products/` — create
* PUT `/api/v1/products/{id}` — update product by id
* DELETE `/api/v1/products/{id}` — delete product by id
* GET `/health` — health check

## Running Locally
**_Method 1_**
Prereqs: Python 3.11+, pip
```
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

**_Method 2_**
Prereqs: Docker
```
docker build -t product-catalog .

docker run -d -p 8000:8000 product-catalog 
```
# CI/CD (GitHub Actions)
File: `.github/workflows/product-catalog-pipeline.yml`

Prereq: 
1) Create repository in Amazon ECR named product-catalog in region us-east-1. 
Use the below command to create one using aws cli
```
aws ecr create-repository --repository-name product-catalog --region us-east-1
```
2) Configure AWS access key in GitHub secrets 
Current workflow:
* Install deps
* Lint with flake8
* Run tests with pytest
* Build tag and push Docker image to ECR

# Setup EKS using Terraform
Terraform creates an EKS cluster. 

Prereqs: AWS CLI configured, Terraform and kubectl installed.
1) Set variables in `terraform/terraform.tfvars`:
Ensure subnets are in different Availability Zones.
```
    vpc_id     = "vpc-xxxxxxxx"
    subnet_ids = ["subnet-aaa", "subnet-bbb", "subnet-ccc"]
```
2) Deploy:
```
    cd terraform
    terraform init
    terraform plan
    terraform apply
```
3) Connect kubectl:
```
    aws eks update-kubeconfig --region us-east-1 --name product-eks-cluster
```
# Kubernetes Deployment
_Manifests:_
`k8s/deployment.yaml`
`k8s/service.yaml` (type LoadBalancer)
```
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    kubectl get svc product-catalog-service
```
Load the application using the URL/ IP given under EXTERNAL_IP

