from django.shortcuts import render, get_object_or_404


from profiles.models import UserProfile
from .models import ComunityMessages
from .forms import MessageForm

# Create your views here.


def comunity(request):
    """ 
    Renders comunity page
    """

    title = ComunityMessages.objects.all()

    if request.method == "POST":
        form_data = {
            'username': request.POST['message_username'],
            'title': request.POST['message_title'],
            'message_content': request.POST['message_content'],
        }

        message_form = MessageForm(form_data)
        # saves the message
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.save()

            username = get_object_or_404(UserProfile, user=request.user)

            template = 'comunity/comunity.html'

            context = {
                'title': title,
                'username': username,
            }

            return render(request, template, context)
    else:
        # if user is registered poasses user name
        if request.user.is_authenticated:
            username = get_object_or_404(UserProfile, user=request.user)

            template = 'comunity/comunity.html'

            context = {
                'title': title,
                'username': username,
            }

            return render(request, template, context)
        else:
            template = 'comunity/comunity.html'

            context = {
                'title': title,
            }

            return render(request, template, context)
