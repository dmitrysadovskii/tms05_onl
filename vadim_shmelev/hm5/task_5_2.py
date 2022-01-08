like_list = input('Write list of people: ')
like_list = like_list.split()
likes_sum = len(like_list)

if likes_sum == 0:
    print('no one likes this')
elif likes_sum < 2:
    print(f'{like_list[0]} likes this')
elif likes_sum < 3:
    print(f'{like_list[0]} and {like_list[1]} like this')
elif likes_sum < 4:
    print(f'{like_list[0]}, {like_list[1]} and {like_list[2]} like this')
elif likes_sum >= 4:
    likes_sum = likes_sum - 2
    from random import choice
    print(f'{choice(like_list)}, {choice(like_list)} and {likes_sum} other like this')
