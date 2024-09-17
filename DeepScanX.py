import subprocess
import argparse
import json


def run_command(command):
    """Run a shell command and print real-time output."""
    print(f"Running: {' '.join(command)}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line.decode().strip())
    process.wait()


def load_config(config_file):
    """Load JSON configuration file."""
    with open(config_file, 'r') as file:
        return json.load(file)a


def main():
    parser = argparse.ArgumentParser(description='DeepScanX - Advanced Nmap-based scanning tool')
    parser.add_argument('--target', required=True, help='Target IP, hostname, or network range')
    parser.add_argument('--profile', choices=['full', 'quick', 'custom'], default='quick', help='Select scan profile')
    parser.add_argument('--config', default='config.json', help='Path to config file (optional)')

    args = parser.parse_args()

    # Load configuration from file if necessary
    config = load_config(args.config) if args.config else {}

    # Determine the scan profile
    if args.profile == 'full':
        command = ['nmap', '-A', '-sC', '-p-', args.target]
    elif args.profile == 'quick':
        command = ['nmap', '-T4', args.target]
    else:
        command = ['nmap', '-sV', '-sC', args.target]

    # Show the command that is going to be run
    print(f"\n[INFO] Executing scan with the following command:\n{' '.join(command)}\n")

    # Execute the command
    run_command(command)


if __name__ == "__main__":
    main()
