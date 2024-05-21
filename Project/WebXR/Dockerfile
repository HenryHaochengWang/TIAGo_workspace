# webxr/Dockerfile
FROM node:14-slim

WORKDIR /app
COPY . /app

# Install http-server and curl
RUN npm install -g http-server && apt-get update && apt-get install -y curl

# Expose port 80
EXPOSE 80

# Command to run http-server
CMD ["http-server", "-p", "80"]
