it_staff = {
    'name': {
        'first': 'Robert', 
        'last': 'Anderson'
    },
    'access_roles': [
        'system_admin'
        'network_manager'
    ],
    'clearance_level': 3.5
}

last_name = it_staff['name']['last']
print(f"Last name: {last_name}")

roles = it_staff['access_roles']
print(f"Current roles: {roles}")

it_staff['access_roles'].append('security_analyst')

updated_roles = it_staff['access_roles']
print(f"Updated roles: {updated_roles}")