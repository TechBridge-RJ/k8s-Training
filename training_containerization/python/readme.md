# Build and run image
docker build -t python-demo-image .
docker run -d -p 5000:5000 -v ./backend_api:/app --name python-demo-container python-demo-image:latest
# with environment variable configured
docker run -d -p 5000:5000 -v ./backend_api:/app -e dbTable="users_feedback" -e dbHost="192.168.0.22" -e dbName="demo_mysql" -e dbUser="mysql-admin" -e dbPass="mysql-password"  --name python-demo-container python-demo-image:latest
# with multiple dev environment
docker run -d -p <Port>:5000 -v ./backend_api:/app -e dbTable="users_feedback" -e dbHost="192.168.0.22" -e dbName="demo_mysql" -e dbUser="mysql-admin" -e dbPass="mysql-password"  --name python-demo-container python-demo-image:latest