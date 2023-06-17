from unittest.mock import AsyncMock

from app.bot import cmd_help


async def test_cmd_help_smoke(message_mock: AsyncMock):
    await cmd_help(message_mock)

    assert message_mock.answer.call_count == 1
