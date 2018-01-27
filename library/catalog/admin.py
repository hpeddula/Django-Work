from django.contrib import admin
from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre
from .models import Language


admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    """
    Defines format of inline book insertion (used in AuthorAdmin)
    """
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    inlines = [BookInstanceInLine]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','borrower','due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets=(
    ('Book Details',{'fields':('book','imprint','id')}),
    ('Availabilty',{'fields':('due_back','status','borrower')}),
    )


# Register your models here.
