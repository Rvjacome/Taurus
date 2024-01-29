<div align="center">

  # Taurus
</div>

## :books: Package Summary

- :rocket: [`taurus_toolbox](./taurus_toolbox): Provee soporte para Slam con slam_toolbox.
- :robot: [`taurus_description`](./taurus_description): Contiene la descripcion del URDF del robot.
- :ledger: [`taurus_nav2`](./taurus_nav2): Stack de navegacion basado en nav2.

## :paperclips: Information source
- ROS Documentation: https://docs.ros.org/en/humble/index.html

## Installing and cloning ROS 2 packages

To avoid possible errors, please update your system and install the following ROS 2 dependencies.

```bash
sudo apt-get update
sudo apt-get install ros-$ROS_DISTRO-joint-state-publisher ros-$ROS_DISTRO-xacro ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-tf2-* ros-$ROS_DISTRO-gazebo-* ros-$ROS_DISTRO-rviz-default-plugins
```

If the following error appears:<br>
_LookupError: Could not find the resource '<package_name>' of type 'packages'_

Try to install the correponding ROS dependency with

`sudo apt-get install ros-$ROS_DISTRO-<package-name>`

For example:

`sudo apt-get install ros-$ROS_DISTRO-joint-state-publisher-gui`

<br>


## Cloning and building this repo

```bash
cd ~/colcon_ws/src
git clone https://github.com/cmauricioae8/basic_diffbot.git
cd ~/colcon_ws
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
```

If command 'rosdep' not found, use:

```
sudo apt install python3-rosdep2
```

If an error appears indicating that rosdep has not been initialized, so run:
```
rosdep update
```

If <br>
`Error(s) in package '/home/user/colcon_ws/src/basic_diffbot/package.xml':
The manifest contains invalid XML:
not well-formed (invalid token): line 31, column 43`
<br>

Please, modify the package.xml file using **your user name** and try again.


If you already have all your dependencies, the console will return:<br>
#All required rosdeps installed successfully

**Note:** _This is made only once for the whole workspace._

Then, build colcon ws:
```
colcon build --packages-select basic_diffbot --symlink-install
source install/setup.bash
```

**:NOTE:** This builds the package and sets a symbolic link to the python files (nodes and launch files). With this, re-build every time that a python file is modified, is not required.<br>
In ROS 2, launch files may be written in yaml, xml or python languages, but it is extremely recommended to use python. Also, the name of all launch files must finish with 'launch.py'. Otherwise, the file will not be recognized.<br>
If some warnings appear, run `colcon build --packages-select basic_diffbot --symlink-install` again and they will disappear.


#  Diseño
## :electron: Diseño electrico
El diseño de conecciones electricas del Robot.
![Diseño electrico](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/Schematic.jpeg)

## :mechanical_arm: Diseño mecanico
El diseño mecanico del robot se puede obtener en :(Link de Grabcad) en formato .STEP
![ensamblado](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/Robot.jpeg)

## :rocket:Programa:
Colocar dependencias y paquetes usados en para simulacion , nav2


## :computer: Simulation
![gazebo](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/gazebo.jpeg)
![nav2](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/nav2.png)

## :compass: Navigation
#### install slam_toolbox

ROSDep will take care of the major things

```
rosdep install -q -y -r --from-paths src --ignore-src
```

Or install via apt

```
apt install ros-eloquent-slam-toolbox
```

Run your colcon build procedure of choice.

You can run via `ros2 launch slam_toolbox online_sync_launch.py`
### :star2: Referencias:

* *[Pololu Zumo for Arduino][1]*


### Licencia:
Todos estos productos están liberados mediante licencia Apache 2.0

