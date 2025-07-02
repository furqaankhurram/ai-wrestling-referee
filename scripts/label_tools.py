import cv2
import os
import csv

frame_dir = '/home/furqaan-khurram/Documents/ai-wrestling-referee/data/frames_throws'
output_csv = '/home/furqaan-khurram/Documents/ai-wrestling-referee/annotations/move_segments_throws.csv'

frames = sorted(os.listdir(frame_dir))
current_index = 0
start_frame = None
end_frame = None

label_map = {
    '4': '4pt_takedown',
    '2': '2pt_takedown',
    '5': '5pt_takedown',
    't': 'turn',
    'o': 'step_out',
    'n': 'neutral',
}

# Create output CSV and write header if it doesn't exist
if not os.path.exists(output_csv):
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['start_frame', 'end_frame', 'label'])

def save_label(start, end, label):
    with open(output_csv, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([start, end, label])
    print(f"Saved segment: {start} to {end} as {label}")

while True:
    frame_name = frames[current_index]
    frame_path = os.path.join(frame_dir, frame_name)
    frame = cv2.imread(frame_path)
    display_frame = frame.copy()

    instructions = f"[s] start  [e] end  [4/2/5/t/o/n] label  [a/d] prev/next  [ESC] quit"
    frame_num_text = f"Frame {current_index} - {frame_name}"
    cv2.putText(display_frame, instructions, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    cv2.putText(display_frame, frame_num_text, (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 1)

    if start_frame is not None:
        cv2.putText(display_frame, f"Start: {start_frame}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
    if end_frame is not None:
        cv2.putText(display_frame, f"End: {end_frame}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

    cv2.imshow("Labeling Tool", display_frame)
    key = cv2.waitKey(0) & 0xFF

    if key == 27:  # ESC
        break
    elif key == ord('a') and current_index > 0:
        current_index -= 1
    elif key == ord('d') and current_index < len(frames) - 1:
        current_index += 1
    elif key == ord('s'):
        start_frame = int(frames[current_index].split('.')[0].split('_')[-1])
    elif key == ord('e'):
        end_frame = int(frames[current_index].split('.')[0].split('_')[-1])
    elif chr(key) in label_map and start_frame is not None and end_frame is not None:
        label = label_map[chr(key)]
        save_label(start_frame, end_frame, label)
        start_frame, end_frame = None, None
    else:
        print("Unrecognized key or missing start/end")

cv2.destroyAllWindows()
