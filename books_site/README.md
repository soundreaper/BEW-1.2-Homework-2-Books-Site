1. How would we filter for all books with titles containing the word ‘Django’?
2. How would we filter for all books with tag ‘Fiction’?
3. How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!

- Search through the book objects and find the ones containing 'Django' in the name parameter.
- Use Book.objects.filter()
- Use Book.objects.filter() to create a list of books with 'Django' in the name and then use the list to print out the authors of each book.