from django.utils import timezone
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

signer = TimestampSigner(salt="user-register")

TOKEN_EXPIRY_SECONDS = 3600  # 1 hour

def generate_user_register_token(user):
    return signer.sign(user.pk)

def verify_user_register_token(token):
    try:
        unsigned = signer.unsign(token, max_age=TOKEN_EXPIRY_SECONDS)
        return int(unsigned)
    except SignatureExpired:
        logger.warning("User registration token expired.")
    except BadSignature:
        logger.warning("User registration token invalid.")
    return None