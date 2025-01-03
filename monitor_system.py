import argparse
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import pandas as pd
import os
import signal
import time

# Initialize data storage for CSV
data = {
    "Timestamp": [],
    "CPU_Usage (%)": [],
    "Memory_Usage (%)": [],
    "Disk_Usage (%)": []
}

# Initialize figure for plotting
fig, ax = plt.subplots()
cpu_usage = []
memory_usage = []
disk_usage = []
timestamps = []

# Function to collect system metrics
def get_metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, memory, disk

# Update function for the animation
def update(frame):
    global data
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu, memory, disk = get_metrics()

    # Append data for plotting
    timestamps.append(timestamp)
    cpu_usage.append(cpu)
    memory_usage.append(memory)
    disk_usage.append(disk)

    # Keep last 20 records for real-time display
    if len(timestamps) > 20:
        timestamps.pop(0)
        cpu_usage.pop(0)
        memory_usage.pop(0)
        disk_usage.pop(0)

    # Update data for CSV
    data["Timestamp"].append(timestamp)
    data["CPU_Usage (%)"].append(cpu)
    data["Memory_Usage (%)"].append(memory)
    data["Disk_Usage (%)"].append(disk)

    # Clear and replot
    ax.clear()
    ax.plot(timestamps, cpu_usage, label='CPU Usage (%)', color='r')
    ax.plot(timestamps, memory_usage, label='Memory Usage (%)', color='g')
    ax.plot(timestamps, disk_usage, label='Disk Usage (%)', color='b')
    ax.legend(loc='upper left')
    ax.set_title("System Metrics in Real Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Usage (%)")
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()

# Save metrics to CSV
def save_to_csv():
    df = pd.DataFrame(data)
    df.to_csv('system_metrics.csv', index=False)
    print("Metrics saved to system_metrics.csv")

# Handle script termination gracefully
def handle_exit(signal_received, frame):
    print("\nTerminating script...")
    save_to_csv()
    plt.close('all')
    exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, handle_exit)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Monitor system metrics in real-time.")
parser.add_argument('--interval', type=int, default=1000, help="Monitoring interval in milliseconds (default: 1000ms)")
parser.add_argument('--save_video', action='store_true', help="Save the animation as a video file")
args = parser.parse_args()

# Adjust frame rate for video
frame_rate = max(1, 1000 // args.interval)

# Create animation with the user-defined interval
ani = FuncAnimation(fig, update, interval=args.interval, cache_frame_data=False)

if args.save_video:
    try:
        ani.save('system_metrics_animation.mp4', writer='ffmpeg', fps=frame_rate)
        print("Animation saved as system_metrics_animation.mp4")
    except Exception as e:
        print(f"Failed to save animation: {e}")

# Show the plot (requires GUI setup if using WSL or headless servers)
try:
    plt.show()
except Exception as e:
    print(f"Unable to show plot: {e}")

