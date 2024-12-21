#Build and deploy apache server with simple index.html
docker build -t apache-welcome-image .
docker run -d -p 80:80 --name apache-welcome-container apache-welcome-image