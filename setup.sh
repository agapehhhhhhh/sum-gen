#!/bin/bash
# Setup script for FastAPI summarization service on Ubuntu server

sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker

# Clone project and build
git clone https://github.com/yourusername/summary_service.git
cd summary_service
docker-compose up --build -d
