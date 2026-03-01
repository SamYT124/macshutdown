import subprocess

def shutdown(minutes):
    alert_script = f'display alert "Shutdown Scheduled" message "This Mac will shut down in {minutes} minute(s). Please save your work." as informational'
    shutdown_command = ["sudo", "shutdown", "-h", f"+{minutes}"]
    
    try:
        subprocess.run(["osascript", "-e", alert_script])
        subprocess.run(shutdown_command, check=True)
        print(f"Shutdown scheduled in {minutes} minute(s).")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

shutdown(1)