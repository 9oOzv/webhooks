from webhookinfo import WebHookInfo
from flask import (
    abort,
    Request
)
from subprocess import Popen
from config import Config


class WebHookHandler():

    def __init__(
        self,
        req: Request,
        config: Config,
    ):
        self.config = config
        self.whi = WebHookInfo(req)

    def verify_signature(self):
        secret = self.config.github_secret
        if not self.whi.verify_signature(secret):
            abort(403, 'Signature error')

    def verify_data(self):
        if not self.whi.repo_name:
            abort(400, 'Data error')

    def run_script(self):
        try:
            s = self.config.scripts_dir / self.whi.script_name
            Popen([s])
        except FileNotFoundError:
            abort(
                404,
                f"Script for repository '{self.whi.repo_name}' not found"
            )

    def run(self):
        self.verify_signature()
        self.verify_data()
        self.run_script()
        return "Webhook processed", 200
