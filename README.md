# weather-application-using-flask

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
