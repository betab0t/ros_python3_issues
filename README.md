# ros_python3_issues
ROS Package used to reproduce common Python 3 setup issues described in my [Medium post](https://medium.com/@beta_b0t/how-to-setup-ros-with-python-3-44a69ca36674).

# Setup
```sh
mkdir ~/catkin_ws && cd ~/catkin_ws
mkdir src && cd src
git clone https://github.com/betab0t/ros_python3_issues.git
cd ..
catkin_make
source devel/setup.bash
```

## 1. Missing YAML library issue
```sh
rosrun ros_python3_issues issue_yaml.py
```

## 2. cv_bridge issue
```sh
rosrun ros_python3_issues issue_cv_bridge.py
```

## 3. rostest issue
```sh
rostest ros_python3_issues test_issue_rosunit.launch
```
