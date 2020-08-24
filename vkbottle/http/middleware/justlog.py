from .abc import ABCHTTPMiddleware
from vkbottle.modules import logger
import typing


class JustLogHTTPMiddleware(ABCHTTPMiddleware):
    async def pre(
        self,
        method: str,
        url: str,
        data: typing.Optional[dict] = None,
        **kwargs
    ):
        logger.debug(f"{method.upper()} Request to {url}; data={data} " + "; ".join(f"{k}={v}" for k, v in kwargs.items()))

    async def post(self, response: typing.Any):
        logger.debug(f"Response: {response}")
