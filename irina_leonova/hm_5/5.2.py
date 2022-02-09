who = input("who posted like: ")
people = who.split()
print(people[0])
like = len(people)
likes = like - 2
if like == 0:
    print("no one likes this")
if like == 1:
    print(people[0], "likes this")
if like == 2:
    print(people[0], "and ", people[1], " like this")
if like == 3:
    print(people[0], people[1], " and ", people[2], " like this")
if like >= 4:
    print(people[0], people[1], " and ", likes, "others like this")
