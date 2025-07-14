from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RecoveryRequest, Contact
from .schemas import RecoveryRequestSchema, ContactSchema
from pydantic import ValidationError

from django.shortcuts import render

def home(request):
    # List of questions and answers
    questions = [
        {"id": 1, "question": "Which recovery plan should I choose?", "answer": "The best recovery plan depends on your financial goals, risk appetite, and timeline. At BlackRock, we offer a variety of options—from conservative portfolios for capital preservation to aggressive growth strategies. Our team can help tailor a plan specifically for you, ensuring your recoverys align with your future vision."},
        {"id": 2, "question": "What are the benefits of investing with BlackRock?", "answer": "Investing with BlackRock gives you access to a global leader in asset management with a proven track record, cutting-edge technology, and a commitment to transparency. You’ll benefit from diversified recovery opportunities, expert insights, and personalized support at every step of your financial journey."},
        {"id": 3, "question": "Do I need to create an account before my recovery process can kick off?", "answer": "Yes, creating an account is the first step to ensure a secure and streamlined recovery process. It enables us to verify your identity, track your case efficiently, and provide real-time updates on your crypto recovery status."},
        {"id": 4, "question": "What are some key statistics about crypto recovery?", "answer": "While recovery outcomes vary by case, statistics show that timely action significantly increases success rates. Over 70% of recoverable cases are resolved when reported within the first 14 days. Our advanced tracing tools and legal partnerships enhance recovery efforts across major blockchains."},
        {"id": 5, "question": "Can I pay directly using cryptocurrency?", "answer": "Absolutely. We accept payments in major cryptocurrencies such as Bitcoin, Ethereum, and USDT. Our secure payment gateway ensures fast and seamless transactions with full encryption and confirmation."},
    ]
    return render(request, 'home.html', {'questions': questions})

def submit_recovery_request(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = RecoveryRequestSchema(**data)
            RecoveryRequest.objects.create(**validated.dict(exclude={'created_at'}))
            messages.success(request, 'Your recovery request has been submitted successfully!')
            return redirect('home')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    else:
        form = RecoveryRequestForm()
    return render(request, 'submit_request.html', {'form': RecoveryRequestForm(), 'title': 'Submit Recovery Request'})

# Track recovery status
def track_status(request):
    if request.method == 'GET':
        request_id = request.GET.get('request_id')
        try:
            recovery_request = RecoveryRequest.objects.get(id=request_id)
            return JsonResponse({
                'status': recovery_request.status,
                'message': recovery_request.message
            })
        except RecoveryRequest.DoesNotExist:
            return JsonResponse({'error': 'Recovery request not found'}, status=404)
    return render(request, 'track_status.html', {'title': 'Track Recovery Status'})

# Wallet recovery
def wallet_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        wallet_name = request.POST.get('wallet_name')
        WalletRecovery.objects.create(email=email, wallet_name=wallet_name, recovery_status="In Progress")
        return render(request, 'wallet_recovery.html', {'success': True})
    return render(request, 'wallet_recovery.html')

# Blockchain explorer
def blockchain_explorer(request):
    transactions = BlockchainTransaction.objects.all()
    return render(request, 'blockchain_explorer.html', {'transactions': transactions})

# About page
def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

# Crypto converter
def crypto_converter(request):
    converted_amount = None
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        rate = float(request.POST.get('rate'))
        converted_amount = amount * rate
    return render(request, 'crypto_converter.html', {'converted_amount': converted_amount})

# News updates
def news_updates(request):
    news = [
        {"title": "Bitcoin Hits New High", "content": "Bitcoin reached a new all-time high today."},
        {"title": "Ethereum 2.0 Launch", "content": "Ethereum 2.0 is set to launch next month."},
    ]
    return render(request, 'news_updates.html', {'news': news})

def contact_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            validated = ContactSchema(**data)
            Contact.objects.create(**validated.dict(exclude={'created_at'}))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        except ValidationError as e:
            messages.error(request, f'Validation error: {e}')
        except Exception as e:
            messages.error(request, f'Error submitting form: {e}')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': ContactForm()})

def write_up(request):
    write_up_content = [
        '''
        <h2>Cryptocurrency Recovery: From Obscurity to Mainstream Adoption</h2>
        <p>In the early days of cryptocurrency, the lack of regulatory oversight and the decentralized nature of the technology made it a prime target for criminal activities, such as money laundering, fraud, and theft. As the cryptocurrency market grew, so did the need for effective ways to recover stolen or misappropriated digital assets.</p>
        ''',
        '''
        <h2>The Emergence of Cryptocurrency Forensics</h2>
        <p>To address these challenges, the cryptocurrency industry has evolved a range of specialized tools and techniques known as "cryptocurrency forensics." These tools leverage the transparency of blockchain technology to trace and analyze transaction flows, identify wallet addresses, and uncover the identities of individuals or entities involved in illicit activities.</p>
        ''',
        '''
        <h2>Collaboration with Regulatory Authorities</h2>
        <p>As the cryptocurrency ecosystem has matured, there has been a growing emphasis on collaboration between the industry and regulatory bodies like the SEC, IRS, and FBI. This partnership has yielded several benefits.</p>
        '''
    ]
    return render(request, 'home.html', {'write_up_content': write_up_content})
