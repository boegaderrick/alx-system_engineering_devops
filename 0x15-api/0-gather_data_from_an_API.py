#!/usr/bin/python3
"""
    This script requests an api for workers and all assignments
    and then prints a worker's name and their progress
    It takes a single command-line argument which is the ID of
    the subject worker.
"""
if __name__ == '__main__':

    from json import loads
    from requests import get
    from sys import argv

    users = get('https://jsonplaceholder.typicode.com/users/')
    user = [i for i in loads(users.text) if str(i.get('id')) == argv[1]][0]

    data = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = [i for i in loads(data.text) if str(i['userId']) == argv[1]]
    complete = [i for i in tasks if i.get('completed')]

    total = len(tasks)
    done = len(complete)
    # print(f'Employee {user.get("name")} is done with tasks({done}/{total})')
    print('Employee {} is done with tasks({}/{}):'.format(user.get("name"),
                                                          done, total))
    for i in complete:
        print('\t' + i.get('title'))
