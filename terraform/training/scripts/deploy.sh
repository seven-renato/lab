#!/bin/bash
set -e

KEY_PATH=./scripts/infra-challenge-wazuh-key.pem
USER=ec2-user
HOST=52.90.229.60

echo "==> Sending files to the EC2..."
scp -i $KEY_PATH ./scripts/setup.sh $USER@$HOST:~/setup.sh
scp -i $KEY_PATH -r ./docker/docker-compose.yml $USER@$HOST:~/docker-compose.yml

echo "==> Connecting to the EC2 and executing setup.sh..."
ssh -i $KEY_PATH $USER@$HOST "chmod +x setup.sh && ./setup.sh"

echo "==> Deployment completed successfully!"
