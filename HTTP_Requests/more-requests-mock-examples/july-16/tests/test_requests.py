from examples import get_google, get_most_popular_py


def test_first_example(requests_mock):
    requests_mock.get(
        'https://www.google.ca',
        text='I am not google'
    )
    response = get_google()
    assert response.text == 'I am not google'

def test_second_example(requests_mock):
    requests_mock.get(
        'https://www.google.ca',
        text='Not found',
        status_code=404
    )
    response = get_google()
    assert response.status_code == 404

def test_third_example(requests_mock):
    requests_mock.get(
        'https://api.github.com/search/repositories?sort=stars&q=language:python',
        json={
            'total_count': 100,
            'items': [
                {'id': 100, 'html_url': 'superman/package1', 'stargazers_count': 100},
                {'id': 101, 'html_url': 'batman/awesome', 'stargazers_count': 99}
            ]
        }
    )
    expected = [
        {'url': 'superman/package1', 'stars': 100},
        {'url': 'batman/awesome', 'stars': 99}
    ]
    result = get_most_popular_py()
    assert result == expected
