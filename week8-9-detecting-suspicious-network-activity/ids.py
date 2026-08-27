from collections import Counter

simulated_packets = [
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.20",
    "192.168.1.20",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
    "192.168.1.150",
]

THRESHOLD = 20


def run_ids():
  print("Analyzing simulated network packets...")

  packet_counts = Counter(simulated_packets)

  print("Packet counts per source IP:")
  for ip, count in packet_counts.items():
    print(f"- {ip}: {count} packets")

  print("\nChecking for suspicious activity...")
  for ip, count in packet_counts.items():
    if count > THRESHOLD:
      print(
          f"!!! ALERT: Suspicious activity detected from {ip}. Packets sent:"
          f" {count}"
      )


if __name__ == "__main__":
  run_ids()