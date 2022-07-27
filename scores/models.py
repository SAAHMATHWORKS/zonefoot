from django.db import models
from django.contrib.auth.models import User



TYPE_CARTON = (
    ('ROUGE', 'ROUGE'),
    ('JAUNE', 'JAUNE'),
)



class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    affiliation = models.BooleanField(default=True)
    #mj = models.PositiveIntegerField(default=0)
    #gagne = models.PositiveIntegerField(default=0)
    #nul = models.PositiveIntegerField(default=0)
    #perdu = models.PositiveIntegerField(default=0)
    #bp = models.PositiveIntegerField(default=0)
    #bc = models.PositiveIntegerField(default=0)
    #points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def mj(self):
    	nb_away = self.away_games.filter(game_finished=True).count()
    	nb_home = self.home_games.filter(game_finished=True).count()
    	return nb_home + nb_away


    @property
    def gagne(self):
    	win_away = 0
    	win_home = 0

    	for m in self.away_games.filter(game_finished=True):
    		if m.away_goals > m.home_goals:
    			win_away +=1
    	for m in self.home_games.filter(game_finished=True):
    		if m.home_goals > m.away_goals:
    			win_home +=1
    	return win_home + win_away

    @property
    def perdu(self):
    	lost_away = 0
    	lost_home = 0

    	for m in self.away_games.filter(game_finished=True):
    		if m.away_goals < m.home_goals:
    			lost_away +=1
    	for m in self.home_games.filter(game_finished=True):
    		if m.home_goals < m.away_goals:
    			lost_home +=1
    	return lost_home + lost_away

    @property
    def nul(self):
    	nul_away = 0
    	nul_home = 0

    	for m in self.away_games.filter(game_finished=True):
    		if m.home_goals == m.away_goals:
    			nul_away +=1
    	for m in self.home_games.filter(game_finished=True):
    		if m.away_goals == m.home_goals:
    			nul_home +=1
    	return nul_home + nul_away


    @property
    def points(self):
    	return self.gagne*3 + self.nul


    @property
    def bp(self):
    	bp_away = 0
    	bp_home = 0

    	for m in self.home_games.filter(game_finished=True):
    		bp_home += m.home_goals
    	for m in self.away_games.filter(game_finished=True):
    		bp_away += m.away_goals
    	return bp_away + bp_home

    @property
    def bc(self):
    	bc_away = 0
    	bc_home = 0

    	for m in self.home_games.filter(game_finished=True):
    		bc_home += m.away_goals
    	for m in self.away_games.filter(game_finished=True):
    		bc_away += m.home_goals
    	return bc_away + bc_home


    @property
    def db(self):
    	return self.bp - self.bc


   




class Fixture(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"





class Player(models.Model):
    name = models.CharField(max_length=128, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    affiliation = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def totalbut(self):
        return But.objects.filter(player_id=self.id).count()





class But(models.Model):
    match = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player.name + " marque à la " + str(self.minute) + " minute"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    text = models.TextField()
    #parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " ---Message---> " + self.text[:15]




class Carton(models.Model):
    match = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type_carton = models.CharField(choices=TYPE_CARTON, max_length=7)
    paye = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.player.name + " carton: " + self.type_carton