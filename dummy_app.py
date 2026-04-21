import os
from pathlib import Path


def load_env_file(env_file: str) -> None:
    path = Path(env_file)
    if not path.exists():
        raise FileNotFoundError(f'Environment file not found: {env_file}')

    for line in path.read_text().splitlines():
        entry = line.strip()
        if not entry or entry.startswith('#') or '=' not in entry:
            continue
        key, value = entry.split('=', 1)
        os.environ[key.strip()] = value.strip()


def main() -> None:
    env_name = os.environ.get('APP_ENV', 'dev')
    env_file = '.env.test' if env_name == 'test' else '.env.dev'
    load_env_file(env_file)

    print('Dummy Okta app loaded configuration:')
    print(f"client_id={os.environ.get('OKTA_CLIENT_ID', '')}")
    secret = os.environ.get('OKTA_CLIENT_SECRET', '')
    redacted = f"{secret[:4]}...{secret[-4:]}" if len(secret) > 8 else '********'
    print(f'client_secret={redacted}')


if __name__ == '__main__':
    main()
