import os


class ConfigError(Exception):
    pass


class BaseConfig:

    def error(self, key: str, env: str):
        raise ConfigError(
            f'Configuration `{key}` missing.'
            f' Consider setting `{env}` environment variable'
        )

    def value(
        self,
        key: str,
        default: str = None,
    ):
        env_name = key.upper()
        value = (
            os.environ.get(env_name) or
            default or
            self.error(key, env_name)
        )
        setattr(self, key, value)
