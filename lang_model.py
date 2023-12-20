import os
import openai

# Configure Open AI Key:
# openai.api_key = os.environ.get('OPENAI_API_KEY')

class LLM:
    """
    Class to communicate with ChatGPT
    """
    def __init__(self):
        pass

    @staticmethod
    def create_summary(kind: str, text: str) -> dict:
        """
        Write summary to a text. The user will decide which style of summary from a UI list
        :param kind: Summary kind: Bullet points, short summary, 1 sentence, 5 sentences.
        :param text: Text to summarize
        :return: ChatGPT answer
        """

        response = openai.chat.completions.create(
            model="gpt-4",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": f"Please write summary for the following text. I want the best {kind} summary that you can get."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        return response


    @staticmethod
    def answer(text: str, query: str) -> dict:
        """
        Get answer about the text, and send answer via ChatGPT.
        :param text: subject text
        :param query: user question
        :return: ChatGPT answer
        """
        response = openai.chat.completions.create(
            model="gpt-4",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": f"You are agent that is very familiar with the given text, the user will ask you a "
                               f"question about the following text, and you will answer to him."
                               f"If the question is not related to the text topics, Please mention it to user, and ask"
                               f"him to check with other LLMs"
                               f"Also please start your answer by re-writing the user question in short"
                               f"For example, you will get a text about transportation, and the user will ask how many "
                               f"sits there are in regular city bus"
                               f"You will search for answer in the text, for example 'in a city bus we have at least 30 "
                               f"seats' and you will return '30 seats'"
                               
                               f"The text you need to understand and answer about is this: {text}"
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )
        return response

