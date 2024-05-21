FROM ros:kinetic

# Basic tools and dependencies and nodejs LTS PPA.
RUN apt update && apt install -y curl && curl -sL https://deb.nodesource.com/setup_16.x | bash -

# Install npm.
RUN apt install -y npm

# Install rvizweb.
WORKDIR /rvizweb_ws
ARG rvizweb_branch=master
RUN git clone https://github.com/osrf/rvizweb/ src/rvizweb -b ${rvizweb_branch}
RUN rosdep install --from-paths src --ignore-src -r -y

# Install npm packages.
WORKDIR /rvizweb_ws/src/rvizweb
COPY package.json .
RUN npm install

# Build rvizweb.
WORKDIR /rvizweb_ws
RUN . /opt/ros/kinetic/setup.sh && catkin_make install

# Clear apt cache.
RUN apt clean

EXPOSE 8001

ENTRYPOINT ["/bin/bash", "-c", "source /rvizweb_ws/install/setup.bash && roslaunch rvizweb rvizweb.launch"]
