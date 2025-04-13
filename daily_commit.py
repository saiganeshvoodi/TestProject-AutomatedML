import subprocess
import datetime
import os

# Step 1: Get today's date
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Step 2: Check if there is any commit made today
try:
    log_output = subprocess.check_output(
        ["git", "log", "--since=midnight", "--pretty=format:%cd", "--date=short"]
    ).decode().strip()
except subprocess.CalledProcessError:
    log_output = ""

if today in log_output:
    print("📅 A commit was already made today. Skipping daily keep-alive commit.")
else:
    print("✅ No commit yet today. Proceeding with daily keep-alive commit...")

    # Step 3: Append a log entry to force a commit
    with open("daily-log.txt", "a") as f:
        f.write(f"🕐 Daily keep-alive: {datetime.datetime.now()}\n")

    # Step 4: Run Git automation
    os.system("git add daily-log.txt")
    os.system("git commit -m '🔄 Daily auto-commit'")
    os.system("git push origin main")
