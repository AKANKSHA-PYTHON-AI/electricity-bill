import database

user_choice = '''
Enter :
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit '''
print(user_choice)
print()
print('------choose what you want------')
choice = input('enter your choice :')
print()


def menu():
    database.create_books_table()
    user_input = input(user_choice)
    while user_input!='q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        else:
            user_input == 'd'
            prompt_delete_book()
            user_input = input(user_choice)


def prompt_add_book():
    name = input('Enter the name of the book you wish to read :')
    database.insert_book(name)

prompt_add_book()


def list_books():
    for book in database.get_all_books():
        read = 'Yes' if book ['read'] else 'No'
        print(f'{book['name']} by {book} read: {read}')
list_books()


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading :')
prompt_read_book()

def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete :')
    database.delete_book(name)
prompt_delete_book()