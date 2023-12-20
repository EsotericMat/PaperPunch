import random
import os
from dotenv import set_key,unset_key, find_dotenv, dotenv_values
import requests
import openai
import streamlit as st

class App:
    """
    Class for application utilities
    """
    LOAD_SENTENCES = [
    "Loading like a snail on espresso.",
    "Tickling electrons for faster vibes.",
    "Summoning warp-speed gerbils!",
    "Pixelating at the speed of sloth.",
    "Coffee break for the code ninjas.",
    "Tick-tock, loading o'clock!",
    "Rustling up pixel pancakes.",
    "Fetching data, one byte at a time.",
    "Tickling servers for a giggle boost.",
    "Seducing zeros and ones to cooperate."]

    def __init__(self):
        self.config = dotenv_values('.env')

    def load_lotti(self, url: str) -> dict:
        """
        Load Lotti animation
        :param url: URL for the animation
        :return: Details in json
        """
        response = requests.get(url)
        if response.status_code != 200:
            return {None: None}
        return response.json()

    def random_spinner_text(self) -> str:
        """
        Select one sentence to print while the application is processing information.
        :return: Random sentence
        """
        return random.choice(self.LOAD_SENTENCES)