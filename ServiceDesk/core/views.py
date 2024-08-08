from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone
from .forms import CustomUserCreationForm, AdminLoginForm

from .forms import FeedbackForm, TicketForm
from .models import Ticket, Feedback, ITAsset

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    return render(request, 'core/my_tickets.html', {'tickets': tickets})

@login_required
def self_service(request):
    return render(request, 'core/self_service.html')

@login_required
def asset_tracking(request):
    assets = ITAsset.objects.all()
    return render(request, 'core/asset_tracking.html', {'assets': assets})

@login_required
def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, 'Ticket submitted successfully!')
            return redirect('core:track_tickets')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = TicketForm()

    return render(request, 'core/submit_ticket.html', {'form': form})

def track_tickets(request):
    tickets = Ticket.objects.all()  # Retrieve all tickets
    context = {
        'tickets': tickets,
    }
    return render(request, 'core/track_tickets.html', context)

def user_logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('core:user_login')
    return render(request, 'core/logout.html')

def admin_check(user):
    return user.is_superuser

@login_required
@user_passes_test(admin_check)
def resolve_tickets(request):
    unresolved_tickets = Ticket.objects.filter(status='Unresolved')
    if request.method == 'POST':
        resolution = request.POST.get('resolution')
        ticket = unresolved_tickets.first()
        if ticket and resolution:
            ticket.status = 'Resolved'
            ticket.resolved_at = timezone.now()
            ticket.resolution_notes = resolution
            ticket.save()
            messages.success(request, 'Ticket resolved successfully!')
        else:
            messages.error(request, 'No unresolved tickets found or resolution details are missing.')
        return redirect('core:resolve_tickets')
    return render(request, 'core/resolve_tickets.html', {'tickets': unresolved_tickets})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback submitted successfully!')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback.html', {'form': form})


def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'core/feedback_list.html', {'feedbacks': feedbacks})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')

            # Redirect based on user role or other criteria
            if user.is_superuser:
                return redirect('admin:index')  # Redirect to admin page
            else:
                return redirect('core:index')  # Redirect to homepage or any other page

        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                auth_login(request, user)
                return redirect('core:admin_dashboard')
            else:
                messages.error(request, 'You do not have admin privileges.')
                return redirect('core:user_login')
    else:
        form = AuthenticationForm()
    return render(request, 'core/admin_login.html', {'form': form})

@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    total_tickets = Ticket.objects.count()
    unresolved_tickets = Ticket.objects.filter(status='Unresolved').count()
    feedback_count = Feedback.objects.count()
    
    context = {
        'total_tickets': total_tickets,
        'unresolved_tickets': unresolved_tickets,
        'feedback_count': feedback_count
    }
    return render(request, 'core/admin_dashboard.html', context)

def reports(request):
    # Fetch data for reports
    tickets_count = Ticket.objects.count()
    feedback_count = Feedback.objects.count()
    assets_count = ITAsset.objects.count()

    # Fetch additional report data if needed
    unresolved_tickets = Ticket.objects.filter(status='unresolved').count()
    resolved_tickets = Ticket.objects.filter(status='resolved').count()
    in_progress_tickets = Ticket.objects.filter(status='in_progress').count()
    
    # Context data for the template
    context = {
        'tickets_count': tickets_count,
        'feedback_count': feedback_count,
        'assets_count': assets_count,
        'unresolved_tickets': unresolved_tickets,
        'resolved_tickets': resolved_tickets,
        'in_progress_tickets': in_progress_tickets,
    }

    return render(request, 'core/reports.html', context)



