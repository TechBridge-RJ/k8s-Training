# Build and run image
docker build -t nginx-lb-image .
docker run -d -p 5000:5000 --name nginx-lb-container python-lb-image:latest