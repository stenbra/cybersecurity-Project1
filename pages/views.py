from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account,Poem


@login_required
@csrf_exempt
def homePageView(request):
    injection=request.GET.get("query", "")
    query = f"SELECT id, title FROM pages_poem WHERE user_id = {request.user.id} AND title LIKE '%{injection}%'"
    poems = Poem.objects.raw(query)
	# poems = Poem.objects.filter(
    #     user=request.user,
    # )
    return render(request, 'pages/index.html', {'poems': poems})

@login_required
@csrf_exempt
def poemAddView(request):
    if request.method == "POST":
        poem = Poem(
            user=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("content"),
        )
        poem.save()
    return redirect(request.META.get("HTTP_REFERER"), "/")


@login_required
def poemDetailView(request, poem_id):
    poem = Poem.objects.get(pk=poem_id)
    return render(request, "pages/poem.html", {"poem": poem})

@login_required
def poemDeleteView(request, poem_id):
    poem = Poem.objects.get(pk=poem_id)
    poem.delete()
    return redirect("/")


