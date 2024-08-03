# app/views.py
import os
from django.shortcuts import render
from markdown2 import markdown

def read_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return markdown(content)

def home(request):
    return render(request, 'home.html')

def github(request):
    return render(request, 'github.html')

def quien_soy(request):
    content_html = read_markdown_file(os.path.join('content', 'quiensoy.md'))
    return render(request, 'quien_soy.html', {'content_html': content_html})

def contacto(request):
    return render(request, 'contacto.html')

def blog(request):
    post_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'post')
    posts = []

    for filename in os.listdir(post_dir):
        if filename.endswith('.md'):
            posts.append({'title': filename.replace('.md', ''), 'filename': filename.replace('.md', '')})

    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, filename):
    post_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'post')
    filepath = os.path.join(post_dir, f"{filename}.md")
    content_html = read_markdown_file(filepath)
    return render(request, 'post_detail.html', {'title': filename, 'content_html': content_html})