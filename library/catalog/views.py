from django.shortcuts import render,get_object_or_404
from .models import Genre,Book,BookInstance,Author
from django.views import  generic
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.http import  HttpResponseRedirect
from django.urls import  reverse
from .forms import RenewBookForm
# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()
    #Available books i.e book with status a
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    return render(
    request,
    'index.html',
    context={'num_books':num_books,'num_book_instances':num_book_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_visits':num_visits},
    )
class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author
class AuthorDetailView(generic.DetailView):
    model = Author
class LoanedBookByUserView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
def renew_book_librarian(request,pk):
    book_inst = get_object_or_404(BookInstance,pk = pk)

    if request.method == 'POST':
        form =RenewBookForm(request.POST)

        if form.is_valid():
            book_inst.due_back = form.cleanded_data['renewal_date']
            book_inst.save()

    else:
        proposed_renew_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return(request,'catalog/book_renew_librarian.html',{'form':form,'bookinst':book_inst})
