from django.contrib import admin
from .models import PersonalInfo, Education, WorkExperience, Skill


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'second_phone', 'address')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('address',)
    fieldsets = (
        ("Basic Information", {
            'fields': ('full_name', 'email', 'phone', 'second_phone', 'address', 'profile_picture', 'about'),
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'personal_info')
    search_fields = ('name', 'category', 'proficiency', 'personal_info__full_name')
    list_filter = ('category', 'proficiency')
    autocomplete_fields = ('personal_info',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'field_of_study', 'start_date', 'end_date', 'personal_info')
    search_fields = ('school_name', 'degree', 'field_of_study', 'personal_info__full_name')
    list_filter = ('degree', 'field_of_study', 'start_date', 'end_date')
    autocomplete_fields = ('personal_info',)

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'personal_info')
    search_fields = ('job_title', 'company', 'description', 'personal_info__full_name')
    list_filter = ('company', 'start_date', 'end_date')
    autocomplete_fields = ('personal_info',)
