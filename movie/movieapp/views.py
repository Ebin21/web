from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm



# Create your views here.
def index(request):
    obj = Movie.objects.all()
    context={'movie_l':obj}
    return render(request,"index.html",context)
def details(request,movie_id):
    mov=Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movied':mov})
    # return HttpResponse(" The movie id is %s"% movie_id )
def add(request):
    if request.method=='POST':
        mname=request.POST.get('mname')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES.get('img')
        movie=Movie(name=mname, desc=desc, year=year, img=img)
        movie.save()

    return render(request,"add.html")

def update(request,movie_id):
    mov=Movie.objects.get(id=movie_id)
    form=MovieForm(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form,'movie':mov})
def delete(request,movie_id):
    if request.method=='POST':
        mov = Movie.objects.get(id=movie_id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')
