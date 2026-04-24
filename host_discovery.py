import time

print("==== HOST DISCOVERY SERVICE ====\n")

hosts = {
    "h1": "10.0.0.1",
    "h2": "10.0.0.2"
}

while True:
    print("Active Hosts:\n")

    for name, ip in hosts.items():
        print(f"{name} -> {ip}")

    print("\n(Hosts are active in Mininet network)")
    print("-----------------------------------\n")

    time.sleep(5)
