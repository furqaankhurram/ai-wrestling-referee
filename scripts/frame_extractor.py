import cv2
import os


def extract_frames(video_path, output_folder, frame_rate=5):
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    if video_fps == 0:
        print("Warning: Cannot determine FPS of video, defaulting to 30")
        video_fps = 30  # default fallback
    
    print(f"Video FPS: {video_fps}")
    
    frame_interval = int(video_fps / frame_rate)
    if frame_interval == 0:
        frame_interval = 1

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Reached end of video or failed to read frame.")
            break
        
        if frame_count % frame_interval == 0:
            filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Saved {filename}")
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"Done. Extracted {saved_count} frames to {output_folder}")

if __name__ == "__main__":
    video_path = "/home/furqaan-khurram/Documents/ai-wrestling-referee/data/raw_videos/throws_only.mp4"
    output_folder = "/home/furqaan-khurram/Documents/ai-wrestling-referee/data/frames_throws"
    extract_frames(video_path, output_folder)
