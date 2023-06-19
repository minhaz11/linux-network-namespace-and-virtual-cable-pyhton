import subprocess
import platform

# Check if the operating system is Linux
if platform.system() != 'Linux':
    print('Network namespaces are only supported on Linux.')
    exit()

NS1 = "thor"
NS2 = "loki"

IP_NS1 = "17.0.0.1/24"
IP_NS2 = "17.0.0.2/24"

VETH1 = "veth-thor"
VETH2 = "veth-loki"


subprocess.run(['sudo', 'ip', 'netns', 'add', NS1], check=True)
subprocess.run(['sudo', 'ip', 'netns', 'add', NS2], check=True)

# Create two veth cables
subprocess.run(['sudo', 'ip', 'link', 'add', VETH1, 'type', 'veth', 'peer', 'name', VETH2], check=True)

# Assign each veth cable to each namespace
subprocess.run(['sudo', 'ip', 'link', 'set', VETH1, 'netns', NS1], check=True)
subprocess.run(['sudo', 'ip', 'link', 'set', VETH2, 'netns', NS2], check=True)

# Configure/assign IP address of the veth interfaces for each namespace
subprocess.run(['sudo', 'ip', 'netns', 'exec', NS1, 'ip', 'addr', 'add', IP_NS1, 'dev', VETH1], check=True)
subprocess.run(['sudo', 'ip', 'netns', 'exec', NS2, 'ip', 'addr', 'add', IP_NS2, 'dev', VETH2], check=True)

# Now enable/up/activate the veth interfaces/cables
subprocess.run(['sudo', 'ip', 'netns', 'exec', NS1, 'ip', 'link', 'set', VETH1, 'up'], check=True)
subprocess.run(['sudo', 'ip', 'netns', 'exec', NS2, 'ip', 'link', 'set', VETH2, 'up'], check=True)

# Ping to another namespace for testing connection
subprocess.run(['sudo', 'ip', 'netns', 'exec', NS1, 'ping', '17.0.0.2'], check=True)
