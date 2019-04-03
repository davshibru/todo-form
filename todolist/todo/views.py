from django.shortcuts import render, get_object_or_404
from .models import To
from .forms import ToForm
from django.shortcuts import redirect

def todo_list(request):
	to = To.objects.all()
	return render(request, 'todo/todo_list.html', {'to': to})

def todo_new(request):
	if request.method == "TODO":
		form = ToForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('todo_detail', pk=form.pk)
	else:
		form = ToForm()
	return render(request, 'todo/todo_edit.html', {'form': form} )

def todo_edit(request, pk):
	todo = get_object_or_404(To, pk = pk)
	if request.method == "TODO":
		form = ToForm(request.POST, instans=todo)
		if form.is_valid:
			form.save
			return redirect('todo_detail', pk=form.pk)
	else:
		form = ToForm(instans=todo)
	return render(request, 'todo/todo_edit.html', {'form': form})

# Create your views here.
