# Use the official Apache image
FROM httpd:2.4

# Set environment variables
ENV HOST_IP="192.168.0.22"
ENV BACKEND_API="192.168.0.22"
ENV BACKEND_PORT="5000"

# Copy the HTML file into the web root
COPY ./pages/* /usr/local/apache2/htdocs/
COPY updateEnv.sh /usr/local/bin/updateEnv.sh

# Make the script executable
RUN chmod +x /usr/local/bin/updateEnv.sh

# Map the /user_name URL to the /cgi-bin/user_name.sh script
RUN echo 'Alias /hostip /usr/local/apache2/htdocs/hostip' >> /usr/local/apache2/conf/httpd.conf
RUN echo 'Alias /backendapi /usr/local/apache2/htdocs/backendapi' >> /usr/local/apache2/conf/httpd.conf
RUN echo 'Alias /backendport /usr/local/apache2/htdocs/backendport' >> /usr/local/apache2/conf/httpd.conf

# Expose port 80 to the host
EXPOSE 80

# Start Apache server
CMD ["/bin/bash","-c","/usr/local/bin/updateEnv.sh && httpd-foreground"]
