# SSH Extension for Gemini CLI (v2.1)

This extension provides a robust `/ssh` command for interacting with remote servers, enabling secure command execution directly from the Gemini CLI.

It uses the `paramiko` Python library, ensuring reliable and secure connections.

## Features

-   **Simplified Command:** A single `/ssh` command for all remote execution.
-   **Standard SSH Syntax:** Uses familiar `user@hostname "command"` syntax.
-   **Secure Connections:** Leverages the `paramiko` library and your local SSH agent for authentication.
-   **Detailed Output:** Returns `stdout`, `stderr`, and the `exit_code` for every command.

## Installation

1.  **Prerequisites:** Ensure you have Python and `pip` installed.
2.  **Install Dependencies:** From within this extension's directory, run:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install the Extension:** Run the following command from the extension's directory:
    ```bash
    gemini extensions install .
    ```
4.  **Restart Gemini CLI:** **This is a critical step.** Close and reopen the Gemini CLI to ensure the new `/ssh` command is registered.

## Usage

The extension provides a single `ssh` tool that can be used like a command.

### `ssh`

Executes a shell command on a remote host. The arguments should be a single string in the format `user@hostname "command"`.

**Example:**
```
/ssh args='bitnami@63.178.255.78 "df -h"'
```
