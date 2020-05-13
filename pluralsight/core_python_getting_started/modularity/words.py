# Program to read a txt file from internet and put the words in string format
# into a list.

# Getting the url from the command line.
"""Retrive and print words from a URL.

Usage:

    python3 words.py <url>
"""
import sys

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The url of UTF-8 text document.
        
    Returns:
        A list of strings containing the words from 
        the document.
    """
    # Importing urlopen method.
    from urllib.request import urlopen

    # Getting the text from the url given.
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_items(items):
    """Prints items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    """Prints each word from a text document from a URL.

    Args:
        url: The url of UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])
