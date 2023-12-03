from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render (request, 'forum/home.html')

def lesson (request):
    return render (request, 'lesson/lesson.html')

def forum(request):

    posts = Post.objects.all()

    return render(request, 'myapp/forum.html', {'posts': posts})


def create_post(request):

    if request.method == 'POST':

        # Handle form submission and create a new post

        # For simplicity, let's assume you have a form handling logic here

        # You should validate and save the form data to create a new Post object

        # Redirect to the forum page after creating the post

        return redirect('forum')

    else:

        # Render the form for creating a new post

        return render(request, 'myapp/create_post.html')


def view_post(request, post_id):

    # View logic for displaying a single post

    # Retrieve the post with the given post_id and pass it to the template

    return render(request, 'myapp/view_post.html', {'post_id': post_id})
    
#return HttpResponse('holas') -> para probar
