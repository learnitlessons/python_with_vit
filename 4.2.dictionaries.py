meeting_room = dict(
    room='Conference A',
    capacity=20,
    equipment='projector'
)
print(meeting_room)

keys = ['room', 'capacity', 'equipment']
values = ['Conference A', 20, 'projector']
meeting_room = dict(zip(keys, values))
room1 = meeting_room['room']
print(room1)