import subprocess
import datetime
import os

# Step 1: Check for real changes in the Git repo
status_output = subprocess.check_output(["git", "status", "--porcelain"]).decode().strip()

if status_output:
    print("🔧 Uncommitted changes detected. Skipping fake daily commit.")
else:
    print("✅ No real changes. Proceeding with daily keep-alive commit...")

    # Step 2: Append a log entry to force a commit
    with open("daily-log.txt", "a") as f:
        f.write(f"🕐 Daily keep-alive: {datetime.datetime.now()}\n")

    # Step 3: Run Git automation
    os.system("git add daily-log.txt")
    os.system("git commit -m '🔄 Daily auto-commit'")
    os.system("git push origin main")
