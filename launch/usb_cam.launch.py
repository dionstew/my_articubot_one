import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # default: file YAML berada di folder "config" yang sama level dengan file launch ini
    pkg_share = get_package_share_directory('articubot_one')
    default_yaml = os.path.join(pkg_share, 'config', 'camera_config.yaml')
    param_file = LaunchConfiguration('camera_param_file')

    return LaunchDescription([
        DeclareLaunchArgument(
            'camera_param_file',
            default_value=default_yaml,
            description='Path ke file parameter kamera (YAML)'
        ),

        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            # namespace='camera',             # topic menjadi /camera/image_raw
            output='screen',
            parameters=[param_file],
            # contoh remap (opsional): ubah nama topic jika perlu
            # remappings=[('image_raw', '/camera/image_raw')],
        ),
    ])

