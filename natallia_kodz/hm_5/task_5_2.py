def likes(watcher: list):
    if len(watcher) == 0:
        return "no one likes this"
    elif len(watcher) == 1:
        return f"{watcher[0]} likes this"
    elif len(watcher) == 2:
        return f"{watcher[0]} and {watcher[1]} like this"
    elif len(watcher) == 3:
        return f"{watcher[0]}, {watcher[1]} and {watcher[2]} like this"
    else:
        watcher_count = len(watcher) - 2
        return f"{watcher[0]}, {watcher[1]} and {watcher_count} others like " \
               f"this"


users = input("Enter watchers list: ")
users_list = users.split()
print(likes(users_list))
