from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, AlumniProfileForm
from .models import Alumni
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Alumni as AlumniProfile
from .models import Alumni, Event
from .models import News
from django.contrib import messages
from .models import Vacancy
from .forms import LoginForm
def home(request):
    alumni_list = Alumni.objects.all()[:4]  # Fetch latest 5 alumni
    event_list = Event.objects.all().order_by('date')  # Fetch upcoming 5 events sorted by date
    news_list = News.objects.all()
    context = {
        'alumni_list': alumni_list,
        'event_list': event_list,
        'news_list': news_list,
    }
    return render(request, 'base.html', context)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def edit_alumni(request):
    if request.method == 'POST':
        try:
            profile = Alumni.objects.get(user=request.user)  # Ensure correct profile retrieval
        except Alumni.DoesNotExist:
            return redirect('dashboard')  # Handle missing profile gracefully

        # Update fields
        profile.user.username = request.POST['username']
        profile.user.email = request.POST['email']
        profile.batch = request.POST['batch']
        profile.department = request.POST['department']
        profile.position = request.POST['position']
        profile.company = request.POST['company']
        profile.contact = request.POST['contact']

        # Save user and profile
        profile.user.save()
        profile.save()

        return redirect('dashboard')

    return redirect('dashboard')
def login_view(request):
    error_message=''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            alumni = Alumni.objects.get(email=username)  # Assuming you're using email as username
            if password==alumni.user.password:  # Check password hash
                login(request, alumni.user)  # Log the user in
                return redirect('home')  # Redirect to a dashboard or home page after login
            else:
                error_message = "Invalid password"
        except Alumni.DoesNotExist:
            error_message = "User not found"
    
    return render(request, "login.html", {"error_message": error_message})
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = AlumniProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Save user registration details
            profile = profile_form.save(commit=False)
            profile.user = user  # Link the alumni profile to the user
            profile.save()  # Save alumni details
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to the dashboard

    else:
        form = UserRegisterForm()
        profile_form = AlumniProfileForm()

    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})
def logout_view(request):
    logout(request)
    return redirect('/')

def alumni_list(request):
    alumni_profiles = Alumni.objects.all()  # Fetch all alumni profiles
    alumni_news = News.objects.all().order_by('-created_at')  # Fetch all news sorted by latest
    alumni_vacancies = Vacancy.objects.all().order_by('-created_at')  # Fetch all vacancies sorted by latest

    context = {
        "alumni_profiles": alumni_profiles,
        "alumni_news": alumni_news,
        "alumni_vacancies": alumni_vacancies,
    }
    return render(request, "alumni_list.html", context)
@login_required
def admin_dashboard(request):
    total_alumni = AlumniProfile.objects.count()
    total_departments = AlumniProfile.objects.values("department").distinct().count()
    total_companies = AlumniProfile.objects.values("company").distinct().count()
    alumni_list = AlumniProfile.objects.all()

    context = {
        "total_alumni": total_alumni,
        "total_departments": total_departments,
        "total_companies": total_companies,
        "alumni_list": alumni_list,
    }
    return render(request, "admin/dashboard.html", context)
def all_alumni(request):
    alumni_list = Alumni.objects.all()
    alumni_news = Vacancy.objects.all()
    alumni_events = Event.objects.all()
    return render(request, "all_alumni.html", {"alumni_list": alumni_list, "alumni_news": alumni_news, "alumni_events": alumni_events})
@login_required
def post_news(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            News.objects.create(title=title, content=content, user=request.user)
            return redirect("post_news")  # Refresh the page after posting

    # Fetch only news posted by the logged-in user (alumni)
    alumni_news = News.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "post_news.html", {"alumni_news": alumni_news})

from .models import Vacancy
from django.contrib import messages

@login_required
def post_vacancy(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        company = request.POST.get("company")
        location = request.POST.get("location")

        if title and description and company:
            Vacancy.objects.create(
                user=request.user,
                title=title,
                description=description,
                company=company,
                location=location
            )
            messages.success(request, "Vacancy posted successfully!")
            return redirect("post_vacancy")  # Stay on the same page after posting
        else:
            messages.error(request, "All fields are required!")

    # Fetch only vacancies posted by the logged-in alumni user
    alumni_vacancies = Vacancy.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "post_vacancy.html", {"alumni_vacancies": alumni_vacancies})

@login_required
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id, user=request.user)
    news.delete()
    messages.success(request, "News post deleted successfully!")
    return redirect("post_news")

@login_required
def delete_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id, user=request.user)
    vacancy.delete()
    messages.success(request, "Vacancy deleted successfully!")
    return redirect("post_vacancy")

def alumni_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if an Alumni record exists with this email and password
        try:
            alumni = Alumni.objects.get(email=email, password=password)  # Direct check
            messages.success(request, "Login successful!")
            return redirect("dashboard")  # Redirect to alumni dashboard
        except Alumni.DoesNotExist:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, "alumni_login.html")