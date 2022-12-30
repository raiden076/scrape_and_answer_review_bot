# from reviewapi.utils.playwright_tools import fetch
# from tenacity import retry
# from tenacity.stop import stop_after_attempt
# from .openai_gpt3 import gen_response as process


# @retry(stop=stop_after_attempt(5))
# def generate_response(URL: str):
#     response_dict = fetch(URL)
#     response_dict.update({"response": "This is a response"})
#     return response_dict


# @retry(stop=stop_after_attempt(5))
# def generate_response2(review_dict: dict[str, str | None]):
#     response = process(review_dict)
#     response_dict.update({"response": response})
#     return response_dict


# twst = {
#     "rating": "5",
#     "review": "Food: 5        Service: 5        Atmosphere: 4",
#     "translated_review": None,
# }


# def test():
#     print(generate_response2(twst))


# if __name__ == "__main__":
#     test()
