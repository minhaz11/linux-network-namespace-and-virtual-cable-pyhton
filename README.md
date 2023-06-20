## Linux Network Namespace Setup

This is a simple Python script that sets up network namespaces and establishes connectivity between them on a Linux operating system. It utilizes the subprocess module to execute various ip commands for creating network namespaces, veth cables, assigning IP addresses, and testing the connection between namespaces.

## Prerequisites

1. Linux operating system
2. Python Installed

## Usage

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the following command:

```
  python namespace.py
```

4. The script will check if the operating system is Linux. If it's not Linux, an error message will be displayed, and the script will exit.

5. Network namespaces thor and loki will be created using the ip netns add command.
6. Two veth cables, veth-thor and veth-loki, will be created using the ip link add command.
7. Each veth cable will be assigned to its respective namespace using the ip link set command.
8. IP addresses 17.0.0.1/24 and 17.0.0.2/24 will be assigned to the veth interfaces in each namespace using the ip addr add command.
9. The veth interfaces will be enabled using the ip link set command.

A ping command will be executed to test the connectivity between the two namespaces.

## Note

Please note that the script requires administrative privileges, so it will prompt for the sudo password when executing the ip commands.

Important: This script assumes you have the necessary permissions and network configuration privileges on your Linux system. Use it at your own risk and ensure you understand the implications before running it.

For more information about network namespaces and the ip command, refer to the Linux documentation.

If you encounter any issues or have questions, please feel free to contact me.
