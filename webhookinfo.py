import hmac
import hashlib
from functools import cached_property
from flask import Request, request


class WebHookInfo:

    def __init__(self, request: Request):
        self.request = request

    @cached_property
    def headers(self) -> dict:
        return self.request.headers

    @cached_property
    def json(self) -> dict | None:
        return self.request.get_json(silent=True)

    def verify_signature(self, secret: str) -> bool:
        mac = hmac.new(
            bytes(secret, 'utf-8'),
            msg=self.payload,
            digestmod=hashlib.sha256
        )
        if not self.signature:
            return False
        return hmac.compare_digest(
            f'sha256={mac.hexdigest()}',
            self.signature
        )

    @cached_property
    def signature(self) -> str | None:
        return self.headers.get('X-Hub-Signature-256')

    @cached_property
    def payload(self) -> str:
        return request.get_data()

    @cached_property
    def repo_name(self) -> str | None:
        return self.json['repository']['name']

    @cached_property
    def script_name(self) -> str:
        return f"{self.repo_name}.sh"
