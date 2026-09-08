import subprocess
reachableHosts = []
unreachableHosts = []
RTT = []

subnetMask = subprocess.run(
            ["ifconfig", "en0"],
            capture_output=True,
            text=True)
for i in subnetMask.stdout.splitlines():
    if "netmask" in i:
        Mask = i.split(" ")[3][2:].count("0")
    else:
        continue

for i in range(1, 16**Mask):
    host = f"192.168.1.{i}"
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-t", "1", host],
            capture_output=True,
            text=True)
        
        RTT.append(float(result.stdout.splitlines()[-1].split("/")[-3]))
        reachableHosts.append(host)
    
    except:
        unreachableHosts.append(host)

    subprocess.run(["clear"])
    print(f"{((i/16**Mask)*100):.2f}% completed")

if len(RTT) != 0:
    RTTAverage = sum(RTT) / len(RTT)
else:
    RTTAverage = 0

subprocess.run(["clear"])
print("Network Reachability Report")
print("---------------------------")
print(f"Hosts Checked: {(len(reachableHosts) + len(unreachableHosts))}")
print(f"Online: {(len(reachableHosts))}")
print(f"Offline: {(len(unreachableHosts))}")
print(f"Average RTT: {RTTAverage:.2f} ms \n")
