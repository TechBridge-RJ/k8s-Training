# Use an official Apache HTTP Server image
FROM httpd:2.4

# Set environment variable for the user
ENV USER_NAME="<Replace Your Name>"

# Copy the custom index.html to the Apache web directory
COPY index.html /usr/local/apache2/htdocs/

SHELL ["/bin/bash", "-c", "echo $USER_NAME  > /usr/local/apache2/htdocs/user_name"]

# Map the /user_name URL to the /cgi-bin/user_name.sh script
RUN echo 'Alias /user_name /usr/local/apache2/htdocs/user_name' >> /usr/local/apache2/conf/httpd.conf

# Expose port 80
EXPOSE 80

# Start Apache server
CMD ["httpd-foreground"]