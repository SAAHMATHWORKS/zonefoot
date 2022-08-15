from django.shortcuts import render
from .models import *

# Create your views here.



def coupe(request):
    teamsA = sorted(TeamA.objects.all(), key=lambda t: (-t.points, -t.db)) #.order_by('-points')
    teamsB = sorted(TeamB.objects.all(), key=lambda t: (-t.points, -t.db)) #.order_by('-points')

    matchA = PouleA.objects.all().order_by('-date')

    matchB = PouleB.objects.all().order_by('-date')

    df = DemiFinal.objects.all().order_by('-date')

    demifinalprogram = True
    if not df:
    	demifinalprogram = False

    context = {'teamsA': teamsA, 'teamsB': teamsB, 'matchA': matchA, 'matchB': matchB, 
    			'df': df, 'demifinalprogram': demifinalprogram}


    return render(request, 'coupe/coupe.html', context)
    