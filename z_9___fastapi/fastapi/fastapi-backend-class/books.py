from fastapi import FastAPI, APIRouter

BOOKS = [
    {"id": 1, "title": "Python Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Python-Cookbook-Second-Edition/dp"},
    {"id": 2, "title": "Django Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 3, "title": "Flask Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 4, "title": "Django Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 5, "title": "Flask Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 6, "title": "Django Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 7, "title": "Flask Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 8, "title": "Django Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
    {"id": 9, "title": "Flask Cookbook", "author": "<NAME>", "url": "https://www.amazon.com/Django-Cookbook-Second-Edition"},
]

app = FastAPI()
router = APIRouter()

@router.get('/', status_code=200)
def main():
    return {"Message": "Hello, World"}


@router.get('/api/v1/books', status_code=200)
def get_all_books() -> list:
    return BOOKS

# reade - crud
@router.get('/api/v1/books/{book_id}', status_code=200)
def get_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    if book:
        return book
    return {'error': f'Book with id {book_id} does not exist'}
    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         book
    #         break

# create - crud
@router.post('/api/v1/books')
def create_book(book: dict):
    #{'id': 10, 'title': 'Python Cookbook', 'author': '<NAME'}
    BOOKS.append(book)
    return book

# update - crud
@router.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book: dict):
    book_list = next((book for book in BOOKS if book['id'] == book_id), None)

    if book_list:
        book_list.update(book)
        return book
    return {'error': f'Book with id {book_id} does not exist'}

# delete - crud
@router.delete('/api/v1/books/{book_id}')
def delete_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    if book:
        BOOKS.remove(book)
        return book



app.include_router(router)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("books:app", host="0.0.0.0", port=8001, reload=True)