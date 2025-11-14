import os
import sys
import json
import paramiko
import shlex

def _get_ssh_client(hostname, port, username, password=None, key_filename=None):
    """Creates and connects an SSH client."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Environment variable fallbacks
    key_filename = key_filename or os.getenv('SSH_KEY_PATH')
    password = password or os.getenv('SSH_PASSWORD')
    
    try:
        if key_filename:
            key_path = os.path.expanduser(key_filename)
            if not os.path.exists(key_path):
                raise FileNotFoundError(f"SSH key file not found at {key_path}")
            client.connect(hostname, port=port, username=username, key_filename=key_path)
        elif password:
            client.connect(hostname, port=port, username=username, password=password)
        else:
            client.connect(hostname, port=port, username=username, allow_agent=True, look_for_keys=True)
        return client
    except Exception as e:
        raise ConnectionError(f"SSH connection failed: {e}")

def execute_ssh_command(args):
    """Parses ssh arguments and executes the command."""
    try:
        # A simple parser for 'user@host command'
        parts = shlex.split(args)
        
        user_host = parts[0]
        command = " ".join(parts[1:])

        if '@' not in user_host:
            raise ValueError("Invalid format. Expected 'user@hostname'.")

        username, hostname = user_host.split('@', 1)
        
        port = int(os.getenv('SSH_PORT', 22))

        client = _get_ssh_client(hostname, port, username)
        
        stdin, stdout, stderr = client.exec_command(command)
        exit_code = stdout.channel.recv_exit_status()
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        client.close()
        
        return {
            "exit_code": exit_code,
            "stdout": output,
            "stderr": error
        }

    except Exception as e:
        return {"error": f"Failed to execute command: {str(e)}"}

if __name__ == "__main__":
    try:
        input_data = json.load(sys.stdin)
        tool_name = input_data.get("tool_name")
        params = input_data.get("parameters", {})

        if tool_name == "ssh":
            ssh_args = params.get("args")
            if not ssh_args:
                raise ValueError("No args provided for SSH command.")
            result = execute_ssh_command(ssh_args)
        else:
            result = {"error": f"Unknown or unsupported tool: {tool_name}"}

    except Exception as e:
        result = {"error": str(e)}

    print(json.dumps(result))
