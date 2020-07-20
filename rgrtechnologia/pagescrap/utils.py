import re


def get_regex():
    return [
        re.compile(r'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})'),
        re.compile(r'(\+\(?\d{2}\)?\s)?(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})'),
        re.compile(r'(\d{13})'),
        re.compile(r'(\+\d{11})'),
        re.compile(r'(\(\d{3}\)\s\d{3}\-\d{4})'),
    ]


def get_link_logo(img_logos):
    return [src.replace('src=', '').replace('\"', '') for img in img_logos if 'logo' in img.lower() for src in img.split() if
            'src=' in src]
