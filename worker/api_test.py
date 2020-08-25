from requests import put, get


html=put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
print(html)

get_html = get('http://localhost:5000/todo1').json()
print(get_html)
