network_devices = ['router_01', 192.168, 'active']
print(len(network_devices))
print(network_devices[0])
print(network_devices[:-1])
additional_divoces = ['switch_01', 'firewall_02']
complete_network = network_devices + additional_divoces
print(complete_network)

log_entries = ['error_01', 'warning_02', 'info_03']
daily_logs = log_entries * 2
print(daily_logs)