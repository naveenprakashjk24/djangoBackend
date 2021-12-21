from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DO_NOTHING


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, max_length=200)
    phone = models.CharField(max_length=200, null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class ProjectContractor(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectStage(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectStagesMapping(models.Model):
    site_name = models.CharField(max_length=200)
    phase_id = models.IntegerField(null=False)
    stage_id = models.ForeignKey(ProjectStage, on_delete=models.DO_NOTHING)
    sensor_count = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.site_name + ' ' + str(self.stage_id)


class ProjectDailyupdates(models.Model):
    site_name = models.ForeignKey(ProjectStagesMapping, on_delete=DO_NOTHING)
    user_name = models.ForeignKey(User, on_delete=DO_NOTHING, default='')
    plumbing_count = models.IntegerField()
    electrial_count = models.IntegerField()
    commissioning_count = models.IntegerField()
    contractor_name = models.ForeignKey(ProjectContractor, on_delete=DO_NOTHING)
    plumber_count = models.IntegerField()
    helper_count = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


class ProjectAssigningDetails(models.Model):
    site_name = models.ForeignKey(ProjectStagesMapping, on_delete=DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=DO_NOTHING)
    resource_id = models.ForeignKey(ProjectContractor, on_delete=DO_NOTHING)
