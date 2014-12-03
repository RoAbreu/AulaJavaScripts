from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from tekton import router
from gaegraph.model import Node, Arc
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(_logged_user):
   chave_do_usuario = _logged_user.key
   query=AutorArco.query(AutorArco.origin==chave_do_usuario)
   autor_arcos = query.fetch()
   chaves_de_livros=[arco.destination for arco in autor_arcos]
   livro_lista = ndb.get_multi(chaves_de_livros)
   livro_lista=[livro for livro in livro_lista if livro!=None]
   form=BookFormTable()
   livro_lista=[form.fill_with_model(livro) for livro in livro_lista]
   editar_form_path=router.to_path(editar_form)
   delete_path = router.to_path(delete)
   for livro in livro_lista:
       livro['edit_path']='%s/%s'%(editar_form_path,livro['id'])
       livro['delete_path']='%s/%s'%(delete_path,livro['id'])
   contexto = {'livro_lista':livro_lista}
   return TemplateResponse(contexto)

def delete(book_id):
    chave = ndb.Key(Book, int(book_id))
    chave.delete()
    query = AutorArco.find_origins(chave)
    chaves_dos_arcos = query.fetch(keys_only=True)
    ndb.delete_multi(chaves_dos_arcos)
    return RedirectResponse(router.to_path(index))

@no_csrf
def editar_form(book_id):
    book_id=int(book_id)
    book = Book.get_by_id(book_id)
    book_form=BookForm()
    book_form.fill_with_model(book)
    contexto = {'salvar_path': router.to_path(editar,book_id), 'book':book_form}
    return TemplateResponse(contexto, 'books/form.html')

def editar(book_id, **propriedades):
    book_id=int(book_id)
    book=Book.get_by_id(book_id)
    book_form = BookForm(**propriedades)
    erros = book_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros': erros, 'book': book_form}
        return TemplateResponse(contexto, 'books/form.html')
    else:
        book_form.fill_model(book)
        book.put()
        return RedirectResponse(router.to_path(index))

@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Book(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty()

class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Book, required=True)

class BookFormTable(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.creation, Book.price]

class BookForm(ModelForm):
    _model_class = Book
    _include = [Book.title, Book.release, Book.price]

def salvar(_logged_user, **propriedades):
    book_form = BookForm(**propriedades)
    erros = book_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros': erros, 'book': book_form}
        return TemplateResponse(contexto, 'books/home.html')
    else:
        book = book_form.fill_model()
        chave_do_livro = book.put()
        chave_de_usuario = _logged_user.key
        autor_arco = AutorArco(origin=chave_de_usuario, destination=chave_do_livro)
        autor_arco.put()

        return RedirectResponse(router.to_path(index))