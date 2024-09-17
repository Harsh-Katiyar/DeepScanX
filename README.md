# DeepScanX

**DeepScanX** is an advanced and comprehensive Nmap-based Python tool designed to execute thorough network scans using all available Nmap options and scripts. It guarantees that no detail is overlooked during the scanning process, providing users with real-time feedback and descriptive messages about the actions taken in the background.

## Features

- Supports all Nmap scan options, including service and OS detection.
- Automatically runs all NSE (Nmap Scripting Engine) scripts to detect vulnerabilities, gather information, and more.
- Offers customizable scan profiles to adjust scanning depth (`full`, `quick`, or `custom`).
- Provides real-time, descriptive feedback to the user, detailing each Nmap command being executed in the background.
- Generates detailed and structured scan reports.
- Allows configuration of scan parameters via JSON files for flexibility.

## Requirements

- Python 3.8 or later
- Nmap installed and available in your system's PATH

Install Python dependencies via `pip`:

```bash
pip install -r requirements.txt
