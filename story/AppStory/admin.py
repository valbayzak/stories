from django.contrib import admin
from .models import Project, Story, StoryFile, UserStoryFile, User
# Register your models here.
admin.site.register(Project)
admin.site.register(Story)
admin.site.register(StoryFile)
admin.site.register(UserStoryFile)
admin.site.register(User)