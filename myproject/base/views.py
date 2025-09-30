from django.shortcuts import render,redirect,get_object_or_404
from base.models import TaskModel,HistoryModel
from django.db.models import Q

# Create your views here.
from django.db.models import Q

def home(request):
    user = request.user
    if 'q' in request.GET:
        q = request.GET['q']
        all_data = TaskModel.objects.filter(
            (Q(title__icontains=q) & Q(host=user)) |
            (Q(desc__icontains=q) & Q(host=user))
        )
    else:
        all_data = TaskModel.objects.filter(host=user, is_completed=False)  
    return render(request, 'home.html', {'data': all_data})



def add(request):
    if request.method=='POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']
        print(title_data,desc_data)
        TaskModel.objects.create(
            title=title_data,
            desc=desc_data,
            host=request.user
        )
        return redirect('home')
    return render(request,'add.html')

def about(request):
    return render(request,'about.html')

def support(request):
    return render(request,'support.html')

def history(request):
    return render(request,'history.html')

def completed(request):
    return render(request,'completed.html')

def update(request,pk):
    #old data
    task=TaskModel.objects.get(id=pk)
    #new data
    if request.method=='POST':
        title_data=request.POST['title_attr']
        desc_data=request.POST['desc_attr']

        task.title=title_data
        task.desc=desc_data
        task.save()
        return redirect('home')
    return render(request,'update.html',{'task':task})

def delete_(request,pk):
    data=TaskModel.objects.get(id=pk)
    HistoryModel.objects.create(title=data.title,desc=data.desc)
    data.delete()
    return redirect('home')

def history(request):
    history_data=HistoryModel.objects.all()
    return render(request,'history.html',{'data':history_data})

def delete_task(request, pk):
    data = HistoryModel.objects.get(id=pk)
    data.delete()
    return redirect('history')

def restore_task(request,pk):
    data=HistoryModel.objects.get(id=pk)
    TaskModel.objects.create(title=data.title,desc=data.desc,host=request.user)
    data.delete()
    return redirect('home')

def restore_all(request):
    data = HistoryModel.objects.all()
    for item in data:  
        TaskModel.objects.create(title=item.title, desc=item.desc,host=request.user)
    data.delete()  
    return redirect('home')

def clear_all(request):
    data=HistoryModel.objects.all()
    data.delete()
    return redirect('history')

def confirm_delete(request,pk):
    data=TaskModel.objects.get(id=pk)
    return render(request,'confirm_delete.html',{'record':data})
    
def complete_task(request, id):
    task = get_object_or_404(TaskModel, id=id, host=request.user)
    task.is_completed = True
    task.save()
    return redirect('completed') 

def completed_tasks(request):
    data = TaskModel.objects.filter(host=request.user, is_completed=True)
    return render(request, 'completed.html', {'data': data})


def undo_complete(request, id):
    task = get_object_or_404(TaskModel, id=id, host=request.user)
    task.is_completed = False
    task.save()
    return redirect('home') 

def delete_completed(request, id):
    task = get_object_or_404(TaskModel, id=id, host=request.user)
    task.delete()
    return redirect('completed')
