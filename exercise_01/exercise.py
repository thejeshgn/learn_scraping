###############################################################################
# Thejesh <i@thejeshgn.com>, GNU/GPL v3
###############################################################################
# Exercise: Get the title of the given url.
#
# Hint: Use python `requests` and `BeautifulSoup` libraries.
# `requests` is a python library used to get html content.
# `BeautifulSoup` is a python library used to parse html content.
#
# Implement get_title function below.
###############################################################################


# TODO Import requests and BeautifulSoup

# This function should return the title of the url
def get_title(url):
    page_title = "nothing"
    # TODO Get the content of the web page using requests

    # TODO Parse the content using BeautifulSoup html parser

    # TODO Extract the title tag, its content and then return it.
    return page_title


def main():
    """Runs the program. And try it"""
    url = "https://www.google.com/"
    print(get_title(url))


if __name__ == "__main__":
    main()
