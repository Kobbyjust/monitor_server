import scapy.all as scapy

# List of IP address ranges to scan
ip_ranges = ["192.168.52.0/24", "192.168.53.0/24", "192.168.1.0/24"]

# Initialize lists to store the responses for each IP range
all_ans = []
all_unans = []

# Loop through each IP range and perform ARP scan
for ip_range in ip_ranges:
    ans, unans = scapy.arping(ip_range, verbose=False)
    all_ans.append(ans)
    all_unans.append(unans)

# Print the summary of responses for each IP range
print("Summary of responses for each IP range:")
print("--------")
for ans in all_ans:
    for response in ans.res:
        print(response[1].sprintf("IP: %ARP.psrc%  MAC: %ARP.hwsrc%"))
print("--------")

# Print the summary of unanswered packets for each IP range
print("Summary of unanswered packets for each IP range:")
print("--------")
# for unans in all_unans:
#     for packet in unans:
#         #print(packet.sprintf("Unanswered IP: %ARP.pdst%"))
#         print("N")
print("--------")
