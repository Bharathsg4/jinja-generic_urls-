from django.shortcuts import render

# Create your views here.
def Team_India(request):
    D={'player1':'MR.COOL','player2':'HITMAN'}
    return render(request,'Team_India.html',context=D)