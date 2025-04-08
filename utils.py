from urllib.parse import urlparse
import re

def extract_features_from_url(url):
    features = []
    parsed = urlparse(url)

    # 1. Длина URL
    features.append(len(url))

    # 2. Использование https
    features.append(1 if parsed.scheme == "https" else 0)

    # 3. Кол-во поддоменов
    features.append(len(parsed.netloc.split(".")) - 1)

    # 4. Наличие IP-адреса в URL
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    features.append(1 if ip_pattern.search(url) else 0)

    # 5. Кол-во специальных символов
    features.append(url.count("@") + url.count("-") + url.count("=") +
                    url.count("&") + url.count("%") + url.count("+"))

    return features
