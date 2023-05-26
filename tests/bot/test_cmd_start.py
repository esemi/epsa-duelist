from unittest.mock import AsyncMock

from app.bot import cmd_start


async def test_cmd_start_smoke(message_mock: AsyncMock):
    await cmd_start(message_mock)

    assert message_mock.answer.call_count == 1
