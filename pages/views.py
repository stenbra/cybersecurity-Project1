from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account,Poem


@login_required
def homePageView(request):
	poems = Poem.objects.filter(
        user=request.user,
    )

	return render(request, 'pages/index.html', {'poems': poems})

@login_required
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


