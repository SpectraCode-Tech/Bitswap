from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet
from transactions.models import Transaction
from .utils import get_all_crypto_rates

# Create your views here.
@login_required
def dashboard(request):
    wallet, created = Wallet.objects.get_or_create(user = request.user)
    transactions = Transaction.objects.filter(user = request.user).order_by('-created_at')
    crypto_rates = get_all_crypto_rates
    return render(request, 'dashboard/dashboard.html', 
                  {'wallet': wallet, 
                   'transactions': transactions,
                   'crypto_rates': crypto_rates})