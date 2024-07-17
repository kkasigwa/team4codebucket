# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
# ENV PATH $PATH:/opt/mqm/bin
ENV LD_LIBRARY_PATH /opt/mqm/lib:/opt/mqm/lib64

# Install system dependencies
RUN apt-get update 
RUN apt-get install -y ssh
RUN apt-get install -y git
RUN apt-get install -y nano
RUN apt-get install -y vim
# RUN apt-get install -y vi
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
# RUN apt-get install -y python3-devel
RUN apt-get install -y gcc
    # libpq-dev \
    # && apt-get clean \
    # && rm -rf /var/lib/apt/lists/*

# pip3 install virtualenv
# git config --global user.email "ec2-docker-`cat /etc/hostname`@ba"
# git config --global user.name "ec2-docker-`cat /etc/hostname`"
    
# Set the working directory in the container
# WORKDIR /usr/src/app
WORKDIR /opt

# Copy the requirements file into the container
COPY requirements.txt ./
COPY MQServer/ ./MQServer
# COPY Errorcodes.properties ./

RUN MQServer/mqlicense.sh -accept

RUN dpkg -i MQServer/ibmmq-runtime_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-java_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-jre_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-gskit_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-server_9.4.0.0_amd64.deb

RUN dpkg -i MQServer/ibmmq-amqp_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-ams_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-client_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-ftbase_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-ftagent_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-ftlogger_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-ftservice_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-fttools_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-man_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-cs_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-de_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-es_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-fr_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-hu_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-it_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-ja_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-ko_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-pl_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-pt_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-ru_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-zh-cn_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-msg-zh-tw_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-samples_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-sdk_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-web_9.4.0.0_amd64.deb
RUN dpkg -i MQServer/ibmmq-xrservice_9.4.0.0_amd64.deb

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
# COPY src/ ./src
COPY env.sh ./

# Make port 8080 available to the world outside this container
# EXPOSE 8080

# Run transform.py when the container launches
CMD ["python", "./src/ecsservice/app.py"]
# CMD ["source", "./env.sh"]
