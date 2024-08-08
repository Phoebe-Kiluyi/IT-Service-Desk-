from django.contrib import admin
from .models import ITAsset, Ticket, Feedback, Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'employee_number')

@admin.register(ITAsset)
class ITAssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset_name', 'asset_type', 'purchase_date', 'assigned_to', 'employee', 'employee_number','contact')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'category', 'due_date', 'created_by')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user_name', 'user_email', 'rating', 'created_at')
