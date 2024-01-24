# Taurus
MazeSolverRobot
--ROS version : ROS2 HUMBLE--
## Information source
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

**NOTE:** This builds the package and sets a symbolic link to the python files (nodes and launch files). With this, re-build every time that a python file is modified, is not required.<br>
In ROS 2, launch files may be written in yaml, xml or python languages, but it is extremely recommended to use python. Also, the name of all launch files must finish with 'launch.py'. Otherwise, the file will not be recognized.<br>
If some warnings appear, run `colcon build --packages-select basic_diffbot --symlink-install` again and they will disappear.

# **Diseño del Robot**
Este proyecto se constan en la realizacion desde su conceptualizacion hasta la implementacion de un robot Resuelve laberinto para competencia.
Existen varias categorias de Robot Laberinto o Maze Solver Robot ,entre estas estan:
####  Micro-Mouse Mini:
Puede tener restricciones más estrictas en cuanto a tamaño y peso. Por ejemplo:
Tamaño máximo: 10 cm x 10 cm
Peso máximo: 150 gramos.
####  Micro-Mouse Classic:
La categoría estándar para Micro mouse, con restricciones de tamaño y peso, pero más flexibilidad que la categoría Mini. Ejemplo:
Tamaño máximo: 18 cm x 18 cm
Peso máximo: 500 gramos
####  Micro-Mouse Mega:
Puede permitir robots más grandes y complejos. Ejemplo:
Tamaño máximo: 25 cm x 25 cm
Peso máximo: 1 kilogramo.

Las restricciones cambian un poco dependiendo por ejemplo del Pais donde se realiza la competencia .restricciones en cuanto a tamaño para el diseño de Taurus se tomaron de la pasada competencia Robot & Science 2023 de la categoria de Robot Laberinto Classic en las que las dimensiones maximas del robot no debe superar los 15x15x15 cm sin restriccion de peso y se prohibe expandir sus dimensiones durante la competencia y ademas el robot debe ser completamente autonomo prohibiendose el uso de sistemas de comunicacion externo.
Los componentes para el desarrollo de Taurus fueron:
### Materiales:
* Caster ball Pololu Zumo 
* Raspberry pi pico ( W si se desea usar el un control inalambrico)
* Bateria de 3.7V
* Bateria 7.5V
* modelo TB6612FNG driver motor
* 2 GP2Y0A41SK0F sensor - alcance 4-30 cm
* Zumo Reflectance Sensor Array (QTR)
* N20 DC Motor with Magnetic Encoder - 6V
* Piezas impresas 3D PLA
* Tornillos de 3 mm de diámetro para sujeción
* Cables para conexionado, (recomendado CI perforado universal para soldar cables) o se puede usar la PCB diseñada en este proyecto
* SD card adapter

# Diseño
## Diseño electrico
El diseño de conecciones electricas del Robot.
![Diseño electrico](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/Schematic.jpeg)

## Diseño mecanico
El diseño mecanico del robot se puede obtener en :(Link de Grabcad) en formato .STEP
![ensamblado](https://github.com/Rvjacome/Taurus/blob/main/Imagenes/Robot.jpeg)

### Programa:
Colocar dependencias y paquetes usados en para simulacion , nav2
### Desplazamientos y giros:
Taurus es un robot diferencial de lo que 

### Piezas impresas:


### Construcción:
Armado fisico





### Referencias:

* *[Pololu Zumo for Arduino][1]*



### Autor:
**Robinson Vinicio Jacome Bejarano**

### Agradecimientos:



### Licencia:
Todos estos productos están liberados mediante licencia Apache 2.0

[1]:https://www.pololu.com/product/2506


