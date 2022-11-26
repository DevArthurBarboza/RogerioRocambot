import os
from dotenv import load_dotenv

class Env:
     
    isLoaded = False

    def load_dotenv():
        Env.isLoaded = True
        return load_dotenv()

    def get_env(name):
        if Env.isLoaded == False:
            self.load_dotenv()

        return os.getenv(name)

