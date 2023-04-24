#!/usr/bin/python3
"""
    This script requests an api for workers and all assignments
    and then exports all workers' progress report in json format
    to a json file.

    It takes a single command-line argument which is the ID of
    the subject worker.
"""
if __name__ == '__main__':

    from json import loads, dump
    from requests import get
    from sys import argv

    users = get('https://jsonplaceholder.typicode.com/users/')
    user_ids = [i.get('id') for i in loads(users.text)]

    data = get('https://jsonplaceholder.typicode.com/todos/')

    final = {}
    for id in user_ids:
        tasks = [i for i in loads(data.text) if i['userId'] == id]
        user = loads(get(f'https://jsonplaceholder.typicode.com/users/{id}').text)
        new = {id: []}
        for i in tasks:
            foo = {}
            foo['username'] = user.get('username')
            foo['task'] = i.get('title')
            foo['completed'] = i.get('completed')
            new[id].append(foo)
        final.update(new)
    with open(f'todo_all_employees.json', mode='w', encoding='utf-8') as f:
        dump(final, f)
