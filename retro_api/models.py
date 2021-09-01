from django.db import models
from django.db.models.fields import related
from django.db.models.fields.json import JSONField
from django.contrib.auth.models import AbstractUser
import time



# Create your models here.
class BaseModel(models.Model):
    """
    Base Model with created_at, and modified_at fields, will be inherited
    in all other models.
    """

    meta_created_ts = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name=("Meta Created TimeStamp"),
        null=True,
        blank=True,
    )
    meta_updated_ts = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name=("Meta Updated TimeStamp"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

class LoginProvider(BaseModel):
    name = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField()
    is_deleted = models.BooleanField()
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)


class RetroUserRole(BaseModel):
    access_permission = JSONField()
    description = models.CharField(max_length=200,null=True)
    is_deleted = models.BooleanField()
    role_type = models.CharField(max_length=255,null=True)


def user_profile_picture(instance, filename):
    filebase, extension = filename.split('.')
    return 'user_profile_picture/%s.%s' % ( str(int(round(time.time() * 1000))), extension)

class RetroUser(AbstractUser):
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    profile_pic = models.ImageField(upload_to=user_profile_picture,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    retro_user_role_id= models.ForeignKey(RetroUserRole,on_delete=models.DO_NOTHING,null=True,related_name="retrouserrole")
    login_provider_id=models.ForeignKey(LoginProvider,on_delete=models.DO_NOTHING,null=True,related_name="loginprovider")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class InvitationRetroUser(BaseModel):
    invitation_code = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,default=True)
    first_name =models.CharField(max_length=255,default=True)
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retros_user')
    invitation_status = models.CharField(max_length=255, choices=[("Notsent","Notsent"),("Pending","Pending"),("Accepted","Accepted"),("Cancelled","Cancelled"),],default="Notsent")
    is_email_sent = models.BooleanField(default=False)

class Template(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.BooleanField()
    is_published = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retro_user_id')

class RetroStage(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    sequence = models.IntegerField()
    is_active = models.BooleanField()

class Organization(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retrouser_id')


class Project(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    organization_id = models.ForeignKey(Organization,models.DO_NOTHING,blank=True,null=True,related_name='organization')
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retrouser')

    
class Retrospective(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    is_anonymous = models.BooleanField()
    sprint_title = models.CharField(max_length=255,blank=True,null=True)
    sprint_start_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    sprint_end_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    template_id = models.ForeignKey(Template,models.DO_NOTHING,null=True,blank=True,related_name='template_id')
    retro_stage_id = models.ForeignKey(RetroStage,models.DO_NOTHING,null=True,blank=True,related_name='retrostage')
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retro_users_id')
    project_id = models.ForeignKey(Project,models.DO_NOTHING,null=True,blank=True,related_name='project')

class RetrospectiveCollaborator(BaseModel):
    retrospective_id = models.ForeignKey(Retrospective , models.DO_NOTHING,null=True,blank=True,related_name='retrospectivee_id')
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retro_user_idd')

class Report(BaseModel):
    retrospective_id = models.ForeignKey(Retrospective , models.DO_NOTHING,null=True,blank=True,related_name='retrospective')

class Status(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)


class ColumnList(BaseModel):
    name = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.BooleanField()


class TemplateColumn(BaseModel):
    sequence = models.IntegerField()
    vote = models.BooleanField()
    comment = models.BooleanField()
    reaction = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    column_list_id = models.ForeignKey(ColumnList,models.DO_NOTHING,null=True,blank=True,related_name='column_list')
    template_id = models.ForeignKey(Template,models.DO_NOTHING,null=True,blank=True,related_name='template')

class RetroColumn(BaseModel):
    sequence = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    vote = models.BooleanField()
    comment = models.BooleanField()
    reaction = models.BooleanField()
    retrospective_id = models.ForeignKey(Retrospective,models.DO_NOTHING,null=True,blank=True,related_name='retrospectivee')
    column_list_id = models.ForeignKey(ColumnList,models.DO_NOTHING,null=True,blank=True,related_name='columnlist')

class RetroTopic(BaseModel):
    sequence = models.IntegerField()
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    retrospective_id = models.ForeignKey(Retrospective,models.DO_NOTHING,null=True,blank=True,related_name='retrospective_id')
    retro_column_id = models.ForeignKey(RetroColumn,models.DO_NOTHING,null=True,blank=True,related_name='retrocolumn')
   
class RetroTopicComment(BaseModel):
    description = models.CharField(max_length=255,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_anonymous = models.BooleanField()
    retro_topic_id= models.ForeignKey(RetroTopic,models.DO_NOTHING,blank=True,null=True,related_name='retro_topic')
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,blank=True,null=True,related_name='retro_user')


class RetroAction(BaseModel):
    description = models.CharField(max_length=255,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    estimate_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    status_id = models.ForeignKey(Status,models.DO_NOTHING,null=True,blank=True,related_name='status')
    retrospective_id = models.ForeignKey(Retrospective,models.DO_NOTHING,null=True,blank=True,related_name='retrospect_id')
    retro_topic_id = models.ForeignKey(RetroTopic,models.DO_NOTHING,null=True,blank=True,related_name='retrotopic')
    retro_user_id = models.ForeignKey(RetroUser,models.DO_NOTHING,null=True,blank=True,related_name='retro_users')






