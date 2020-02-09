### Set Up
After cloning the repo, you should create a new virtual env and install all dependencies from `requirements.txt` then create access_tokens from `twitter_developers` + access_tokens from `google_developers` and add them to two seperate files called `twitter_keys.py` and `gphotos_keys.json` respectively. This is how both the files should look like:
1. `config.py`
    ```
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""
    ```
2. `gphotos_keys.json`
    ```
    {
    "installed":
        {
            "client_id":"",
            "client_secret":"",
            "auth_uri":"https://accounts.google.com/o/oauth2/auth",
            "token_uri":"https://www.googleapis.com/oauth2/v3/token",
            "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]
        }
    s}
    ```
Now, Just run `main.py`