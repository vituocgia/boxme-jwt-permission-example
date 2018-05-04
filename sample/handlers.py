# -*- coding: utf-8 -*-
from boxme_jwt.utils import jwt_payload_handler

from boxme_jwt_permission.settings import get_setting

from .models import GroupScope


def custom_jwt_payload_handler(user):
    payload = jwt_payload_handler(user)
    scopes = list(GroupScope.objects.filter(group__user=user).values_list("scope", flat=True))
    payload[get_setting("JWT_PAYLOAD_SCOPES_KEY")] = scopes
    return payload
