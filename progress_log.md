# Progress Log - AI Wrestling Referee Project

## Day 1 - 2025-06-25

- Set up Python + OpenCV environment
- Downloaded wrestling match video
- Extracted 3,228 frames successfully
- Next: Start labeling moves and build move classifier (Day 2)

## Day 2 – 2025-06-26

- Replaced frame-by-frame labeling with a segment-based labeling tool (`label_tool_segment.py`)
- Tool allows marking:
  - `s` = start frame
  - `e` = end frame
  - `2`, `4`, `5`, `t`, `o`, `n` = move labels (`2pt_takedown`, `4pt_takedown`, etc.)
- Labeled multiple match videos:
  - `move_segments_day1.csv`
  - `move_segments_day2.csv`
  - `move_segments_throws.csv`
- Collected a clean and diverse dataset:
  - Many `turn`s and `step_out`s
  - A few `2pt_takedown`s
  - Plenty of `4pt` and `5pt` throws from highlight videos
- Deferred wrestler (Red/Blue) assignment for now — will add during scoring simulation
- Dataset is now ready for move detection, scoring logic, and SystemVerilog design

## Day 3 – 2025-06-27

- Wrote `scoring_simulator.py` to parse labeled segments
- Generated per-frame scoring log in `logs/scoring_log.csv`
- Wrote `plot_scoring_timeline.py` to visualize scoring over time
- Validated scoring events match labeled move segments
- Noticed event log resets to 0 between moves (needs cumulative scoring later)
- Next: Fix cumulative scoring, add Red/Blue labels, start SystemVerilog scoring module
