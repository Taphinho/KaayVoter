from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Candidat
from accounts.models import User
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def vote(request):
    candidats = Candidat.objects.all().order_by("id")
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)
    
    if request.method == "POST":
        print(user.dejaVote)
        if user.dejaVote == False :
            value = request.POST.get('candidatId')
            candidat = get_object_or_404(Candidat, pk=value)
            print(candidat.nbrvote)
            candidat.nbrvote += 1
            candidat.save()
            user.dejaVote = True
            user.save()
            response_data = {
            'success': True,
            'message': 'Vote enregistré avec succès !',
        }
            return JsonResponse(response_data)
        else:
            response_data = {
            'success': False,
            'message': 'Vous Avez deja vote',
        }
            print("wesh")
            return JsonResponse(response_data)


    return render(request, 'vote.html', {"candidats":candidats})

def vote_success(request):
    return render(request, 'vote_success.html',{})
def error(request):
    return render(request,'vote_error.html',{})