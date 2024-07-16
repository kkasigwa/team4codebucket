# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

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

# RUN dpkg -i MQSeriesRuntime-9.4.0-0.x86_64.rpm
# RUN dpkg -i MQSeriesGSKit-9.4.0-0.x86_64.rpm
# RUN dpkg -i MQSeriesSDK-9.4.0-0.x86_64.rpm
# RUN dpkg -i MQSeriesClient-9.4.0-0.x86_64.rpm

RUN dpkg -i ibmmq-amqp_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-ams_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-client_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-ftagent_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-ftbase_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-ftlogger_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-ftservice_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-fttools_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-gskit_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-java_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-jre_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-man_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-cs_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-de_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-es_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-fr_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-hu_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-it_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-ja_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-ko_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-pl_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-pt_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-ru_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-zh-cn_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-msg-zh-tw_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-runtime_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-samples_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-sdk_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-server_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-web_9.4.0.0_amd64.deb
RUN dpkg -i ibmmq-xrservice_9.4.0.0_amd64.deb

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
# COPY src/ ./src

# Make port 8080 available to the world outside this container
# EXPOSE 8080

# Run transform.py when the container launches
CMD ["python", "./src/ecsservice/app.py"]
