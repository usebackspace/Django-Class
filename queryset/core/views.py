from django.shortcuts import render
from . models import Queryset
from django.db.models import Q
# Create your views here.
def queryset(request):
    # query = Queryset.objects.all()
    query = Queryset.objects.all()[:7]    # Same as slicing method works
    # query = Queryset.objects.filter(id=3)       #give result value which have id=3
    # query = Queryset.objects.exclude(id=3)      # give result value other than id=3  
    # query = Queryset.objects.filter(name__exact='chris')     # Search for exact value and it is case sensitive
    # query = Queryset.objects.filter(name__iexact='chris')    # Search for exact value and it is not case sensitive
    # query = Queryset.objects.filter(name__contains='j')   
    # query = Queryset.objects.filter(name__icontains='j')      
    # query = Queryset.objects.filter(name__in=['tony','Chris'])   
    # query = Queryset.objects.filter(id__in=[1,3,6,9,21])      # Display data of specific id
    # query = Queryset.objects.filter(id__gt=4)                 # id>4
    # query = Queryset.objects.filter(id__gte=4)                  # id>=4
    # query = Queryset.objects.filter(id__lt=4)                  # id<=4
    # query = Queryset.objects.filter(id__lte=4)                  # id<=4
    # query = Queryset.objects.filter(name__startswith='s')                  
    # query = Queryset.objects.filter(name__startswith='s')                  
    # query = Queryset.objects.filter(name__endswith='s')                  
    # query = Queryset.objects.filter(id__range=(2,10))                  
    # query = Queryset.objects.exclude(Q(id=8)&Q(name='Bruce'))            
    return render(request,'core/queryset.html',{'query':query})