from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.db.models import Q
from django.core.serializers import serialize
from django.core.serializers import deserialize
from .models import Properties  
from random import sample

def home(request):
    if request.method == 'POST':
        search = request.POST.get("search")
        if search:
            try:
                instance = Properties.objects.filter(Q(name__icontains=search) | Q(address__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search))
                if (len(instance) == 1):
                    return redirect(reverse("property") + f"?p={instance[0].id}")
                elif(len(instance)==0):
                    raise Properties.DoesNotExist
                else:
                    serialized_instances = serialize('json', instance)
                    return redirect(reverse("property_list") + f"?instances={serialized_instances}")
            except Properties.DoesNotExist:
                return redirect(reverse("null") + f"?search={search}")    
    random_properties = sample(list(Properties.objects.all()), 3)   
    return render(request, 'home.html', {'randoms': random_properties})

def index(request):
    instance_id = request.GET.get('p', '')
    
    instance = get_object_or_404(Properties, id=instance_id)
    return render(request, "index.html", {"p": instance})
    
def null_view(request):
    search = request.GET.get('search', '')
    
    return render(request, "null.html", {"search": search})

def index2(request):
    serialized_instances = request.GET.get('instances', '')
    instances = list(deserialize('json', serialized_instances))
    
    if request.method == "POST":
        property_id = request.POST.get("property_id")
        if property_id:
            return redirect(reverse("property") + f"?p={property_id}")  
        
    return render(request, "index2.html", {"instances": instances})


