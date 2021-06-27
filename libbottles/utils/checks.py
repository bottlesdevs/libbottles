import re


def check_special_chars(text: str) -> bool:
    """
    Check for special characters in text.

    Parameters
    ----------
    text : str
        the text to be checked

    Return
    ----------
        returns True if it finds a special character, else False
    """
    regex = re.compile('[@!#$£%^&*()<>=?/|}{~:.;,]')
    if regex.search(text) is None:
        return False
    return True
