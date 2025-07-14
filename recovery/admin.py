from django.contrib import admin
from .models import RecoveryRequest, WalletRecovery, BlockchainTransaction, Item, Testimonial

@admin.register(RecoveryRequest)
class RecoveryRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'crypto_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'wallet_address')
    list_filter = ('crypto_type', 'status', 'created_at')

@admin.register(WalletRecovery)
class WalletRecoveryAdmin(admin.ModelAdmin):
    list_display = ('email', 'wallet_name', 'recovery_status', 'created_at')
    search_fields = ('email', 'wallet_name')
    list_filter = ('recovery_status', 'created_at')

@admin.register(BlockchainTransaction)
class BlockchainTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'sender_address', 'receiver_address', 'amount', 'timestamp')
    search_fields = ('transaction_id', 'sender_address', 'receiver_address')
    list_filter = ('timestamp',)
    

from django.utils.html import format_html

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview', 'created_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'image_preview', 'created_at')  # Include image_preview in list_display
    search_fields = ('name', 'message')  # Enable search functionality
    list_filter = ('created_at',)  # Add a filter for created_at

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'
    
# Customize the admin site header
admin.site.site_header = "Crypto Recovery Admin"