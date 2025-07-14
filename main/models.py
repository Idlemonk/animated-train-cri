from django.db import models

class RecoveryRequest(models.Model):
        CRYPTO_CHOICES = [
                ('BTC', 'Bitcoin'),
                ('ETH', 'Ethereum'),
                ('USDT', 'Tether'),
                ('BNB', 'Binance Coin'),
                ('ADA', 'Cardano'),
                ('XRP', 'Ripple'),
                ('DOGE', 'Dogecoin'),
                ('OTHER', 'Other'),
        ]
        name = models.CharField(max_length=100)
        email = models.EmailField()
        wallet_address = models.CharField(max_length=255)
        crypto_type = models.CharField(max_length=10, choices=CRYPTO_CHOICES)
        issue_description = models.TextField()
        status = models.CharField(max_length=50, default='Pending')
        created_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return f"{self.name} - {self.crypto_type} - {self.status}"

class Contact(models.Model):
        RECOVERY_TYPES = [
                ('wallet', 'Wallet Recovery'),
                ('crypto', 'Cryptocurrency Recovery'),
                ('other', 'Other'),
        ]
        name = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=15, blank=True, null=True)
        country = models.CharField(max_length=100, blank=True, null=True)
        type_of_recovery = models.CharField(max_length=50, choices=RECOVERY_TYPES, default='other')
        message = models.TextField()
        privacy_policy = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        def __str__(self):
                return f"{self.name} - {self.type_of_recovery}"
