from unittest.mock import AsyncMock

from app.bot import dev_func


async def test_dev_func_smoke(message_mock: AsyncMock):
    await dev_func(message_mock)

    assert message_mock.answer.call_count == 1
