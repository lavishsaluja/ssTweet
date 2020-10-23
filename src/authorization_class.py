from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import AuthorizedSession
from google.oauth2.credentials import Credentials
import os
import logging

logging.basicConfig(
    format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I_%M_%S %p',
    filename='log_file',
    level=logging.INFO
)


class Authorization:
    def __init__(self, scopes):
        self.scopes = scopes

    def prompt_user_for_credentials(self):
        path = os.path.dirname(os.path.abspath(__file__))
        flow = InstalledAppFlow.from_client_secrets_file(
            path+'/gphotos_keys.json',
            scopes=self.scopes
        )

        logging.info('Prompting user to login to get their credentials for the defined scopes')

        return flow.run_local_server(
            host='localhost',
            port=8080,
            authorization_prompt_message='',
            success_message="google authorization has been completed & tweets' screenshots have been uploaded. open your google photos app when you'd like to see the tweets.",
            open_browser=True
        )

    def get_credentials(self, auth_file):
        if auth_file:
            try:
                return Credentials.from_authorized_user_file(auth_file)
            except ValueError as err:
                logging.error('the info (auth file) is not in the expected format: {}'.format(err))
                raise err
        return self.prompt_user_for_credentials()

    def get_auth_session(self, cred):
        return AuthorizedSession(cred)
