from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from django.conf import settings
from .forms import EmailForm, ComentForm, SearchForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import Q


def post_share(request , post_id):

    post = get_object_or_404(Post, id = post_id)

    sent = False

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #post_url = request.buit_absolute_uri(post.get_absolute_url()) нужно для того чтобы показывать в письме откуда пришло письмо полынй домен нашего сайта

            subject = f"{cd["name"]} рекомендую прочитать это письмо {post.title}"
            message = f"{post.title} от \n\n {cd["name"]}, {cd["email"]}, {cd["comment"]}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd["to"]])

            sent = True
    else:
        form = EmailForm()

    return render(request, "blog/post_share.html", context={"post" : post, "form" : form, "sent" : sent} )


def post_list(request, tag_slug = None):




    post = Post.objects.all()

    tag = False
    if tag_slug :
        print(tag_slug)
        tag = get_object_or_404(Tag, slug = tag_slug) 
        post = post.filter(tags__in=[tag])

    form = SearchForm()

    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search']

            # 3) Поиск основанные на 
            post = post.annotate(similarity_title=TrigramSimilarity('title', query), 
                                 similarity_body=TrigramSimilarity('body', query)).filter(Q(similarity_title__gt=0.1) | Q(similarity_body__gt=0.1)).order_by('-similarity_title', '-similarity_body')

            # 2) Создаем полноценый поиск по релевантности и с последуйщей сортировкой по рангу
            # search_vector = SearchVector("title", "body", config='russian')
            # search_query = SearchQuery(query, config='russian')
            # post = post.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')

            # 1) Просто проверяем есть ли вхождение какото тектса в 2 полях title and text 
            #post = post.annotate(search = SearchVector("title", "body"),).filter(search=query)
            #post = post.filter(Q(title__icontains=query) | Q(body__icontains=query))
            
   
    paginator = Paginator(post, 3)

    page_number = request.GET.get("page", 1)

    try:
        posts = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        posts = paginator.page(paginator.num_pages)

    
    return render(request, "blog/list.html", context = {"post":posts, "tag":tag, "form":form })


def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, 
                            publish__year = year,
                            publish__month = month,
                            publish__day = day,
                            slug = post)
    
    if request.method == "POST":
        coments = None
        
    # if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            coments = form.save(commit = False)

            coments.post = post
            coments.user = request.user
            coments.save()
            
           

    coments = post.coments.all()

    formcoments = ComentForm()


    post_tags_ids = post.tags.values_list("id", flat = True) # На данном этапе получаем все id-шники у тегов связанных с постом  = [2, 3, 4]
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id) # тут выдает другие посты которые имеют такие же теги точнее id которые есть в списке выше
    #Добавляем аннотацию same_tags, которая будет содержать количество совпадающих тегов для каждого поста
    #Затем сортируем результаты по количеству совпадений (same_tags) в порядке убывания
    similar_posts = similar_posts.annotate(same_tags=Count("tags")).order_by("-same_tags") # таким образом будет выводися значение более релевантые по тегам как и с этим постом (чем больше ткгов совпадают тем пост похож это и делает данная строка)
    

    return render(request, "blog/detail.html", context = {"post_detail":post, "coments": coments, "formcoments":formcoments, "similar_posts":similar_posts})


# @require_POST # функция буде доступна только если был запрос POST в другом случае функция не выполнится
# def post_coment(request, post_id):
#     coment = None
#     post = get_object_or_404(Post, id=post_id)  
#     print(post_id)
#     # if request.method == "POST":
#     form = ComentForm(request.POST)
#     if form.is_valid():
#         coment = form.save(commit = False)

#         coment.post = post
#         coment.user = request.user
#         coment.save()

#     return render(request, "blog/detail.html", context = {"coment":coment, "post":post, "form":form})