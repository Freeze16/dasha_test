from pelican import signals

from .config import DASHA_API_KEY, DASHA_BASE_ID
from .dasha import DashaMail
from .tools import get_participants_emails

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def update_mailing_list(_):
    emails = get_participants_emails()
    mg = DashaMail(DASHA_API_KEY)
    mg.update_mailing_list(DASHA_BASE_ID, emails)


def register():
    signals.initialized.connect(update_mailing_list)


__all__ = ("register",)
