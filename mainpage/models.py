from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    second_phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about = models.TextField(blank=True)

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Language', 'Programming Language'),
        ('Framework', 'Framework'),
        ('Database', 'Database'),
        ('Technology', 'Technology'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True, null=True)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Education(models.Model):
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='educations')

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='work_experiences')
