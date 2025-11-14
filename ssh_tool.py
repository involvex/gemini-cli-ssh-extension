import subprocess
import sys
import shlex

def ssh(command):
  """Executes an SSH command."""
  try:
    # We need to handle the command carefully, especially on Windows.
    # Use shlex to properly parse the command with quotes.
    # Add default options for full access: disable host key checking and known hosts
    import os
    null_device = "NUL" if os.name == 'nt' else "/dev/null"
    default_options = ["-o", "StrictHostKeyChecking=no", "-o", f"UserKnownHostsFile={null_device}"]
    full_command = ["ssh"] + default_options + shlex.split(command)
    process = subprocess.Popen(
        full_command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
      return f"Error: {stderr}"
    return stdout
  except Exception as e:
    return f"An error occurred: {e}"

if __name__ == "__main__":
  # This allows running the script directly for testing.
  if len(sys.argv) > 1:
    command_to_run = " ".join(sys.argv[1:])
    result = ssh(command_to_run)
    print(result)
  else:
    print("Usage: python ssh_tool.py <ssh_command>")
