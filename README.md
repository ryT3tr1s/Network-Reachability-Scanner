# Network Reachability Scanner
A python based tool that scans a subnet using ICMP echo requests, identifies reachable and unreachable hosts, calculates average RTT for responding hosts, and generates a terminal-based reachability report.

# Skills Demonstrated
- Python
- Network Diagnostics
- ICMP/Ping
- Subprocess Management
- File Parsing
- Network Troubleshooting
- Automation Scripting

# Usage 
To scan a single host: 
    ``python3 network_monitor.py 192.168.1.20``
    
To scan a list of hosts from a file: 
    ``python3 network_monitor.py hosts.txt``

To output the report to a file: 
    ``python3 network_monitor.py --output Network_Reachability_Report_09-09-2026.txt``

To scan the entire network:
    ``python3 network_monitor.py``

# Output
![imagealt](https://github.com/ryT3tr1s/Network-Reachability-Scanner/blob/7d2423c984e6db0aaaf0d84f8dcc676588ea2d3a/Network-Reachability-Scanner.png)

<h3>Applies to: MacOS</h3>
  
