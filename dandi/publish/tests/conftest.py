import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
    AssetFactory,
    DandisetFactory,
    DraftVersionFactory,
    UserFactory,
    VersionFactory,
)
from .girder import GirderFileFactory, MockGirderClient

register(AssetFactory)
register(DandisetFactory)
register(DraftVersionFactory)
register(GirderFileFactory)
register(UserFactory)
register(VersionFactory)


@pytest.fixture
def girder_file(girder_file_factory):
    # TODO: Due to https://github.com/pytest-dev/pytest-factoryboy/issues/67 , this fixture is
    # broken when auto-generated by pytest_factoryboy
    return girder_file_factory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def mock_girder_client() -> MockGirderClient:
    return MockGirderClient()
