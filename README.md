# SSH Extension for Gemini CLI

A simple extension for the Gemini CLI that allows you to execute SSH commands.

## Installation

To install this extension from the local directory, run the following command from the `ssh-extension` directory:

```bash
gemini extensions install .
```

Alternatively, you can install it from GitHub:

```bash
gemini extensions install https://github.com/involvex/gemini-cli-ssh-extension.git
```

## SSH Key

For passwordless authentication, ensure your SSH private key is added to the SSH agent. On Windows, you can do this with `ssh-add`. If your key is not in the default location (`~/.ssh/id_rsa`), you may need to specify the path to your private key.

If you do not have an SSH key, you will be prompted for a password.




## Usage

This extension provides an `ssh` tool to execute remote commands.

### `ssh`

Executes an SSH command.

**Parameters:**

*   `command` (string, required): The SSH command to execute, including the username and host.


