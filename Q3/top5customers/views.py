from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from .models import Order

def top_customers_view(request):
    six_months_ago = timezone.now() - timedelta(days=180)
    
    top_customers = Order.objects.filter(
        order_date__gte=six_months_ago, status='completed'
    ).values('customer').annotate(
        total_spent=Sum('total_amount')
    ).order_by('-total_spent')[:5] 
    
    return render(request, 'top_customers.html', {'top_customers': top_customers})
