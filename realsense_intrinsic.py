import pyrealsense2 as rs

if __name__ == '__main__':
    # Starts captures
    width, height, fps = 640, 480, 30

    # Sets up realsense
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
    config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
    profile = pipeline.start(config)

    # Get intrinsics
    depth_sensor = profile.get_device().first_depth_sensor()
    cam_scale = depth_sensor.get_depth_scale()
    intrc =  profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
    intrd =  profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()

    # Prints intrinsics
    print(f'Color:\n{intrc}\n')
    print(f'Depth:\n{intrd}, scale: {cam_scale}\n')