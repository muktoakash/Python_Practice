# coding: utf-8
import requests
response = requests.get('https://www.google.ca') 
response
response.status_code
response.reason
response = requests.get('https://www.google.ca/sdofkjsdlfksjdf') 
response
response.reason
response.headers
response = requests.get('https://www.google.ca') 
response.headers
response.content
response = requests.get('https://api.github.com/user/gvanrossum')
response
response = requests.get('https://api.github.com/v3/user/gvanrossum')
response
response = requests.get('https://api.github.com/v3/users/gvanrossum')
response
response = requests.get('https://api.github.com/users/gvanrossum')
response
response.content
response.headers
response.json()
response = requests.get('https://api.github.com/users/marcgibbons')
response.json()
profile = response.json()
type(profile)
dict.keys()
profile.keys()
list(profile)
sorted(list(profile))
sorted(profile)
profile['name']
profile['location']
response = requests.get('https://api.github.com/users/')
response
response = requests.get('https://api.github.com/users')
response
response.json()
data = response.json()
len(data)
type(data)
len(data)
data[0]
list(data[0])
sorted(data[0])
response = requests.get('https://api.github.com/repositories')
response
data = response.json()
type(data)
data[0]
list(data[0])
sorted(data[0])
response = requests.get('https://api.github.com/search/repositories')
response
response.reason
response = requests.get('https://api.github.com/search/repositories?sort=stars')
response
response.json()
response = requests.get('https://api.github.com/search/repositories?sort=stars&q=language:python')
response
python = response.json()
data = response.json()
type(data)
data
sorted(data)
data['imcomplete_results']
data['incomplete_results']
data['total_count']
type(data['items'])
len(data['items'])
response = requests.get('https://api.github.com/search/repositories?sort=stars&q=language:python')
data = response.json()
data['total_count']
data['items']
data['items'][0]
sorted(data['items'][0])
data['items'][0]['stargazers_count']
data['items'][0]['html_url']
data['items'][0]['name']
data['items'][1]['name']
data['items'][1]['stargazers_count']
results = [
    {'url': repo['html_url'], 'stars': repo['stargazers_count']} 
    for repo in data['items']
]
results
len(results)
results[:5]
results[:10]
get_ipython().run_line_magic('save', 'log.txt n1-n88')
