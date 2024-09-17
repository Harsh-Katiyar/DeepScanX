import nmap
import os
import time


# Function to run the comprehensive Nmap scan
def run_nmap_scan(target):
    nm = nmap.PortScanner()  # Initialize the Nmap scanner

    # Create output directory for results
    output_dir = "./nmap_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Output filename with timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_file_base = os.path.join(output_dir, f"nmap-{target}-{timestamp}")

    # Informing user about the scan type
    print("\n[INFO] Starting a comprehensive Nmap scan with all available options and scripts.\n")
    print("[INFO] This scan may take a long time depending on the target's network size, firewalls, and performance.\n")

    # Explaining the options that will be used
    print(f"Example: Scanning {target} with the following settings:\n")
    print(
        "1. SYN, UDP, ACK, Window, and Maimon scans\n"
        "2. Operating System detection, version detection, traceroute, and script scanning\n"
        "3. Top 65535 ports, including fast scans of well-known ports\n"
        "4. Execution of default, safe, and vulnerability detection NSE scripts\n"
        "5. Firewall evasion techniques, such as packet fragmentation\n"
        "6. High-performance tweaks like parallelism and rate-limiting adjustments\n"
    )

    # Build the Nmap command with detailed options
    nmap_command = (
        f"-sS -sT -sU -sA -sW -sM "
        f"-O -A -T4 -v -Pn "
        f"--max-retries 10 --version-all --osscan-guess --max-os-tries 9 "
        f"-F --top-ports 65535 "
        f"--script 'default,safe,vuln,auth,discovery,external,malware' "
        f"--script-args=all "
        f"--data-length 200 "
        f"--mtu 32 "
        f"--max-rate 10000 --min-rate 5000 "
        f"--min-hostgroup 64 --max-hostgroup 256 "
        f"--min-parallelism 128 --max-parallelism 256 "
        f"--packet-trace --reason --traceroute --append-output "
        f"--iflist --resume --exclude 127.0.0.1 "
        f"-p- -oA {output_file_base} {target}"
    )

    # Display the command that will be run
    print(f"\n[INFO] Running Nmap with the following command:\n")
    print(f"nmap {nmap_command}\n")

    # Running the Nmap scan with the command line options
    print(f"[INFO] Nmap scan initiated on target: {target}\n")
    nm.scan(hosts=target, arguments=nmap_command)

    # Output results in multiple formats
    print(f"[INFO] Nmap scan completed on {target}. Check output in {output_dir}\n")

    # Optional: Process XML to HTML
    xml_output = f"{output_file_base}.xml"
    html_output = f"{output_file_base}.html"
    os.system(f"xsltproc {xml_output} -o {html_output}")
    print(f"[INFO] HTML report generated: {html_output}\n")


if __name__ == "__main__":
    # Provide the user with detailed help and examples
    print("Welcome to the Enhanced Nmap Scanner!\n")
    print("This tool performs an advanced Nmap scan using all options and scripts available.\n")
    print("Example: To scan the target 'scanme.nmap.org', you would input 'scanme.nmap.org' as the target.")
    print("Example: To scan a specific IP, you would input '192.168.1.1' as the target.\n")

    # Take target input from user
    target = input("Enter the target IP or domain to scan: ")

    # Validate the input and proceed
    if not target:
        print("[ERROR] Target IP/domain is required! Please enter a valid target.")
    else:
        print(f"\n[INFO] You have entered '{target}' as the target. Proceeding with the scan...\n")
        run_nmap_scan(target)
