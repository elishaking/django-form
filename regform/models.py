from django.db import models
from django.contrib import admin
from multiselectfield import MultiSelectField


# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField("Full name:", max_length=60)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField("Gender:", max_length=1, choices=GENDER, blank=True)
    MARITAL_STATUS = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widow'),
        ('W', 'Widower'),
        ('Se', 'Separated'),
    )
    marital_status = models.CharField("Marital Status:", max_length=2, choices=MARITAL_STATUS, blank=True)
    phone = models.CharField("Phone:", max_length=100, blank=True)
    town = models.CharField("Town:", max_length=100, blank=True)
    lga = models.CharField("LGA:", max_length=100, blank=True)
    state = models.CharField("State of Origin:", max_length=100, blank=True)
    email = models.EmailField("Email Address: (example: abc@example.com)", max_length=200, blank=True)
    residence = models.CharField("Home Address:", max_length=300, blank=True)
    name_of_next_of_kin = models.CharField("Name of next of Kin:", max_length=100, blank=True)
    address_of_next_of_kin = models.CharField("Address of next kin:", max_length=200, blank=True)
    relation_with_next_of_kin = models.CharField("Relationship with next of kin:", max_length=100, blank=True)

    def __str__(self):
        return self.full_name, self.member_id

    def __unicode__(self):
        return self.member_id

    occupation = models.CharField("Occupation:", max_length=100, blank=True)
    business_address = models.CharField("Business Address:", max_length=200, blank=True)
    skills = models.CharField("Skills/Talents:", max_length=100, blank=True)
    sports = models.CharField("Sports:", max_length=100, blank=True)

    def __str__(self):
        return self.occupation

    BAPTIZED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_a_baptized_catholic = models.CharField("Are you a babtized catholic ?", max_length=1, choices=BAPTIZED,
                                                   blank=True)
    not_baptized = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    COMMUNICANT = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_a_communicant = models.CharField("Are you a communicant ? ", max_length=1, choices=COMMUNICANT, blank=True)
    not_communicant = models.CharField("If no, please, state your reasons", max_length=300, blank=True)

    CONFIRMED_CATHOLIC = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_you_confirmed = models.CharField("Are you confirmed ? ", max_length=1, choices=CONFIRMED_CATHOLIC, blank=True)
    not_confirmed = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    WEDDED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    are_wedded_in_the_church = models.CharField("Are you wedded in the church ? ", max_length=1, choices=WEDDED,
                                                blank=True)
    not_wedded = models.CharField("If no, please, state your reasons:", max_length=300, blank=True)

    TRIBAL_COMMUNITY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    any_tribal_community = models.CharField("Do you belong to any tribal communities in the church ? ", max_length=1,
                                            choices=CONFIRMED_CATHOLIC, blank=True)
    not_in_tribal_community = models.CharField("If no, please, state reasons:", max_length=300, blank=True)
    in_tribal_community = models.CharField("If yes, please, state the community:", max_length=300, blank=True)

    PIUS_SOCIETY = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    member_of_any_pius_society = models.CharField("Are you a member of any pius societies in the church ? ",
                                                  max_length=1, choices=PIUS_SOCIETY, blank=True)
    not_in_pius_society = models.CharField("If no, please state your reasons:", max_length=300, blank=True)
    yes_In_pius_society = models.CharField("If yes, please, state the society:", max_length=300, blank=True)

    ORGAN_CHURCH = (
        ('W', 'CWO'),
        ('M', 'CMO'),
        ('C', 'CYON'),
    )
    belongs_to_any_organ_in_church = models.CharField("Do you belong to any of the three organs in the church ?",
                                                      max_length=1, choices=ORGAN_CHURCH, blank=True)
    dont_belong_to = models.CharField("If no, please state reasons:", max_length=300, blank=True)
    yes_belong_to = models.CharField("If yes, please, state your role:", max_length=300, blank=True)

    def __str__(self):
        return self.are_you_a_baptized_catholic

    # def __init__(self):
    #     self.catechetical_work

    CATECHETICAL_WORK = (
        ('Teaching Catechisms', 'Teaching Catechisms'),
        ('Teaching in sunday school', 'Teaching in sunday school'),
        ('Teaching in marriage course', 'Teaching in marriage course'),
        ('Infant Baptism class', 'Infant Baptism class'),
    )

    LITURGICAL_WORK = (
        ('Choir', 'Choir'),
        ('Layreader', 'Proclamation(Layreader/Lector)'),
        ('Church warden', 'Church wardens'),
        ('Alter Service', 'Alter Service'),
    )

    SECURITY_WORK = (
        ('MOD', 'MOD'),
        ('Boys Brigade', 'Boys Brigade'),
        ('Security committee', 'Security committee'),
        ('I am a security personnel', 'I am a security personnel'),
        ('N/A', 'None'),
    )

    ENVIRONMENTAL_WORK = (
        ('Personal church cleaning', 'Personal church cleaning'),
        ('Gardenning', 'Gardenning'),
        ('Societal church cleaning', 'Societal church cleaning'),
        ('Done this in the past', 'I used to clean the church'),
        ('I clean the church', 'I do clean the church'),
        ('None', 'Not apply'),
    )

    HEALTH_WORK = (
        ('Health committee', 'Health committee'),
        ('Medical practitioner', 'Medical practitioner'),
        ('Midwifing', 'Midwifing'),
        ('Not my field', 'Not my occupation'),
        ('Other', 'Other, please specify'),
    )
    other_health_work = models.CharField(max_length=50, blank=True)

    SPORTS = (
        ('Sports committee', 'Sports committee'),
        ('Trainer/Coach', 'Trainer/Coach'),
        ('Umpire', 'Umpire'),
        ('Count me out', 'Count me out'),
        ('Sport team', 'Sport team'),
    )

    OTHER_WORK = (
        ('Harvest and Bazaar', 'Harvest and Bazaar'),
        ('Fund raising', 'Fund raising'),
        ('Building/Project', 'Building/Project'),
        ('Enlightenment and Awareness', 'Enlightenment and Awareness'),
        ('Finance', 'Finance'),
        ('Other', 'Other, please specify'),
    )
    other_other_work = models.CharField(max_length=50, blank=True)

    catechetical_work = MultiSelectField(max_length=100, choices=CATECHETICAL_WORK, blank=True)
    liturgical_work = MultiSelectField(max_length=100, choices=LITURGICAL_WORK, blank=True)
    security_work = MultiSelectField(max_length=100, choices=SECURITY_WORK, blank=True)
    environmental_work = MultiSelectField(max_length=100, choices=ENVIRONMENTAL_WORK, blank=True)
    health_work = MultiSelectField(max_length=100, choices=HEALTH_WORK, blank=True)
    sports = MultiSelectField(max_length=100, choices=SPORTS, blank=True)
    other_work = MultiSelectField(max_length=100, choices=OTHER_WORK, blank=True)
