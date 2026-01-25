from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet

# Create your views here.
@login_required
def dashboard(request):
    wallet, created = Wallet.objects.get_or_create(user = request.user)
    return render(request, 'dashboard/dashboard.html', {'wallet': wallet})