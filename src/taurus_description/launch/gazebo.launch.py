    
# Importación de las librerias necesarias
import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

# Función principal para generar la descripción del lanzamiento
def generate_launch_description():
    taurus_description_dir = get_package_share_directory("taurus_description")
    taurus_description_share = os.path.join(get_package_prefix("taurus_description"), "share")
    gazebo_ros_dir = get_package_share_directory("gazebo_ros")


    # Argumento de lanzamiento para especificar la ubicación del archivo URDF del robot
    model_arg = DeclareLaunchArgument(
        name="taurus",
        default_value=os.path.join(taurus_description_dir, "urdf", "taurus.urdf.xacro"),
        description="Absolute path to robot urdf file"
    )

    # Declaración del archivo del mundo de Gazebo
    world_file_name = 'mundo.world'
    world_path = os.path.join(taurus_description_dir, 'worlds', world_file_name)
    declare_world_cmd = DeclareLaunchArgument(
        name='world',
        default_value=world_path,
        description='Full path to the world model file to load'
    )

    # Configuración de la variable de entorno para la ruta de modelos de Gazebo
    env_var = SetEnvironmentVariable("GAZEBO_MODEL_PATH", taurus_description_share)

    # Configuración del parámetro del nodo del robot_state_publisher
    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("taurus")]), value_type=str)
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )

    # Lanzamiento del servidor Gazebo
    start_gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_dir, "launch", "gzserver.launch.py")),
        launch_arguments={'world': world_path}.items()
    )

    # Lanzamiento del cliente Gazebo
    start_gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_dir, "launch", "gzclient.launch.py")
        )
    )

    # Nodo para spawnear el modelo del robot en Gazebo
    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "taurus", "-topic", "robot_description"],
        output="screen"
    )
    
    # Devuelve la descripción del lanzamiento con los elementos especificados
    return LaunchDescription([
        env_var,
        model_arg,
        declare_world_cmd,
        start_gazebo_server,
        start_gazebo_client,
        robot_state_publisher_node,
        spawn_robot
    ])
