from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
	stuffs=Timetable.objects.all()
	context= {
		'stuffs': stuffs

	}
	return render(request,'index.html',context)



def add_stuff(request):
	if request.method=="POST":
		course_name = request.POST['course_name']
		Program_name = request.POST['Program_name']
		tmtable =Timetable(course_name=course_name, Program_name=Program_name)
		tmtable.save()
		messages.info(request,"SUCCESSFULLY ADDED")
	else:
		pass

	stuffs=Timetable.objects.all()
	context= {
		'stuffs': stuffs

	}
	return render(request,'index.html',context)


def delete_stuff(request,myid):
	itm = Timetable.objects.get(id=myid)
	itm.delete()
	messages.info(request,"ITEM DELETED SUCCESSFULLY ")
	return redirect(index)


def edit_stuff(request,myid):
	edit_itm =Timetable.objects.get(id=myid)
	stuffs=Timetable.objects.all()
	context = {
		"edit_itm":edit_itm,
		"stuffs":stuffs
	}
	return render(request,'index.html',context)



def update_stuff(request,myid):
	itms =Timetable.objects.get(id=myid)
	itms.course_name=request.POST['course_name']
	itms.Program_name=request.POST['Program_name']
	itms.save()
	messages.info(request,"ITEM UPDATED SUCCESSFULLY ")
	return redirect('index')