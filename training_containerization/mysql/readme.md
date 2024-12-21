# Build image and run container
docker build -t mysql-demo-image .
docker run -d -p 3306:3306 -v ./data:/var/lib/mysql --name mysql-demo-container mysql-demo-image
