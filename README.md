# okta-vuln
Okta Secret leaked via .env used for testing

## Dummy application
- `dummy_app.py` loads environment variables from `.env.dev` by default.
- Set `APP_ENV=test` to load `.env.test` instead.
