from requests import get, HTTPError, Timeout, TooManyRedirects, RequestException


def get_by_term(term, page):
    url = f'https://www.googleapis.com/books/v1/volumes/'
    params = {
        'key': 'AIzaSyDuFY-Q-UHBEUFxcDWi4MFXZLSMt5ru3VY',
        'q': term,
        'maxResults': 40,
        'printType': 'books',
        'startIndex': 40*page + 1,
        'langRestrict': 'pt'
    }
    return get_information(url, params)


def get_information(url, params=None, retry=0):
    try:
        response = get(url, params=params, timeout=5)
        response.raise_for_status()

    except HTTPError as err:
        return f'#error x01 - HTTP error occurred: {err}'

    except Timeout as err:
        if retry > 2:
            return f'#error x02 - Timeout: {err}'
        else:
            return get_information(url, params, retry + 1)

    except TooManyRedirects as err:
        return f'#error x03 - Too Many Redirects: {err}'

    except RequestException as err:
        return f'#error x04 - Request Error: {err}'

    except Exception as err:
        return f'#error x05 - Unknown Error: {err}'

    else:
        return response.json()

