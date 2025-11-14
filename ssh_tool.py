import subprocess
import sys

def ssh(command):
  """Executes an SSH command."""
  try:
    # We need to handle the command carefully, especially on Windows.
    # We'll split the command into a list of arguments.
    full_command = ["ssh"] + command.split()
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
