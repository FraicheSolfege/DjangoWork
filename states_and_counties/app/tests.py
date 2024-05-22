from django.test import TestCase
from app import models as s
# Create your tests here.

class TestCases(TestCase):
    def test_create_state(self):
        ms = s.create_state("Mississippi", "MS", "Magnolia", "Jackson")
        oh = s.create_state("Ohio", "OH", "Scarlet Carnation", "Columbus")

        self.assertEqual(ms.name, "Mississippi")
        self.assertEqual(ms.abbreviation, "MS")
        self.assertEqual(ms.flower, "Magnolia")
        self.assertEqual(ms.capital, "Jackson")

        self.assertEqual(oh.name, "Ohio")
        self.assertEqual(oh.abbreviation, "OH")
        self.assertEqual(oh.flower, "Scarlet Carnation")
        self.assertEqual(oh.capital, "Columbus")
    
    def test_create_county(self):
        ms = s.create_state("Mississippi", "MS", "Magnolia", "Jackson")
        oh = s.create_state("Ohio", "OH", "Scarlet Carnation", "Columbus")
        hinds = s.create_county("Hinds", "Jackson", 245285, ms)
        franklin = s.create_county("Franklin", "Columbus", 1163414, oh)

        self.assertEqual(hinds.name, "Hinds")
        self.assertEqual(hinds.county_seat, "Jackson")
        self.assertEqual(hinds.population, 245285)
        self.assertEqual(hinds.state, ms)

    def test_find_counties_for_state(self):
        ms = s.create_state("Mississippi", "MS", "Magnolia", "Jackson")
        oh = s.create_state("Ohio", "OH", "Scarlet Carnation", "Columbus")
        hinds = s.create_county("Hinds", "Jackson", 245285, ms)
        franklin = s.create_county("Franklin", "Columbus", 1163414, oh)
        lafayette = s.create_county("Lafayette", "Oxford", 25713, ms)

        counties_in_ms = s.find_counties_for_state("MS")
        self.assertEqual(len(counties_in_ms), 2)

    def test_state_population(self):
        ms = s.create_state("Mississippi", "MS", "Magnolia", "Jackson")
        oh = s.create_state("Ohio", "OH", "Scarlet Carnation", "Columbus")
        hinds = s.create_county("Hinds", "Jackson", 1, ms)
        franklin = s.create_county("Franklin", "Columbus", 1163414, oh)
        lafayette = s.create_county("Lafayette", "Oxford", 2, ms)

        total_population_of_ms = s.state_population("Mississippi")
        self.assertEqual(total_population_of_ms, 3)

    def test_counties_containing_state_capital(self):
        ms = s.create_state("Mississippi", "MS", "Magnolia", "Jackson")
        oh = s.create_state("Ohio", "OH", "Scarlet Carnation", "Columbus")
        hinds = s.create_county("Hinds", "Jackson", 1, ms)
        lafayette = s.create_county("Lafayette", "Oxford", 2, ms)

        capital_city = s.counties_containing_state_capital()
        print(capital_city)
        self.assertEqual(len(capital_city), 1)
