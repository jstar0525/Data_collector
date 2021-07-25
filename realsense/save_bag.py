import os
from pathlib import Path
from datetime import datetime
import pyrealsense2 as rs

def set_realsense(SN='xxxxxxxxxxxx'):

    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device(SN)
    # config.enable_all_streams()
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 5)
    config.enable_stream(rs.stream.infrared, 1, 1280, 720, rs.format.y8, 5)
    config.enable_stream(rs.stream.infrared, 2, 1280, 720, rs.format.y8, 5)
    config.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 5)

    return pipeline, config
    

def record_bag(pipeline, config, path, video_time):

    try:
        while(True):
            t1 = datetime.now()
            t = t1.strftime('%Y-%m-%d_%H-%M-%S_%f')
            f_name = os.path.join(path, t)
            config.enable_record_to_file(f_name+'.bag')
            print(t)

            pipeline.start(config)
            dt = 0

            while(dt < video_time):
                pipeline.wait_for_frames()
                t2 = datetime.now()
                dt = (t2-t1).total_seconds()
                
            pipeline.stop()

    finally:
        pipeline.stop()
        

if __name__ == '__main__':
    path = Path('/media/robotv/HDD01/realsense/d455')
    path.mkdir(parents=True, exist_ok=True)
    video_time = 60  # sec

    pipeline, config = set_realsense(SN='xxxxxxxxxxxx')
    record_bag(pipeline, config, path, video_time)
