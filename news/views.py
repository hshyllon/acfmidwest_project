from django.shortcuts import render
from .models import Blog, BlogComment, BlogAuthor
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def news(request):
    get_news = Blog.objects.filter(is_published = True).order_by('-create_date')
    print(get_news)
    context = {
        'get_news' : get_news,
        }
    
    return render(request, 'news/news.html', context)

def blog (request, blog_id):
    blog_detail = get_object_or_404 (Blog, pk = blog_id)
    blog_comment_count = BlogComment.objects.filter(blog = blog_id, is_approved=True).count()
    blog_comments = BlogComment.objects.filter(blog = blog_id, is_approved=True).order_by('-create_date')
    
    get_recent_blogs = Blog.objects.filter(is_published = True).order_by('-create_date')[:3]
    #author_info = BlogAuthor.objects.filter(author = blog_detail.author)
    
    if blog_detail.tags:
        blog_tags = blog_detail.tags.split(",")

    context = {
        'blog_detail': blog_detail,
        'blog_comment_count' : blog_comment_count,
        'blog_tags' : blog_tags,
        'blog_comments' : blog_comments,
        'recent_blogs' : get_recent_blogs,
        }
    
    return render(request, 'news/blog.html', context)

def submission(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        blog = request.POST['blog_id']
        blog_title = request.POST['blog_title']
        comment = request.POST['comment']
        commentor = request.POST['user_id']
#         if request.POST['user_id']:
#             commentor = request.POST['user_id']
#         else:
#             commentor = ""
        
        blog_comment = BlogComment(fullname = fullname, blog=blog, blog_title=blog_title, email=email, comment=comment, commentor=commentor )

        blog_comment.save()
        #messages.success(request, 'Your comment has been submitted. You should see it on this page soon!')
    

    
        context = {
            'blog_title' : blog_title,
            'message' : 'Thank you for your comment on our blog!'
            }
        return render(request, 'news/submission.html', context)