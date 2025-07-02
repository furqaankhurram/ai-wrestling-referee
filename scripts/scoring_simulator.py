import csv
import os
from collections import defaultdict
import random

# 📌 List of your annotation CSV files
csv_files = [
    '../annotations/move_segments_day1.csv',
    '../annotations/move_segments_day2.csv',
    '../annotations/move_segments_throws.csv',
]

# 📌 For now: assign Red/Blue randomly
wrestlers = ['red', 'blue']

# 📌 Define scoring rules
points = {
    '2pt_takedown': 2,
    '4pt_takedown': 4,
    '5pt_takedown': 5,
    'turn': 2,
    'step_out': 1,
    'neutral': 0
}

# 📌 Store running scores per frame
frame_scores = defaultdict(lambda: {'red': 0, 'blue': 0})
segment_log = []

# 📌 Process each CSV
for csv_file in csv_files:
    if not os.path.exists(csv_file):
        print(f"File not found: {csv_file}")
        continue

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            start = int(row['start_frame'])
            end = int(row['end_frame'])
            label = row['label']
            wrestler = row.get('wrestler')

            if wrestler not in ['red', 'blue']:
                wrestler = random.choice(wrestlers)

            score = points.get(label, 0)

            for frame in range(start, end + 1):
                frame_scores[frame][wrestler] += score

            segment_log.append({
                'start': start,
                'end': end,
                'label': label,
                'points': score,
                'wrestler': wrestler
            })

# 📌 Write scoring log
output_dir = '../logs'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'scoring_log.csv')

# 📌 Build cumulative score timeline
all_frames = sorted(frame_scores.keys())
if not all_frames:
    print("No scoring events found!")
    exit()

min_frame = min(all_frames)
max_frame = max(all_frames)

red_total = 0
blue_total = 0

with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['frame', 'red_score', 'blue_score'])

    for frame in range(min_frame, max_frame + 1):
        # Add points if this frame had an event
        red_total += frame_scores[frame]['red']
        blue_total += frame_scores[frame]['blue']

        writer.writerow([frame, red_total, blue_total])


print(f"✅ Scoring log written to: {output_file}")
