import os

import logging

from django.core.management.base import BaseCommand
from src.profiles.models import UserNet

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    __user_class = UserNet

    def handle(self, *args, **options):
        logger.info("run fill command")
        super_username = os.environ["ADMIN_SUPER_USER_NAME"]
        admin_queryset = self.__user_class.objects.all().filter(
            username=super_username
        )
        if len(admin_queryset) < 1:
            logger.info("admin profile not found")
            self.__create_super_user(super_username)

    def __create_super_user(self, username=None):
        logger.info("start creating new admin profile")
        user = self.__user_class(
            is_staff=True,
            is_active=True,
            is_superuser=True,
            username=username
        )
        user.set_password("ADMIN_SUPER_USER_PASSWORD")
        user.save()
        logger.info("admin was created")
