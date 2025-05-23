def is_valid_job(text):
    text = text.lower()
    keywords = ["marketing", "communication", "digital media", "digital marketing"]
    language_keywords = ["english", "anglais"]
    return any(kw in text for kw in keywords) and any(lang in text for lang in language_keywords)