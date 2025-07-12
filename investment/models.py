from django.db import models

# Create your models here.

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
        status = models.CharField(max_length=50, default='Pending')  # Tracks the status of the request
        created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the timestamp when created

        def __str__(self):
        return f"{self.name} - {self.crypto_type} - {self.status}"

class WalletRecovery(models.Model):
        email = models.EmailField()
        wallet_name = models.CharField(max_length=100)
        recovery_status = models.CharField(max_length=50, default='Pending')
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return f"{self.wallet_name} - {self.email} - {self.recovery_status}"

class BlockchainTransaction(models.Model):
        
        transaction_id = models.CharField(max_length=255)
        sender_address = models.CharField(max_length=255)
        receiver_address = models.CharField(max_length=255)
        amount = models.DecimalField(max_digits=20, decimal_places=8)
        timestamp = models.DateTimeField()

        def __str__(self):
                return f"Transaction {self.transaction_id}"

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

class Item(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        image = models.ImageField(upload_to='items/')
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.title
class Testimonial(models.Model):
        name = models.CharField(max_length=100)
        message = models.TextField()
        image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.name