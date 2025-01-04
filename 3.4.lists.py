server_metrics = [["CPU_usage", "RAM_usage", "Disk_space"],
                  ["Network_in", "Network_out", "Active_connections"],
                  ["Responce_time", "Error_rate", "Queue_length"]]

resource_metrics = server_metrics[0]
print(resource_metrics)
network_out = server_metrics[1][1]
print(network_out)