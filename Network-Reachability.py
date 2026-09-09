import subprocess
import sys
reachableHosts = []
unreachableHosts = []
RTT = []
AverageRTT = 0

subnetMask = subprocess.run(
            ["ifconfig", "en0"],
            capture_output=True,
            text=True)
for i in subnetMask.stdout.splitlines():
    if "netmask" in i:
        Mask = i.split(" ")[3][2:].count("0")
    else:
        continue

def myFunction(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-t", "1", host],
            capture_output=True,
            text=True)
        
        RTT.append(float(result.stdout.splitlines()[-1].split("/")[-3]))
        reachableHosts.append(host)
    
    except:
        unreachableHosts.append(host)

    return RTT

def myFunction2():
    for i in range(1, (16**Mask)+1):
        host = f"192.168.1.{i}"
        myFunction(host)

        subprocess.run(["clear"])
        print(f"{((i/16**Mask)*100):.2f}% completed")

try:
    if len(sys.argv[1].split(".")) == 4:
        host = sys.argv[1]
        myFunction(host)

    elif sys.argv[1].endswith("txt"):
        file = open(sys.argv[1])
        for i in file.readlines():
            myFunction(i)

    elif sys.argv[1] == "--output":
        myFunction2()

        with open(sys.argv[2], "w") as file:
            file.write("Network Reachability Report\n")
            file.write("---------------------------\n")
            file.write(f"Hosts Checked: {(len(reachableHosts) + len(unreachableHosts))}\n")
            file.write(f"Online: {(len(reachableHosts))}\n")
            file.write(f"Offline: {(len(unreachableHosts))}\n")
            if len(RTT) != 0:
                file.write(f"Average RTT: {sum(RTT)/len(RTT):.2f} ms \n")
            else:
                file.write("Average RTT: 0 ms \n")
            file.write("Reachable Hosts: \n")

            if len(reachableHosts) == 0:
                file.write("None")
            else:
                for i in reachableHosts:
                    file.write("\n" + i)

except:
    myFunction2()

subprocess.run(["clear"])
print("Network Reachability Report")
print("---------------------------")
print(f"Hosts Checked: {(len(reachableHosts) + len(unreachableHosts))}")
print(f"Online: {(len(reachableHosts))}")
print(f"Offline: {(len(unreachableHosts))}")
if len(RTT) != 0:
    print(f"Average RTT: {sum(RTT)/len(RTT):.2f} ms \n")
else:
    print("Average RTT: 0 ms \n")

print("Reachable Hosts: ")

if len(reachableHosts) == 0:
    print("None")
else:
    for i in reachableHosts:
        print(i.strip("\n"))
