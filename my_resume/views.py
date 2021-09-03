from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView

import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Person, Languages, Awards, Education, Experience, Skills, Project, Volunteer
from .forms import  PersonForm, LanguageForm, AwardForm, ExperienceForm, EducationForm, SkillsForm, ProjectForm, SignUpForm, EditAccountForm, PasswordChangingForm, VolunteerForm


class MyPerson(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Person
    form_class = PersonForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        person = form.save(commit=False)
        person.user = self.request.user  
        person.save()
        return redirect('resume')

@login_required(login_url='login')
def EditPerson(request, pk):
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(instance=person)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_user.html', context)


class MySkills(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Skills
    form_class =SkillsForm
    template_name = 'create_skills.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditSkills(request, pk):
        skills = get_object_or_404(Skills, pk=pk)
        form = SkillsForm(instance=skills)
        if request.method == 'POST':
            form = PersonForm(request.POST, instance=skills)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_skills.html', context)

 
class MyLanguage(LoginRequiredMixin ,CreateView):
    login_url = 'login'
    model = Languages
    form_class = LanguageForm
    template_name = 'create_language.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')


@login_required(login_url='login')
def EditLanguage(request, pk):
        language = get_object_or_404(Languages, pk=pk)
        form = LanguageForm(instance=language)
        if request.method == 'POST':
            form = LanguageForm(request.POST, instance=language)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_language.html', context)


class MyAward(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Awards
    form_class = AwardForm
    template_name = 'create_award.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditAward(request, pk):
        award = get_object_or_404(Awards, pk=pk)
        form = AwardForm(instance=award)
        if request.method == 'POST':
            form = AwardForm(request.POST, instance=award)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_award.html', context)


class MyExperience(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Experience
    form_class = ExperienceForm
    template_name = 'create_experience.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditExperience(request, pk):
        experience = get_object_or_404(Experience, pk=pk)
        form = ExperienceForm(instance=experience)
        if request.method == 'POST':
            form = ExperienceForm(request.POST, instance=experience)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_experience.html', context)


class MyEducation(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Education
    form_class = EducationForm
    template_name = 'create_education.html'

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditEducation(request, pk):
        education = get_object_or_404(Education, pk=pk)
        form = EducationForm(instance=education)
        if request.method == 'POST':
            form = EducationForm(request.POST, instance=education)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_education.html', context)


class MyProject(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        experience = form.save(commit=False)
        experience.user = self.request.user  
        experience.save()
        return redirect('resume')

@login_required(login_url='login')
def EditProject(request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(instance=project)
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_project.html', context)


@login_required(login_url='login')
def Resume(request):
    language  = Languages.objects.filter(user = request.user)[:5]
    education = Education.objects.filter(user = request.user)[:3]
    experience = Experience.objects.filter(user = request.user)[:5]
    person = Person.objects.filter(user = request.user)[:1]
    skills = Skills.objects.filter(user = request.user)[:5]
    awards = Awards.objects.filter(user = request.user)[:5]
    projects = Project.objects.filter(user = request.user)[:5]
    volunteer = Volunteer.objects.filter(user = request.user)[:5]
    # template = loader.get_template('add_resume.html')
    # html = template.render( {'language':language, 'education':education, 'experience':
    #     experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects})
    # options = {
    #     'page-size':'Letter',
    #     'encoding':'UTF-8'
    # }
    # pdf = pdfkit.from_string(html, False, options)
    # response  = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment'
    # filename = 'resume.pdf'
    # return response
    return render(request, 'add_resume.html', {'language':language, 'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects, 'volunteer':volunteer})


@login_required(login_url='login')
def ResumePreview(request):
    language  = Languages.objects.filter(user = request.user)[:5]
    education = Education.objects.filter(user = request.user)[:3]
    experience = Experience.objects.filter(user = request.user)[:5]
    person = Person.objects.filter(user = request.user)[:1]
    skills = Skills.objects.filter(user = request.user)[:5]
    awards = Awards.objects.filter(user = request.user)[:5]
    projects = Project.objects.filter(user = request.user)[:5]
    volunteer = Volunteer.objects.filter(user = request.user)[:5]
    # template = loader.get_template('add_resume.html')
    # html = template.render( {'language':language, 'education':education, 'experience':
    #     experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects})
    # options = {
    #     'page-size':'Letter',
    #     'encoding':'UTF-8'
    # }
    # pdf = pdfkit.from_string(html, False, options)
    # response  = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment'
    # filename = 'resume.pdf'
    # return response
    return render(request, 'resume_preview.html', {'language':language, 'education':education, 'experience':
        experience, 'person': person, 'skills':skills, 'awards': awards, 'projects': projects, 'volunteer':volunteer})


class CreateAccount(CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('resume')

class UpdateAccount(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    form_class= EditAccountForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('blog_list')

    def get_object(self):
        return self.request.user

@login_required(login_url='login')
def UserDelete(request):
     user = request.user
     if request.method == 'POST':
                user.delete()
                return redirect('login')


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = 'login'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

@login_required(login_url='login')
def DeletePerson(request, pk):
	person  = Person .objects.get(id=pk)
	person.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteSkills(request, pk):
	skills =Skills.objects.get(id=pk)
	skills.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteExperience(request, pk):
	experience = Experience.objects.get(id=pk)
	experience.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteEducation(request, pk):
	education = Education.objects.get(id=pk)
	education.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteAwards(request, pk):
	queryset = Awards.objects.get(id=pk)
	queryset.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteLanguage(request, pk):
	language = Languages.objects.get(id=pk)
	language.delete()
	return redirect('resume')

@login_required(login_url='login')
def DeleteProject(request, pk):
	project = Project.objects.get(id=pk)
	project.delete()
	return redirect('resume')

class Volunteers(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'create_volunteer.html'
    success_url = reverse_lazy('resume')

    def form_valid(self, form):
        volunteer = form.save(commit=False)
        volunteer.user = self.request.user  
        volunteer.save()
        return redirect('resume')


@login_required(login_url='login')
def EditVolunteers(request, pk):
        volunteer = get_object_or_404(Volunteer, pk=pk)
        form = VolunteerForm(instance=volunteer)
        if request.method == 'POST':
            form = VolunteerForm(request.POST, instance=volunteer)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form':form}
        return render(request, 'create_volunteer.html', context)

@login_required(login_url='login')
def DeleteVolunteers(request, pk):
	volunteer = Volunteer.objects.get(id=pk)
	volunteer.delete()
	return redirect('resume')