#library_creator
from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:
    class Animal(Thing):
       label = ["animal"]

    class Book(Thing):
        label = ["book"]
               

    class read_books(Animal >> Book):
        python_name = "books"
        label = ["read books"]    

    class is_read_by(Book >> Animal):
        python_name = "is_read_by"    
        inverse_property = read_books
        label = ["is read by"]

    class PopularBook(Book):
        equivalent_to = [Book & is_read_by.min(3, Animal)]
        label = ["popular book"]

    class OneBookReader(Animal):
        equivalent_to = [Animal & read_books.exactly(1, Book)]
        label = ["one book reader"]

    class SuperAnimal(Animal):
        equivalent_to = [Animal & read_books.min(2, Book)]
        label = ["very clever animal that reads a lot"]

    book1 = Book(name="Jane_Eyre",)
    book2 = Book(name="The_Great_Gatsby", )
    book3 = Book(name="The_Grapes_of_Wrath", )

    AllDifferent([book1, book2, book3])

    animal1 = Animal(books = [book1], name="mouse")
    animal2 = Animal(books = [book1, book2, book3], name="owl")
    animal3 = Animal(books = [], name="snail")
    animal4 = Animal(books = [book1, book3], name="frog")

    close_world(Animal)

onto.save("onto.owl")







