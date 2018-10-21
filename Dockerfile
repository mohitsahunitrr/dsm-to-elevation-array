FROM ubuntu:18.04

# Install basic things
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y build-essential

# Install language
RUN apt install -y python python-pip python-gdal gdal-bin libgdal-dev psrecord

# Set an user for app
RUN useradd -m dsm-to-elevation-array

WORKDIR /home/dsm-to-elevation-array

ENTRYPOINT ["/bin/bash"]
