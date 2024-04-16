FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y\
    curl\
    gnupg2\
    lsb-release

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'\
    && curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

RUN apt-get update && apt-get install -y \
    ros-noetic-desktop-full

RUN rosdep init && rosdep update

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
ENV ROS_PACKAGE_PATH="/opt/ros/noetic/share"

WORKDIR /app

COPY ../henry_ws /app/henry_ws
COPY Docker/start.sh /usr/local/bin/start.sh

VOLUME [ "/mnt/henry_ws" ]

CMD ["/usr/local/bin/start.sh"]

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
                  cd /app/henry_ws"

