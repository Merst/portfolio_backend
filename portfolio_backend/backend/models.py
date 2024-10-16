from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the technical skill.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


# Enumeration of technical skills related to a project.
class Skill(models.Model):
    name = models.CharField(max_length=100, help_text='Enter the name of the technical skill.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill, help_text='Select the appropriate related technical skills')
    summary = models.TextField(max_length=2500, help_text='Enter a brief description of the project')
    github_link = models.URLField()
    older_project = models.BooleanField(default=False)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
