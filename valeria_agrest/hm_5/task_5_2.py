array = ['Ann, Tim', 'Alex', 'Katty', 'Paul']


def likes(arr):
    if len(arr) == 0:
        print('no one likes this')
    elif len(arr) == 1:
        print(f'{arr[0]} likes this')
    elif len(arr) == 2:
        print(f'{arr[0]} and {arr[1]} like this')
    elif len(arr) == 3:
        print(f'{arr[0]}, {arr[1]} and {arr[2]} like this')
    elif len(arr) > 3:
        count = len(arr) - 2
        print(f'{arr[0]}, {arr[1]} and {count} others like this')


likes(array)
