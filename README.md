# System Metrics Monitoring Script

This script monitors system metrics in real time, including CPU, memory, and disk usage. It provides options to visualize the metrics, save them as a CSV file, or generate a video animation of the metrics over time.

## Features
- Monitor CPU, memory, and disk usage in real time.
- Save metrics to a CSV file for later analysis.
- Generate a video animation of the metrics.
- Configure the monitoring interval and output format.

## Requirements
- Python 3.6+
- Required Python Libraries:
  - `psutil`
  - `matplotlib`
  - `pandas`
- FFmpeg (for saving video animations)

## Installation
1. Clone the repository or copy the script to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install psutil matplotlib pandas
   ```
3. Ensure FFmpeg is installed:
   ```bash
   sudo apt-get install ffmpeg
   ```

## Usage
Run the script with optional arguments to customize its behavior.

### Command-Line Arguments
- `--interval <milliseconds>`: Set the monitoring interval (default: `1000` ms).
- `--save_video`: Save a video animation of the metrics.

### Examples
1. Monitor metrics with the default interval:
   ```bash
   python3 python.py
   ```

2. Monitor metrics with a 2-second interval:
   ```bash
   python3 python.py --interval 2000
   ```

3. Save a video animation of the metrics:
   ```bash
   python3 python.py --save_video
   ```

4. Combine interval adjustment and video saving:
   ```bash
   python3 python.py --interval 500 --save_video
   ```

## Outputs
1. **CSV File:**
   - The script saves metrics to `system_metrics.csv` when terminated.
   - Columns:
     - `Timestamp`: The time the metric was recorded.
     - `CPU_Usage (%)`
     - `Memory_Usage (%)`
     - `Disk_Usage (%)`

2. **Video Animation:**
   - If `--save_video` is used, the animation is saved as `system_metrics_animation.mp4`.

3. **Real-Time Plot:**
   - The script displays a live plot of system metrics (if a GUI environment is available).

## Notes
- If running in a non-GUI environment, the plot may not display. Use the `--save_video` option to generate a video instead.
- Ensure FFmpeg is properly installed and configured for video generation.

## Troubleshooting
1. **Error: "FigureCanvasAgg is non-interactive":**
   - This error occurs in non-GUI environments. Use the `--save_video` option or modify the script to save plots as images.

2. **Error: "Command '['ffmpeg'...] returned non-zero exit status 255":**
   - Ensure FFmpeg is installed correctly and accessible via the terminal.

3. **No Animation or CSV Output:**
   - Check if the script was interrupted before saving outputs.
   - Ensure write permissions for the output directory.



