user_data = {'name': 'Alex', 'department': 'IT', 'access_level': 3}

#user_data['location']

if 'health_insurance' in user_data:
    process_insurance(user_data['health_insurance'])

clearance = user_data.get('security_level', 'basic')

bonus_elegible = user_data['status'] if 'status' in user_data else 'contractor'