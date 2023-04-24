#!/usr/bin/python3
"""
    This script requests an api for workers and all assignments
    and then exports the specified worker's progress report in
    json format to a json file.

    It takes a single command-line argument which is the ID of
    the subject worker.
"""
if __name__ == '__main__':

    from json import loads, dump
    from requests import get
    from sys import argv

    users = get('https://jsonplaceholder.typicode.com/users/')
    user = [i for i in loads(users.text) if str(i.get('id')) == argv[1]][0]

    data = get('https://jsonplaceholder.typicode.com/todos/')
    tasks = [i for i in loads(data.text) if str(i['userId']) == argv[1]]

    new = {argv[1]: []}
    for i in tasks:
        foo = {}
        foo['task'] = i.get('title')
        foo['completed'] = i.get('completed')
        foo['username'] = user.get('username')
        new[argv[1]].append(foo)
    with open(f'{argv[1]}.json', mode='w', encoding='utf-8') as f:
        dump(new, f)
    #    f.write(new)
