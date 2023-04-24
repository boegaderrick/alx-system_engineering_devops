#!/usr/bin/python3
"""
    This script requests an api for workers and all assignments
    and then exports the specified worker's progress report (i.e
    userid, username, completion status and title of the project)
    in csv format to a csv file.

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

    string = ''
    for i in tasks:
        userId = i.get('userId')
        name = user.get('username')
        proj_status = i.get('completed')
        proj_title = i.get('title')
        string += f'"{userId}","{name}","{proj_status}","{proj_title}"' + '\n'
    string = string[:-1]
    with open(f'{argv[1]}.csv', mode='w', encoding='utf-8') as f:
        f.write(string + '\n')
