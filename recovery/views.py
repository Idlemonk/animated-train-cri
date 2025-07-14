from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RecoveryRequest, WalletRecovery, BlockchainTransaction, Contact
from .schemas import (
    RecoveryRequestSchema,
    ContactSchema,
)
from pydantic import ValidationError

def submit_recovery_request(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = RecoveryRequestSchema(**data)
            RecoveryRequest.objects.create(**validated.dict(exclude={'created_at'}))
            messages.success(request, 'Your recovery request has been submitted successfully!')
            return redirect('recovery:home')  # Adjust to correct URL name
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    return render(request, 'recovery/submit_request.html', {'title': 'Submit Recovery Request'})

def wallet_recovery_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = WalletRecoverySchema(**data)
            WalletRecovery.objects.create(**validated.dict(exclude={'created_at'}))
            messages.success(request, 'Wallet recovery request submitted!')
            return redirect('recovery:wallet_recovery')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    return render(request, 'recovery/wallet_recovery.html', {'title': 'Wallet Recovery'})

def blockchain_transaction_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = BlockchainTransactionSchema(**data)
            BlockchainTransaction.objects.create(**validated.dict(exclude={'timestamp'}))
            messages.success(request, 'Transaction logged successfully!')
            return redirect('recovery:blockchain_transaction')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    return render(request, 'recovery/blockchain_transaction.html', {'title': 'Blockchain Transaction'})

def contact_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = ContactSchema(**data)
            Contact.objects.create(**validated.dict(exclude={'created_at'}))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('recovery:contact')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    return render(request, 'recovery/contact.html', {'title': 'Contact'})
