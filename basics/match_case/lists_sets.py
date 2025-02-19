request = {
    'id': 1,
    'url': 'https://example.com',
    'method': 'GET',
    'timeout': 1000
}

match request:
    case {'url': url, 'method': method, **kwargs} if len(kwargs) < 3:
        print(f'Запрос: url: {url}, метод: {method}')
    case _:
        print('Неверный запрос')
