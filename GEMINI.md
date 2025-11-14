# SSH Extension (v2.1)

This extension provides a robust tool for executing remote commands over SSH using the `paramiko` Python library.

## Authentication

Authentication is handled by the user's local SSH configuration and agent. For best results, ensure your SSH keys are added to your SSH agent. The tool will also respect the `$SSH_KEY_PATH` and `$SSH_PASSWORD` environment variables.

## Available Tools

### `ssh`

-   **Description:** Executes a command on a remote host.
-   **Usage:** The `args` parameter should contain the full command-line string for the SSH connection, in the format `user@hostname "command to run"`.
-   **Example:** `ssh(args='bitnami@123.45.67.89 "ls -la /home/bitnami"')`
