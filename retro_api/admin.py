from django.contrib import admin
from .models import (RetroUser,LoginProvider,RetroUserRole,InvitationRetroUser,Retrospective,RetroStage,
                        RetroAction,RetroTopic,Report,RetroColumn,RetrospectiveCollaborator,RetroTopicComment,
                        Template ,TemplateColumn,Status,ColumnList,Organization,Project)


# Register your models here.

admin.site.register(RetroUser)
admin.site.register(LoginProvider)
admin.site.register(RetroUserRole)
admin.site.register(InvitationRetroUser)
admin.site.register(RetroColumn)
admin.site.register(Retrospective)
admin.site.register(RetrospectiveCollaborator)
admin.site.register(RetroStage)
admin.site.register(RetroAction)
admin.site.register(RetroTopic)
admin.site.register(Report)
admin.site.register(RetroTopicComment)
admin.site.register(Template)
admin.site.register(TemplateColumn)
admin.site.register(Status)
admin.site.register(ColumnList)
admin.site.register(Organization)
admin.site.register(Project)
