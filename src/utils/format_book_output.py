from src.external_api.get_book import get_by_identifier


def format_book_output(data):
    if 'volumeInfo' in data and 'id' in data:
        return {'identifier': data['id'], 'cover': data['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in data[
            'volumeInfo'] else 'https://uploads.sarvgyan.com/2014/03/image-unavailable.jpg',
            'book_title': data['volumeInfo']['title'] if 'title' in data['volumeInfo'] else 'Sem Título',
            'description': data['volumeInfo']['description'] if 'description' in data['volumeInfo'] else 'Sem Descrição',
            'author': data['volumeInfo']['authors'] if 'authors' in data['volumeInfo'] else ['Sem autores'],
            'genre': data['volumeInfo']['categories'] if 'categories' in data['volumeInfo'] else ['Sem Categoria']}
    return {}


def get_and_format_output(identifier):
    book = get_by_identifier(identifier)

    return format_book_output(book)
