from django.shortcuts import render

# Create your views here.
def hello(request):
    tags=['waterfall','Hill','sun','cafe']
    rating = 4
    return render(request,'index.html',
        {
            'name':'Travel North Monograph',
            'author':'JJPnz',
            'tags':tags,
            'rating':rating
        })

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def addBlog(request):
    name = request.POST['name']
    desc = request.POST['description']
    return render(request,'result.html',{'name':name,'desc':desc})
