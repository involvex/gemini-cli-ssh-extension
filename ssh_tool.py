import subprocess
import sys
import shlex
import json

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
      return {"error": stderr}
    return {"output": stdout}
  except Exception as e:
    return {"error": f"An error occurred: {e}"}

if __name__ == "__main__":
  # Read the JSON input from stdin
  try:
    input_json = json.load(sys.stdin)
    command_to_run = input_json.get("command")
    if command_to_run:
      result = ssh(command_to_run)
      # Print the result as a JSON object to stdout
      json.dump(result, sys.stdout)
    else:
      json.dump({"error": "No command provided in the JSON input."}, sys.stdout)
  except json.JSONDecodeError:
    # Fallback for direct testing
    if len(sys.argv) > 1:
      command_to_run = " ".join(sys.argv[1:])
      result = ssh(command_to_run)
      print(json.dumps(result))
    else:
      print(json.dumps({"error": "Usage: python ssh_tool.py <ssh_command> or pipe JSON with a 'command' key."}))