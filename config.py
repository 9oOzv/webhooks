from baseconfig import BaseConfig
from pathlib import Path


class Config(BaseConfig):

    def __init__(self):
        self.value('host', 'localhost')
        self.value('port', '5000')
        self.value('github_secret', 'foobar')
        self.value('scripts_dir', Path(__file__).parent / 'scripts')
