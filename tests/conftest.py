from unittest.mock import AsyncMock

import pytest


@pytest.fixture
def message_mock() -> AsyncMock:
    mock = AsyncMock()
    yield mock
