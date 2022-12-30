"""
steps for me to remember:
1. fetch review with playwright and structure with rating review and translated_review as a dict
2. if review == None, stop
3. then check with the dict if it already exists in the db
4. if it does, fetch and show
5. if it doesn't, process through the model and save to db
"""

from reviewapi.utils.playwright_tools import fetch
from reviewapi.utils.manage_data import search, push
from reviewapi.utils.generate_response import process


def main(URL: str):
    review_dict = fetch(URL)
    if review_dict["review"] == None:
        return "No review found"
    else:
        if search(review_dict):
            print("Found in DB")
            return search(review_dict)

        else:
            response_dict = process(review_dict)
            push(response_dict)
            print("processed and Pushed to DB")
            return response_dict


# print(main("https://goo.gl/maps/uizsBv1sdDK8CG9Z8"))
