from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# Custom User model
class CustomUser(AbstractUser):
    # Additional fields can be added here if needed
    pass

# Model for Employees
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    employee_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Model for IT Assets
class ITAsset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    purchase_date = models.DateField()
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assets_assigned')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assets')
    employee_number = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255)
    
    def __str__(self):
        return self.asset_name

# Model for Tickets
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('unresolved', 'Unresolved'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    CATEGORY_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('network', 'Network'),
        ('it_support', 'IT Support'),  # Ensure this is the choice expected
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unresolved', editable=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    due_date = models.DateField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_created')
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolution_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

# Model for Feedback
class Feedback(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=254)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Ticket {self.ticket.ticket_id} - Rating: {self.rating}"
