from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class TeamA(models.Model):
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

    class Meta:
        verbose_name_plural = "TeamA"

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


   




class PouleA(models.Model):
    home_team = models.ForeignKey(TeamA, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(TeamA, on_delete=models.CASCADE, related_name='away_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


    class Meta:
        verbose_name_plural = "Match PouleA"



class TeamB(models.Model):
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

    class Meta:
        verbose_name_plural = "TeamB"

    @property
    def mj(self):
    	nb_away = self.baway_games.filter(game_finished=True).count()
    	nb_home = self.bhome_games.filter(game_finished=True).count()
    	return nb_home + nb_away


    @property
    def gagne(self):
    	win_away = 0
    	win_home = 0

    	for m in self.baway_games.filter(game_finished=True):
    		if m.away_goals > m.home_goals:
    			win_away +=1
    	for m in self.bhome_games.filter(game_finished=True):
    		if m.home_goals > m.away_goals:
    			win_home +=1
    	return win_home + win_away

    @property
    def perdu(self):
    	lost_away = 0
    	lost_home = 0

    	for m in self.baway_games.filter(game_finished=True):
    		if m.away_goals < m.home_goals:
    			lost_away +=1
    	for m in self.bhome_games.filter(game_finished=True):
    		if m.home_goals < m.away_goals:
    			lost_home +=1
    	return lost_home + lost_away

    @property
    def nul(self):
    	nul_away = 0
    	nul_home = 0

    	for m in self.baway_games.filter(game_finished=True):
    		if m.home_goals == m.away_goals:
    			nul_away +=1
    	for m in self.bhome_games.filter(game_finished=True):
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

    	for m in self.bhome_games.filter(game_finished=True):
    		bp_home += m.home_goals
    	for m in self.baway_games.filter(game_finished=True):
    		bp_away += m.away_goals
    	return bp_away + bp_home

    @property
    def bc(self):
    	bc_away = 0
    	bc_home = 0

    	for m in self.bhome_games.filter(game_finished=True):
    		bc_home += m.away_goals
    	for m in self.baway_games.filter(game_finished=True):
    		bc_away += m.home_goals
    	return bc_away + bc_home


    @property
    def db(self):
    	return self.bp - self.bc


   




class PouleB(models.Model):
    home_team = models.ForeignKey(TeamB, on_delete=models.CASCADE, related_name='bhome_games')
    away_team = models.ForeignKey(TeamB, on_delete=models.CASCADE, related_name='baway_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


    class Meta:
        verbose_name_plural = "Match PouleB"




class DemiFinal(models.Model):
    home_team = models.ForeignKey(TeamA, on_delete=models.CASCADE, related_name='dhome_games')
    away_team = models.ForeignKey(TeamB, on_delete=models.CASCADE, related_name='daway_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
