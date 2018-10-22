def minutes_to_hours(minutes, seconds=0):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(240, 3600), "Hours.")
