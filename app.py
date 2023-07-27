from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    'id': 1,
    'título': 'O Último Reino',
    'autor': 'Bernard Cornwell'
  },
  {
    'id': 2,
    'título': 'Drácula',
    'autor': 'Bram Stoker'
  },
  {
    'id': 3,
    'título': 'Hamlet',
    'autor': 'William Shakespeare'
  }
]

#Consultar(todos)
@app.route('/books',methods=['GET'])
def obtain_books():
  return jsonify(books)
#Consultar(id)
@app.route('/books/<int:id>',methods=['GET'])
def obtain_books_byid(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)
#Editar
@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_byid(id):
  book_altered = request.get_json()
  for index,book in enumerate(books):
    if book.get('id') == id:
      books[index].update(book_altered)
      return jsonify(books[index])
#Criar
@app.route('/books',methods=['POST'])
def create_newbook():
  new_book = request.get_json()
  books.append(new_book)
  
  return jsonify(books)
#Excluir
@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
  for index, book in enumerate(books):
    if book.get('id') == id:
      del books[index]
      
  return jsonify(books)
app.run(port=5000,host='localhost',debug=True)