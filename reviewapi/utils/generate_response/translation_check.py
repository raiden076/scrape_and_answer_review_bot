import re
from reviewapi.utils.playwright_tools import fetch


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
    input_dict = fetch(URL=URL)
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


# input_string = "(Translated by Google) It's good, the service is fast at lunchtime and the staff friendly. 15 euros for starter + main course + dessert or cheese + 1 glass of wine. It's not very filling though. The good side of the thing is to keep the line!\n(Original)\nC est bon, le service est rapide le midi et le personnel aimable. 15 euros pour entrée + plat + dessert ou fromage + 1 verre de vin. Ce n est pas très copieux cependant. Le bon côté de la chose est de garder la ligne !"
# t2 = "Very good      Food: 5        Service: 5        Atmosphere: 5"
# # translated, original = check_n_return(input_string)
# # print(translated)
# # print(original)
# # print(check_n_return(input_string)[0])


# def test():
#     print(check_n_return(fetch("https://goo.gl/maps/Rxg1YuFD5PoGyop8A")))


# test()
