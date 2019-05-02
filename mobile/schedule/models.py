from django.db import models





#Speaker's class
class Speaker(models.Model):
    speaker_title = models.CharField(max_length = 50, default='')
    speaker_name = models.CharField(max_length = 50, default='')
    # conference_paper = models.ForeignKey('Event', related_name='conferencetitle', on_delete=models.CASCADE)
    biography = models.TextField(max_length = 1000)
    twitter = models.CharField(max_length = 16, blank = True)
    facebook = models.CharField(max_length = 50, blank = True)
    def __str__(self):
        return self.speaker_name

#Event Model
class Event(models.Model):
    conference_paper = models.CharField(max_length=100, default='')
    conference_title = models.CharField(max_length=100, default='')
    upload_paper = models.FileField()
    proceeding_paper_title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    speaker_name = models.ForeignKey(Speaker, related_name='speakername', on_delete=models.CASCADE, default='')
    other_authors = models.CharField(max_length=100, default='')
    conference_location = models.CharField(max_length=100, default='')
    conference_start_date = models.DateField(default=2019-12-13)
    conference_end_date = models.DateField(default=2019-12-13)
    place_of_publication = models.CharField(blank=True, max_length=100)
    online_link = models.URLField(default='')

    def __str__(self):
        return self.conference_title

#AGENDA REQUIREMENTS
class Agenda(models.Model):
    documentary_on_cpn = models.CharField(max_length=255)
    agenda_title = models.ForeignKey(Event, related_name='agendas', on_delete=models.CASCADE)
    arrival_and_registraion = models.CharField(max_length=255)
    induction_programme = models.IntegerField()
    welcome_address = models.CharField(max_length=255)
    induction_lectures = models.CharField(max_length=255)
    induction_of_new_members = models.CharField(max_length=255)
    welcome_address_by_president = models.CharField(max_length=150)
    remarks = models.CharField(max_length=200)
    photograph = models.CharField(max_length=255)
    documentary_on_cpn = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    annual_general_meeting = models.CharField(max_length=255)
    dinner_and_presentation_of_awards_and_certificate = models.CharField(
        max_length=255)

    def __str__(self):
        return self.documentary_on_cpn

#Type of Membership
class TypeOfMembership(models.Model):
    membership_type = models.CharField(max_length=150)

    def __str__(self):
        return self.membership_type

#Membership class
class Membership(models.Model):
    membership_Registration_Number = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150, default='')
    email = models.EmailField()
    entry_types = models.ForeignKey(TypeOfMembership, related_name='membersentry', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


