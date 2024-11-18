# ArgoCD project

## Deploying a Weather Application Docker container on AWS EC2 instance

1. Launch EC2 instance which has 5000 port enabled

2. Install Docker on it

## Dockerize the Flask application

### Build Docker Image from dockerfile
```
docker build -t weather-app .

```
### Run Docker container from Docker Image
```
docker run -itd -p 5000:5000 -e WEATHER_API_KEY=value weather-app

```
### Access your App on browser
```
public_DNS_or_IP:5000
```

## Tag Docker Image and push it to DockerHub
```
docker tag weather-app:latest amrendra01/weather-app:latest
docker push amrendra01/weather-app:latest
```

## Create/configure AWS-EKS/k8s/minikube cluster

## Install ArgoCD on it
```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### Get argocd service name and forward port to access argocd server UI on url http://service-ip:service-port or if it is minikube then it'll be localhost:8080
```
kubectl get svc -n argocd
kubectl port-forward svc/argocd-server - n argocd 8080:443
```