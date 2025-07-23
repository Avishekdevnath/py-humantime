from pyhumantime import seconds_to_human, human_to_seconds

print('--- py-humantime sample usage ---')

# Convert seconds to human-readable
print('4523 seconds →', seconds_to_human(4523))  # 1h 15m 23s

# Convert human-readable to seconds
print('"1h 15m 23s" →', human_to_seconds('1h 15m 23s'))  # 4523

# Error handling example
try:
    print(human_to_seconds('notatime'))
except ValueError as e:
    print('Error:', e) 