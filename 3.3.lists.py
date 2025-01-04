laptop_inventory = ["HP-2021-001", "Dell-2022-002", "Lenovo-2023003"]
tablet_inventory = ["iPad-2023-001", "Surface-2023-002"]
laptop_inventory.append("Mac-2024-004")

primary_inventory = ["HP-2021-001", "Dell-2022-002", "Lenovo-2023003"]
acquired_inventory = ["HP-2023-701", "Dell-2023-892"]
primary_inventory.extend(acquired_inventory)

laptop_inventory.insert(1, "DevServer-2025-001")
laptop_inventory.remove("HP-2021-001")
transferred_device = laptop_inventory.pop()
#print(transferred_device)

acquired_inventory.clear()
#print(acquired_inventory)

laptop_inventory.sort()
laptop_inventory.reverse()
server_position = laptop_inventory.index("DevServer-2025-001")
hp_count = laptop_inventory.count("Dell-2022-002")
print(hp_count)

complete_inventory = laptop_inventory + tablet_inventory
branch_setups = tablet_inventory * 3
total_tablet_inventory = len(tablet_inventory + branch_setups)
print(total_tablet_inventory)