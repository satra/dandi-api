from __future__ import annotations

import logging
from typing import Optional
import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.postgres.fields import JSONField

from dandiapi.api.girder import GirderClient, GirderError

from dandiapi.consts import UUID_REGEX
logger = logging.getLogger(__name__)


class Dandiset(TimeStampedModel):
    # Don't add beginning and end markers, so this can be embedded in larger regexes
    IDENTIFIER_REGEX = r'\d{6}'

    uuid = models.UUIDField(unique=True,
                            default=uuid.uuid4)
    metadata = JSONField(blank=True, default=dict)

    class Meta:
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['uuid'])
            ]
        ordering = ['id']

    @property
    def identifier(self) -> Optional[str]:
        # Compare against None, to allow id 0
        return f'DANDI:{self.id:06}' if self.id is not None else ''


    @classmethod
    def published_count(cls):
        """Return the number of Dandisets with published Versions."""
        # Prevent circular import
        from .version import Version

        # It's not possible to efficiently filter by a reverse relation (.versions),
        # so this is an efficient alternative
        return Version.objects.values('dandiset').distinct().count()

    def __str__(self) -> str:
        return self.identifier
