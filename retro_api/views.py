### Sign Up and login with confirmation Email ### 
from io import StringIO
from django.conf import UserSettingsHolder, settings
from django.contrib.sites.models import Site
from django.db import reset_queries
from django.http import request, response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import get_user, login,authenticate, tokens
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes , force_text
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .models import InvitationRetroUser, Project, RetroUser
from django.core.mail import EmailMessage, message, send_mail
from django.db.models import Q
import string
import random
from teamretro import settings



### Api View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema


# Create your views here.



def home(request):
    return render(request,'home.html')

class CustomAuthentication(APIView):
    def post(self,request):
        print('post')
        #get username and password 
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        if not email or not password:
            return Response({'status': 'Failed','message': 'No credentials provided '},
                            status=status.HTTP_401_UNAUTHORIZED)

        domain = Site.objects.all()[0].domain

        credentials = {
            RetroUser.EMAIL_FIELD: email,
            'password':password,
        }

        user =authenticate(username=email, password=password)


        if user is None:
            return Response({'status':'Failed', 'Message':'Incorrect username or password'},
                            status= status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({'status' : 'Failed' , 'Message' : 'User is not active Please check email is activate.'},
                            status = status.HTTP_401_UNAUTHORIZED)

        token ,created = Token.objects.get_or_create(user=user)

        get_user = RetroUser.objects.filter(id=user.id).select_related('login_provider_id').values('id','first_name','email','login_provider_id','last_name','profile_pic').first()
        user_obj = {}
        user_obj['first_name']=get_user['first_name']
        user_obj['last_name']=get_user['last_name']
        user_obj['email'] = get_user['email']

        if get_user['profile_pic'] and len(get_user['profile_pic'])>0:
            user_obj['profile_pic'] = domain+settings.MEDIA_URL+get_user['profile_pic']
        else:
            user_obj['profile_pic'] = None
        
        return Response({'status':"Success","Key":token.key, "user":user_obj},
                        status=status.HTTP_200_OK)


class CustomSignup(APIView):
    def post(self,request):
        #get username and password 
        password = request.data.get('password',None)
        email = request.data.get('email',None)
        first_name = request.data.get('first_name',None)
        last_name = request.data.get('last_name',None)

        # check if the email and password is valid or not
        if not email or not password:
            return Response({'status': 'Failed','message': 'Email or Password is not provided '},
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        current_site = get_current_site(request)            

        # Creating a user 
        user = RetroUser.objects.create(
        username=email,
        email=email,
        first_name = first_name,
        last_name = last_name

        )
        user.set_password(str(password))
        user.is_active=False
        user.save()


        message = render_to_string('acc_active_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            # Sending Activation link in terminal
            # user.email_user(subject,message)
        mail_subject = 'Activate your your account'
        to_email = user
        email = EmailMessage(mail_subject,message,to=[to_email])
        email.send()
        return Response({"status":"Please check your email address to complete email varification "},status=status.HTTP_201_CREATED)



def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = RetroUser.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,RetroUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(request,user)
        return HttpResponse('Thank you for email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is Invalid !! ')



class TeamMemberInviteView(APIView):

    def post(self,request):
        email_id = RetroUser.objects.filter(Q(email=request.data.get("email")) | Q(username = request.data.get("email"))).first()
        print("here")
        if not email_id:
            print("inside if ")
            token = ''.join(random.choices(string.ascii_uppercase+string.digits, k=10))
            print("token created ")
            invite =  InvitationRetroUser.objects.create(
                invitation_code = token,
                email = request.data.get("email"),
                first_name =request.data.get("first_name"),
                status = "Pending"
            )
            print("f_name added")
            invite.save()
            print("Invite Saved")

            if invite :
                #send email
                print("If invited")
                domain = Site.objects.all()[0].domain
                subject ="Invitation - ReleaseDoc App"
                message = "Welcome to RelaseDoc App,Click on the link below to accept the invitation"+domain+"/api/accept-Invitation?token="+token
                email_from = settings.EMAIL_HOST
                recipient_list = [request.data.get("email"),]
                send_mail(subject , message,email_from,recipient_list)

                invites = InvitationRetroUser.objects.filter(email=request.data.get('email'))
                print(" user invited")

                return Response({"status":list(invites)},status=status.HTTP_200_OK)

            else:
                return Response({"status":"failed"},status=status.HTTP_200_OK)

class AcceptInvitationApiView(APIView):

    def get(self,request):
        token = request.query_parms.get('token')
        invitation = InvitationRetroUser.objects.filter(invitations_code = token).first()

        if not invitation:
            return Response({"status":"Invitation not present"},
                                status=status.HTTP_400_BAD_REQUEST)

        email_id = RetroUser.objects.filter(Q(email = invitation.email) | Q(username = invitation.email)).first()

        if email_id:

            try:
                get_details = InvitationRetroUser.objects.filter(invitation_code=token)

            except:

                return Response({"status":"Invitation Already Accepted "},status = status.HTTP_208_ALREADY_REPORTED)        

            return Response({"status":"Invitation Already Accepted"},status = status.HTTP_208_ALREADY_REPORTED)

        
