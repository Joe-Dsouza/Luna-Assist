### api_handler.py
import requests
import wikipedia
from config import HUGGING_FACE_API_URL, headers
from duckduckgo_search import DDGS

def query_huggingface(prompt):
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json={"inputs": prompt, "options": {"wait_for_model": True}})
    if response.status_code == 200:
        result = response.json()
        return result.get("generated_text", "I couldn't process your request.")
    return "I'm having trouble processing your request. Please try again later."

def get_weather(location):
    response = requests.get(f"https://wttr.in/{location}?format=%C+%t")
    return response.text.strip() if response.status_code == 200 else f"Couldn't fetch weather for {location}."

def get_news():
    with DDGS() as ddgs:
        results = ddgs.news("latest news", max_results=3)
        return "\n".join([f"Title: {item['title']}" for item in results])

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous: {e.options[:5]}?"
    except Exception:
        return "Couldn't retrieve information from Wikipedia."

