#Build and deploy python service with simple index.html
docker build -t python-backend-image .
docker run -d -p 5001:5000 -v ./backend:/app --name python-backend-container python-backend-image 
