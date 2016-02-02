from django.contrib.auth.models import User
from chemicals.models.periphery import Profile

def run():
    for profile in Profile.objects.all():
        departments = profile.departments.all()
        name = "{}@KRONOSWW.COM".format(profile.user.username.split('@')[0])
        try:
            user = User.objects.get(username__iexact=name)
            new_profile, created = Profile.objects.get_or_create(user=user)
            if created:
                new_profile.departments = departments
        except:
            pass
