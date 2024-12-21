#!/bin/bash

echo $HOST_IP  > /usr/local/apache2/htdocs/hostip
echo $BACKEND_API  > /usr/local/apache2/htdocs/backendapi
echo $BACKEND_PORT  > /usr/local/apache2/htdocs/backendport
