import csv
import matplotlib.pyplot as plt

# 📌 Path to your cumulative scoring log
scoring_log_file = '../logs/scoring_log.csv'

frames = []
red_scores = []
blue_scores = []

# 📌 Read the scoring_log.csv
with open(scoring_log_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        frames.append(int(row['frame']))
        red_scores.append(int(row['red_score']))
        blue_scores.append(int(row['blue_score']))

# 📌 Plotting
plt.figure(figsize=(12, 6))
plt.plot(frames, red_scores, label='Red Score', color='red')
plt.plot(frames, blue_scores, label='Blue Score', color='blue')

plt.title('Cumulative Scoring Timeline')
plt.xlabel('Frame Number')
plt.ylabel('Cumulative Score')
plt.legend()
plt.grid(True)
plt.tight_layout()

# 📌 Save the plot to logs folder
plt.savefig('../logs/scoring_timeline_cumulative.png')
print("✅ Plot saved to ../logs/scoring_timeline_cumulative.png")
