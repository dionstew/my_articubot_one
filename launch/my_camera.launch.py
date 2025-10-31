from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_camera',
            output='screen',
            parameters=[{
                'camera_name': "front_drive_cam",
                'video_device': '/dev/video0',
                'image_width': 640,
                'image_height': 480,
                'pixel_format':'mjpeg2rgb',
                'framerate': 30.0,
                'frame_id': 'camera_link_optical',
                'io_method': 'mmap'
            }]
        )
    ])
