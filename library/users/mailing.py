import logging

from django.conf import settings
from django.core.mail import send_mail

from library.celery import app
from users.constants import WELCOME_LETTER_MESSAGE, WELCOME_LETTER_SUBJECT


logger = logging.getLogger('custom')


@app.task
def test_task(username, email):
    logger.info('Trying to send email')
    send_mail(
        WELCOME_LETTER_SUBJECT,
        WELCOME_LETTER_MESSAGE.format(username),
        settings.DEFAULT_FROM_EMAIL,
        [email]
    )
