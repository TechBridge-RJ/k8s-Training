# Build image and run container
docker build -t apache-demo-image .
docker run -d -p 8080:80 -v ./pages:/usr/local/apache2/htdocs/ --name apache-demo-container apache-demo-image 
# with environment variables
docker run -d -p 8080:80 -v ./pages:/usr/local/apache2/htdocs/ -e HOST_IP="192.168.0.22" -e BACKEND_API="192.168.0.22" -e BACKEND_PORT="5000"  --name apache-demo-container apache-demo-image 