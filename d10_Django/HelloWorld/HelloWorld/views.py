from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world111111 ")



from django.shortcuts import render
 
def runoob(request):
    context          = {}
    context['hello'] = 'Hello World222222'
    return render(request, 'runoob.html', context)

def runoob2(request):
   
    str="润科通用"
    name="hehe"
    my_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request, 'runoob.html', {'name':str,'hello':name,'list':my_list})

