song_durations_min = [3.5, 2.8, 4.2, 3.0]
durations_sec = list(map(lambda minutes: int(minutes * 60), song_durations_min))
print("pro3 - Durations in seconds:", durations_sec)