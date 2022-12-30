import re
from tenacity import retry
from tenacity.stop import stop_after_attempt

# import asyncio
from reviewapi.utils.playwright_tools import extract


@retry(stop=stop_after_attempt(5))
def fetch_review(URL: str) -> dict[str, str | None]:
    print("fetching review with playwright")
    # URL = input("Enter the URL of the review to extract: ")
    review = extract(URL)
    return {"rating": review[0], "review": clean_review(review[1])}


def clean_review(input_string: str) -> str | None:
    # Use a regular expression to extract the review information
    input_string = " ".join(line.strip() for line in input_string.splitlines())
    match = re.search(r"New(.*)Like", input_string)
    if match:
        return match.group(1).strip()
    else:
        return None


def extract_translated_original(input_string: str):
    # Use a regular expression to extract the translated and original parts
    match = re.search(
        r"(Translated by Google\)(.*)\(Original)", input_string, re.DOTALL
    )
    if match:
        original = match.group(2).strip()
    else:
        original = None
    match = re.search(r"Original\)(.*)", input_string, re.DOTALL)
    if match:
        translated = match.group(1).strip()
    else:
        translated = None

    return original, translated


def check_n_return(URL: str) -> dict[str, str | None]:
    """
    check_n_return(bla)[0] will always return original, whereas [1] will return translated or none
    """
    print("checking for translation")
    input_dict = fetch_review(URL=URL)
    if (
        not input_dict["review"] == None
        and "Translated by Google" in input_dict["review"]
    ):
        translated, original = extract_translated_original(input_dict["review"])
        return {
            "rating": input_dict["rating"],
            "review": original,
            "translated_review": translated,
        }
    else:
        return {
            "rating": input_dict["rating"],
            "review": input_dict["review"],
            "translated_review": None,
        }


# input1 = "                        2 weeks ago New     Very good      Food: 5        Service: 5        Atmosphere: 5                 Like     Share        "
# output1 = extract_review(input1)
# print(output1)

# input2 = "                        5 days ago New     Good      Food: 5        Service: 5        Atmosphere: 5                 Like     Share        "
# output2 = extract_review(input2)
# print(output2)
# print(fetch_review())
# clean_review("                         a month ago New     Dirty palace
# Rough behavior      Price per person     ₹1–200                 Like     Share")
