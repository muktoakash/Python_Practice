import requests


def get_popular_python_repos():
    """
    Returns list of most popular Python repos.
    """
    url = (
        'https://api.github.com/search/repositories'
        '?q=language:python&sort=stars'
    )
    response = requests.get(url)
    data = response.json()

    return [
        (item['name'], item['stargazers_count'])
        for item in data['items']
    ]
