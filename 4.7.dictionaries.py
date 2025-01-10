it_inventory = {
    "LAP001": {
        "type": "Laptop",
        "model": "ThinkPad X1",
        "status": "In Use",
        "assigned_to": "Sarah Chen",
        "department": "Development",
        "location": "Floor 2",
        "purchase_info": {
            "date": "2023-05-15",
            "cost": 1299.99,
            "supplier": "TechVendor Inc"
        },
        "maintenance": {
            "last_check": "2024-01-10",
            "next_check": "2024-04-10",
            "condition": "Excellent"
        }
    },
    "MON002": {
        "type": "Monitor",
        "model": "Dell U2419H",
        "status": "Available",
        "location": "Storage Room",
        "purchase_info": {
            "date": "2023-06-20",
            "cost": 249.99,
            "supplier": "Office Solutions Ltd"
        },
        "maintenance": {
            "last_check": "2024-01-15",
            "next_check": "2024-04-15",
            "condition": "Good"
        }
    }
}

# Basic usage of get() to retrieve equipment status
# laptop_status = it_inventory.get("LAP001", "Not Found")
# printer_status = it_inventory.get ("PRN001", "Not Found")

# print(laptop_status)
# print(printer_status)

# laptop_location = it_inventory.get("LAP001", {}).get("location", "Location Unknown")
# laptop_maintenance = it_inventory.get("LAP001", {}).get("maintenance", {}).get("last_check", "No Record")

# assigned_employee = it_inventory.get("LAP001", {}).get("locaction", "Location Unknown")
# department = it_inventory.get("LAP001", {}).get("department", "No Department")

# print(f"Equipment assigned to: {assigned_employee}")
# print(f"Department: {department}")

# Basic iteration through inventory items
# for asset_id, asset_info in it_inventory.items():
#     print(f"Asset ID: {asset_id}")
#     print(f"Equipment Type: {asset_info['type']}")
#     print(f"Current Status: {asset_info['status']}")
#     print("-" * 30)

# print("Current Equipment Status Report:")
# for asset_id, asset_info in it_inventory.items():
#     location = asset_info['location']
#     status = asset_info['status']
#     model = asset_info['model']
#     print(f"{asset_id}: {model} - Located in {location} - Status: {status}")

# print("\nMaintenance Summary:")
# for asset_id, asset_info in it_inventory.items():
#     last_check = asset_info['maintenance']['last_check']
#     condition = asset_info["maintenance"]['condition']
#     print(f"{asset_id} - Last Check: {last_check}, Condition: {condition}")

# Getting all asset IDs in the inventory
# asset_ids = it_inventory.keys()
# print("Available Asset IDs:", asset_ids)

# for asset_id in it_inventory.keys():
#     if asset_id.startswith("LAP"):
#         print(f"Found laptop: {asset_id}")
#     elif asset_id.startswith("MON"):
#         print(f"Found monitor: {asset_id}")

# laptop_count = 0
# monitor_count = 0

# for asset_id in it_inventory.keys():
#     if asset_id.startswith("LAP"):
#         laptop_count += 1
#     elif asset_id.startswith("MON"):
#         monitor_count += 1

# print(f"Total Laptops: {laptop_count}")
# print(f"Total Monitors: {monitor_count}")

# if "LAP001" in it_inventory.keys():
#     print("Laptop LAP001 is in inventory")

# Getting all equipment details
# all_equipment = it_inventory.values()

# print("Current Status Report:")
# for equipment in it_inventory.values():
#     print(f"Type: {equipment['type']}")
#     print(f"Model: {equipment['model']}")
#     print(f"Status: {equipment['status']}")
#     print(f"Location: {equipment['location']}")
#     print("-" * 30)

# print("\nEquipment by Location:")
# for equipment in it_inventory.values():
#     if equipment['location'] == "Floor 2":
#         print(f"{equipment['type']} - {equipment['model']}")

# print("\nMaintenance Overview: ")
# for equipment in it_inventory.values():
#     print(f"{equipment['type']}: {equipment['maintenance']['condition']}")

# Updating existing equipment information
# Making a copy of our original dictionary 
# demo_inventory = it_inventory.copy()

