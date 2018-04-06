import re


def sanitize_string(s): 
    """
    This function gets the alphanumeric content of a string.

    Args:
        s: The string to sanitize.

    Returns: 
        An alphanumeric string representation of s.
    
    Raises:
        None.
    """
    return ' '.join(' '.join(re.findall(r'[ -~]+', s)).split())


def sanitize_files_list(files, extensions): 
    return filter(lambda f: f.lower().endswith(map(lambda x: x.lower(), extensions)), files)