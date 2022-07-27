from django.shortcuts import render,  redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def fixtures(request):
    fixtures = Fixture.objects.all()

    #all_completed = all(f.game_finished for f in fixtures)

    context = {
        'fixtures': fixtures,
        #'all_completed': all_completed
    }

    
    return render(request, 'fixtures.html', context)




def classement(request):
    matchs = Fixture.objects.filter(game_finished=True)
    teams = sorted(Team.objects.all(), key=lambda t: (-t.points, -t.db)) #.order_by('-points')
    nb_matchs = matchs.count()
    context = {'nb_matchs': nb_matchs, 'teams': teams}
    return render(request, 'classement.html', context)





def clsbuteurs(request):
    buteurs = sorted(Player.objects.all(), key=lambda t: -t.totalbut)

    context={'buteurs': buteurs}

    return render(request, 'buteurs.html', context)




@login_required
def fixture_detail(request, id):
    fixture = get_object_or_404(Fixture, pk=id)

    home_team = fixture.home_team
    away_team = fixture.away_team

    home_team_buts = But.objects.filter(match = fixture, player__team = home_team)

    away_team_buts = But.objects.filter(match = fixture, player__team = away_team)

    #cartons = Carton.objects.filter(match = fixture)
    home_team_cartons = Carton.objects.filter(match = fixture, player__team = home_team)

    away_team_cartons = Carton.objects.filter(match = fixture, player__team = away_team)

    comments = Comment.objects.filter(match = fixture).order_by('-created_at')
    paginator = Paginator(comments, 20)
    page = request.GET.get('page', 1)
    comments = paginator.get_page(page)

    context={'home_team_buts': home_team_buts, 'away_team_buts': away_team_buts, 'away_team_cartons': away_team_cartons, 
    'home_team_cartons':home_team_cartons, 'fixture': fixture, 'comments': comments}

    return render(request, 'fixture_detail.html', context)


def addMessage(request):
    if request.method=="POST":
        comment=request.POST['comment']
        fixture_id=request.POST['fixtureid']
        fixture = get_object_or_404(Fixture, pk=fixture_id)
        
        newMessage = Comment(text=comment, user=request.user, match=fixture)
        newMessage.save()
        messages.success(request, 'Merci pour votre commentaire !!!')
        return redirect('fixture_detail', id=fixture_id)



def cards(request):
    cartons = Carton.objects.all()
    context = {'cartons': cartons}
    return render(request, 'cartons.html', context)

