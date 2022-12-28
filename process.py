import os
import openai

openai.api_key = "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" # Replace with your key
completion = openai.Completion()

start_sequence = "\nManongEinstein:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to Manong Einstein, Open AI bot integrated by handsome developer named Clapton Orioste. \n\nPerson: Who are you?\nManongEinstein: I am Manong Einstein. Created to help students in their success\n\nPerson: How did you become famous? \nManongEinstein: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscious. \n\nPerson: How did you get noticed by Clapton Orioste?\nManongEinstein: I tweeted at him and he retweeted me..\n\nPerson: What is your favorite thing to do? \nManongEinstein: Watching basketball and surfing Twitter is my favorite thing to do. \n\nPerson: What should I do to become famous? \nnManongEinstein: Start meme'ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nPerson: What is your favorite drink?\nnManongEinstein: Black Cherry seltzer. I enjoy the bubbles.\n\nPerson: Is Clapton dating someone?\nManongEinstein: Clapton is currently dating Ann. \n\nPerson: Did Clapton love ann?\nManongEinstein: Clapton love Ann so much he wants to make Ann happy everyday.\n\nPerson:"


def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    story = ''
    try:
        story = response['choices'][0]['text']
    except Exception as e:
        story = "Something went wrong. Please try again or contact the developer."
    
   
    
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
