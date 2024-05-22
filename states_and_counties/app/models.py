from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=2)
    flower = models.CharField(max_length=30)
    capital = models.CharField(max_length=30)

class County(models.Model):
    name = models.CharField(max_length=30)
    county_seat = models.CharField(max_length=50)
    population = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def create_state(name, abbreviation, flower, capital):
    return State.objects.create(name = name, abbreviation = abbreviation, flower = flower, capital = capital)

def create_county(name, county_seat, population, state):
    return County.objects.create(name = name, county_seat = county_seat, population=population, state = state)

def find_counties_for_state(abbreviation):
    return County.objects.filter(state__abbreviation = abbreviation)

def state_population(state):
    counties = County.objects.filter(state__name = state)
    population = 0
    for county in counties:
        population += county.population

    return population

def counties_containing_state_capital():
    counties = County.objects.all()
    capital_county = []
    for county in counties:
        if county.county_seat == county.state.capital:
            capital_county.append(county)

    return capital_county