from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node kamera USB
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_camera',
            output='screen',
            parameters=[{
                'video_device': '/dev/video0',
                'image_width': 320,
                'image_height': 240,
                'framerate': 30.0,
                'pixel_format': 'mjpeg2rgb',     # gunakan MJPEG
                'io_method': 'mmap',
                'camera_frame_id': 'camera_link_optical'
            }]
        ),

        # Node image_transport untuk republish compressed
        Node(
            package='image_transport',
            executable='republish',
            name='image_republish',
            arguments=['compressed', 'raw'],
            remappings=[
                ('in/compressed', '/image_raw/compressed'),
                ('out', '/image_raw')
            ],
            output='screen'
        )
    ])
