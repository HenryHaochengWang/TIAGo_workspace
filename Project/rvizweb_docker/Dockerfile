FROM ros:kinetic

# Basic tools and dependencies and nodejs LTS PPA.
RUN apt update && apt install -y curl nano && curl -sL https://deb.nodesource.com/setup_14.x | bash -

# Install rvizweb.
WORKDIR /rvizweb_ws
ARG rvizweb_branch=master
RUN git clone https://github.com/osrf/rvizweb/ src/rvizweb -b ${rvizweb_branch}
RUN rosdep install --from-paths src --ignore-src -r -y

# NEW ADDED: Install npm bower and polymer-cli.
# RUN apt-get install npm 
RUN npm install -g bower polymer-cli --unsafe-perm=true --allow-root

WORKDIR /rvizweb_ws/src/rvizweb
RUN bower install --allow-root && bower install eventemitter2 --save --allow-root
# RUN polymer build


WORKDIR /rvizweb_ws
RUN . /opt/ros/kinetic/setup.sh && catkin_make install

# Clear apt cache.
RUN apt clean

# Copy the web files to the shared directory.
WORKDIR /rvizweb_ws
RUN rm -rf /rvizweb_ws/install/shared/rvizweb/www/*
RUN cp -r /rvizweb_ws/build/rvizweb/www/* /rvizweb_ws/install/share/rvizweb/www/

EXPOSE 8001

# ENTRYPOINT ["/bin/bash", "-c", "source /rvizweb_ws/install/setup.bash && /bin/bash"]
        # roslaunch rvizweb rvizweb.launch"]
ENTRYPOINT ["/bin/bash", "-c", "source /rvizweb_ws/install/setup.bash && roslaunch rvizweb rvizweb.launch"]
