from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm

# Create your views here.
class CourseObjectMixin(object):
    model = Course
    lookup = id

    def get_object(self):
        obj=None

        lookup = self.kwargs.get("lookup")
        if lookup is not None:
            obj = get_object_or_404(Course, lookup=lookup)
        return obj



class CourseView(View):

    def get(self,request, id=None, *args, **kwargs):
        template_name = 'courses/course_detail.html'

        context = {}
        obj=""
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        context['object']= obj
        return render(request, template_name,context)


class CourseListView(View):
    template_name = 'courses/course_list.html'

    query_set = Course.objects.all()

    def get_queryset(self):
        return self.query_set

    def get(self,request):
     
        print("printing obj")
        print(self.query_set)

        for a in self.query_set:
            print(a.get_absolute_url)

        context = {
            'object_list':self.get_queryset()
        }

        return render(request,self.template_name,context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self,request, id=None, *args, **kwargs):

        context = {}
        form = CourseModelForm()
        context['form']= form
        return render(request, self.template_name,context)


    def post(self,request, id=None, *args, **kwargs):

        context = {}

        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']= form
        return render(request, self.template_name,context)


class CourseUpdateView(View):

    template_name = 'courses/course_update.html'
    def get_object(self):
        obj = ""

        id = self.kwargs.get("pk")
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self,request, id=None, *args, **kwargs):

        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['form']= form
            context['object']= obj

        return render(request, self.template_name,context)


    def post(self,request, id=None, *args, **kwargs):

        context = {}

        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST,instance=obj)
            if form.is_valid():
                form.save()
            context['form']= form
            context['object']= obj

        return render(request, self.template_name,context)


class CourseDeleteView(View):

    template_name = 'courses/course_delete.html'

    def get_object(self):
        obj=""
        id = self.kwargs.get("pk")
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self,request, id=None, *args, **kwargs):

        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object']= obj

        return render(request, self.template_name,context)


    def post(self,request, id=None, *args, **kwargs):

        context = {}

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object']= None
            return redirect('/courses/')

        return render(request, self.template_name,context)

# class MyListView(CourseListView):
#     query_set = Course.objects.filter(id=1)


   