# print("BEFORE UPDATE:")
# print(f"Status {demo_inventory['LAP001']['status']}")
# print(f"Location: {demo_inventory}['LAP001]['location']")
# print(f"Last maintenance: {demo_inventory}['LAP001']['maintenance']['last_check']")
# print("-" * 30)


# demo_inventory["LAP001"].update({
#     "status": "Under Maintenance",
#     "location": "IT Department",
#     "maintenance": {
#         "last_check": "2024-01-07",
#         "next_check": "2025-01-07",
#         "condition": "Needs Repair"
#     }
# })

# print("\nAFTER UPDATE:")
# print(f"Status: {demo_inventory}")
# print(f"Status {demo_inventory['LAP001']['status']}")
# print(f"Location: {demo_inventory}['LAP001]['location']")
# print(f"Last maintenance: {demo_inventory}['LAP001']['maintenance']['last_check']")
# print("-" * 30)

# Using copy() and popitem() methods
# demo_inventory = it_inventory.copy()

# print("Initial inventory size:", len(demo_inventory))

# demo_inventory["KBD001"] = {
#     "type": "Keyboard",
#     "model": "Logitech MX Keys",
#     "status": "New",
#     "location": "IT Storage"
# }

# print("\nAfter adding new item:")
# print("Inventory size:", len(demo_inventory))

# last_item_id, last_item_details = demo_inventory.popitem()
# print("\nLast added item removed:")
# print(f"Asset ID: {last_item_id}")
# print(f"Type: {last_item_details['type']}")
# print(f"Model: {last_item_details['model']}")

# print("\nRemaining inventory size:", len(demo_inventory))

# empty_inventory = {}
# try:
#     empty_inventory.popitem()
# except KeyError:
#     print("\nCannot popitem() from empty inventory")

# empty_inventory = {}
# try:
#     empty_inventory.popitem()
# except KeyError:
#     print("\nCannot popitem() from empty inventory")

# empty_inventory = {}
# empty_inventory.popitem()

# Set default values for existing and non-existing fields
# demo_inventory = it_inventory.copy()

# print("Working with LAP001:")

# status = demo_inventory["LAP001"].setdefault("status", "Unknown")
# print(f"Existing status: {status}")

# notes = demo_inventory["LAP001"].setdefault("notes", "No additional information")
# print(f"New field 'notes': {notes}")

# print("\nWorking with MON002:")
# service_tag = demo_inventory["MON002"].setdefault("service_tag", "Not registered")
# warranty_status = demo_inventory["MON002"].setdefault("warranty_status", "Unknown")
# print(f"Sevice Tag: {service_tag}")
# print(f"Warrenty Status: {warranty_status}")

# print("\nUpdated MON002 record:")
# for key, value in demo_inventory["MON002"].items():
#     print(f"{key}: {value}")

# default_structure = {
#     "type": "Not Specified",
#     "model": "Not Specified",
#     "status": "Pending",
#     "location": "IT Storage",
#     "maintenance": {
#         "last_check": 'None',
#         "next_check": "To be Scheduled",
#         "condition": "Not Checked"
#     }
# }

# new_laptop_ids = ["LAP003","LAP004","LAP005" ]
# new_laptops = dict.fromkeys(new_laptop_ids, default_structure)

# print("Newly created inventory entries:")
# for laptop_id, details in new_laptops.items():
#     print(f"\nAsset ID: {laptop_id}")
#     print(f"Status: {details['status']}")
#     print(f"Location: {details['location']}")
#     print(f"Maintenance Status: {details['maintenance']['condition']}")

# print("\nCaution with shared references:")
# new_laptops["LAP003"]["status"] = "In Use"
# print(f"LAP003 status: {new_laptops['LAP003']['status']}")
# print(f"LAP004 status: {new_laptops['LAP004']['status']}")

# new_laptop_correct = {id: default_structure.copy() for id in new_laptop_ids}

demo_invetory = it_inventory.copy()

print("Intial inventory contents:")
for asset_id in demo_invetory.keys():
    print(f"Asset: {asset_id}")

print(f"\nIntial inventory size: {len(demo_invetory)}")

print("\nClearing inventory...")
demo_invetory.clear()

print(f"Invetory size after clear: {len(demo_invetory)}")
print(f"Inventory contents: {demo_invetory}")

demo_invetory["NEW001"] = {
    "type": "Laptop",
    "status": "New"
}