import requests

from repos import get_popular_python_repos


def test_get_popular_repos(requests_mock):
    url = (
        'https://api.github.com/search/repositories'
        '?q=language:python&sort=stars'
    )

    requests_mock.get(
        url,
        json={
            'items': [
                {'name': 'banana-repo', 'stargazers_count': 10000},
                {'name': 'apple-repo', 'stargazers_count': 25}
            ]
        }
    )

    expected = [
        ('banana-repo', 10000),
        ('apple-repo', 25)
    ]

    assert get_popular_python_repos() == expected
