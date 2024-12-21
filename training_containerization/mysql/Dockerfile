# Use the official MySQL image from Docker Hub
FROM mysql:8.0

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=demo_mysql
ENV MYSQL_USER=mysql-admin
ENV MYSQL_PASSWORD=mysql-password

# Copy any custom SQL scripts to be initialized on container startup
# (These scripts will be automatically executed when the container is first run)
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose port 3306 (MySQL default port)
EXPOSE 3306