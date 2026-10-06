"""Gitlab's isses objects"""

from .utils import enrich_gitlab_list


def get(gitlab_api):
    """Retrieve current user's issues and adapt the data to be displayed"""
    group = gitlab_api.groups.get(183118)
    issues = group.issues.list(
        scope="all", state="opened"
    )
    return enrich_gitlab_list(issues, gitlab_api)
