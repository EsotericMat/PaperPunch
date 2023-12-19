import random

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

    def save_api_key(self, api_key: str) -> None:
        """
        Save a new given API key
        :param api_key: user openAI API key
        :return: None
        """
        env_path = find_dotenv()
        unset_key(env_path, "OPENAI_API_KEY")
        set_key(env_path, "OPENAI_API_KEY", api_key)
        st.success("API Key saved successfully!")

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

    def set_llm_key(self):
        """
        Validate that one have the needed Key to communicate with the LLM.
        :return: None
        """
        if self.config['OPENAI_API_KEY'] != '':
            openai.api_key = self.config['OPENAI_API_KEY']
        else:
            st.write("First, set your OpenAI API Key")
            # Check if .env file exists, create if not
            env_path = find_dotenv()
            if not env_path:
                st.warning("Creating a new .env file...")
                with open(".env", "w") as file:
                    file.write("")

            user_api_key = st.text_input("Enter your OpenAI API Key:")
            if st.button("Save API Key"):
                if user_api_key:
                    self.save_api_key(user_api_key)
                else:
                    st.warning("Please enter an API Key!")

    def random_spinner_text(self) -> str:
        """
        Select one sentence to print while the application is processing information.
        :return: Random sentence
        """
        return random.choice(self.LOAD_SENTENCES)