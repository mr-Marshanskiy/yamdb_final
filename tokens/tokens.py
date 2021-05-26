from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


def generate_confirmation_code(email):
    user, created = User.objects.get_or_create(email=email)
    token_generator = PasswordResetTokenGenerator()
    if created:
        user.delete()
    return token_generator.make_token(user)


def get_tokens_for_user(user):
    return str(AccessToken.for_user(user))
