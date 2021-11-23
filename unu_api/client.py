"""
Клиент к API
"""
import logging
from json.decoder import JSONDecodeError
from typing import Any, Dict

import requests

from .exceptions import JsonParsingError, RequestError, UnknowError

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class Client:
    """
    Клиент для подключения к API
    """

    req = requests.Session()

    @classmethod
    def post(cls, url: str, data: Dict[Any, Any]) -> str:
        """
        Метод реализует post-запрос к API
        """
        try:
            response = cls.req.post(url=url, data=data)
            response_json = response.json()
            if response_json["success"] == "true":
                return response_json
            elif response_json["success"] == "false":
                logging.debug(response.text)
                raise RequestError
        except JSONDecodeError:
            logging.debug(response.text)
            raise JsonParsingError
        except Exception:
            raise UnknowError
