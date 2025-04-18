from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from claim.models import Claimant

@receiver(pre_save, sender=Claimant)
def notify_user_on_status_change(sender, instance, **kwargs):
    if not instance.pk:
        # New record; skip
        return

    # Fetch existing object from DB
    try:
        previous = Claimant.objects.get(pk=instance.pk)
    except Claimant.DoesNotExist:
        return

    # Compare statuses
    if previous.status != instance.status:
        user_email = instance.user.email
        subject = 'Your Claim Status Has Been Updated'
        message = f'Hi {instance.first_name},\n\nYour insurance claim status has changed from "{previous.status}" to "{instance.status}".\n\nRegards,\nInsurance Team'
        send_mail(subject, message, 'no-reply@insurance.com', [user_email])
