from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Issue, StatusUpdate, Message
from django.http import JsonResponse
import json

def report_issue(request):
    if request.method == "POST":
        is_draft = request.POST.get('save_draft') == 'true'
        issue_data = {
            'issue_type': request.POST.get('issue_type'),
            'description': request.POST.get('description'),
            'location': request.POST.get('location'),
            'latitude': float(request.POST.get('latitude', 0)),
            'longitude': float(request.POST.get('longitude', 0)),
        }
        
        if not is_draft:
            issue = Issue.objects.create(**issue_data, is_draft=False)
            StatusUpdate.objects.create(issue=issue, status='Submitted', note='Issue submitted')
            messages.success(request, 'Issue reported successfully!')
            return redirect('confirmation')
        else:
            # Save draft logic (simplified)
            messages.info(request, 'Draft saved!')
            return redirect('report_issue')
    
    return render(request, 'reporting/report_issue.html')

def dashboard(request):
    if request.user.is_authenticated:
        issues = Issue.objects.filter(user=request.user).order_by('-created_at')
    else:
        issues = Issue.objects.none()
    return render(request, 'reporting/dashboard.html', {'issues': issues})

@login_required
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk, user=request.user)
    if request.method == 'POST':
        if 'escalate' in request.POST:
            issue.status = 'Reopened'
            issue.save()
            StatusUpdate.objects.create(issue=issue, status='Reopened', note='User escalated')
        elif 'message' in request.POST:
            Message.objects.create(issue=issue, user=request.user, message=request.POST['message'])
        messages.success(request, 'Action completed!')
        return redirect('issue_detail', pk=pk)
    return render(request, 'reporting/issue_detail.html', {'issue': issue})

def confirmation(request):
    return render(request, 'reporting/confirmation.html')

def home(request):
    return render(request, 'reporting/home.html')