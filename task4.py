weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

forward_dict = {i + 1: weekdays[i] for i in range(len(weekdays))}
reverse_dict = {day: i + 1 for i, day in enumerate(weekdays)}

print(forward_dict)
print(reverse_dict)
