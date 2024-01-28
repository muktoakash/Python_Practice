import requests

def get_google():
    return requests.get('https://www.google.ca')


def get_most_popular_py():
    response = requests.get('https://api.github.com/search/repositories?sort=stars&q=language:python')
    data = response.json()
    return [
        {'url': repo['html_url'], 'stars': repo['stargazers_count']}
        for repo in data['items']
    ]
