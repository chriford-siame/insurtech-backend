from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from claim.models import Claim

@receiver(pre_save, sender=Claim)
def notify_user_on_status_change(sender, instance, **kwargs):
    if not instance.pk:
        # New record; skip
        print("new entry recorded")
        return

    # Fetch existing object from DB
    try:
        previous = Claim.objects.get(pk=instance.pk)
    except Claim.DoesNotExist:
        return

    # Compare statuses
    if previous.status != instance.status:
        user_email = instance.user.email
        subject = 'Your Claim Status Has Been Updated'
        message = f'Hi {instance.first_name},\n\nYour insurance claim status has changed from "{previous.status}" to "{instance.status}".\n\nRegards,\nInsurance Team'
        send_mail(subject, message, 'no-reply@insurance.com', [user_email])
