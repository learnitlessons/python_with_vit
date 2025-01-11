employee_record = ('John Smith', 'IT', 45000)
date_components = (2025, 1, 10)

project_phases = ('Planning', 'Development', 'Testing', 'Deployment')
print(len(project_phases))
combined_phases = project_phases + ('Maintenance',)
current_phase = project_phases[0]
print(combined_phases)
print(current_phase)

server_status = ('active', 'inactive', 'active,' 'maintenance')
active_status = server_status.count('active')
inactive_position = server_status.index('inactive')

config_setting = ('debug_mode', 'test_server', 'logging_enabled')
config_setting[0] = 'release_mode' # TypeError: tuple doesn't support item assignment

system_info = ('Production Server', 2.5, ['CPU', 'Memory', 'Disk'])
resource_group = system_info[2][1]

db_config = ('localhost', 5432, 'userdb', 'admin')
host, port, datadase, user = db_config