import openai

# from tenacity import retry
# from tenacity.stop import stop_after_attempt

# Set your API key
openai.api_key = "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"

# Define the function to generate a response
# def generate_response(review: str, rating: int):
#     # Extract the star rating from the review
#     # rating = int(review.split()[-1])
#     if rating >= 4:
#         # Generate a positive response
#         prompt = f"'This Bot does not ask follow up questions, just generate appropriate responses'\n\nBot: We are happy to hear that you had a great experience at our restaurant. Could you please tell us more about what you enjoyed during your visit?\nCustomer: {review}"
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             temperature=0.5,
#             max_tokens=70,
#             top_p=1,
#             frequency_penalty=1,
#             presence_penalty=1,
#             stop=["Customer :"],
#         )
#         return response
#     elif rating == 3:
#         # Generate a neutral response
#         prompt = f"'This Bot does not ask follow up questions, just generate appropriate responses'\n\nBot: Thank you for your feedback. Could you please tell us more about your experience at our restaurant?\nCustomer: {review}"
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             temperature=0.5,
#             max_tokens=70,
#             top_p=1,
#             frequency_penalty=1,
#             presence_penalty=1,
#             stop=["Customer :"],
#         )
#         return response
#     else:
#         # Generate a negative response
#         prompt = f"'This Bot does not ask follow up questions, just generate appropriate responses'\n\nBot: We are sorry to hear that you had a negative experience at our restaurant. Could you please tell us more about what went wrong during your visit?\nCustomer: {review}"
#         response = openai.Completion.create(
#             engine="text-curie-001",
#             prompt=prompt,
#             temperature=1.0,
#             max_tokens=70,
#             top_p=1,
#             frequency_penalty=1,
#             presence_penalty=1,
#             stop=["Customer :"],
#         )
#         return response


# Define the review
# review = "Very good      Food: 5        Service: 5        Atmosphere: 5"
# review = "Alors pourquoi une étoile Menu choisi à 32 euros ( Le plus cher) Escalopes de foie gras et bonbon de cailles ( cuisses de cailles ) Jusque là ça été, classique Ensuite bouillabaisse , un petit filet de poisson, 2 crevettes, une noix de saint jacques et en guise de légumes un quart de Christophine, soit la valeur d'une grosse frite , légumes absents, lorsque j'ai demandé ,on m'a dit que la sauce à la tomates et la Christophine étaient les légumes ! la serveuse au demeurant sympathique ne m'a rien proposé, juste lorsque j'ai fait la remarque, elle m'a dit texto : en 8 ans c'est la première fois qu'on me dit ça ! ensuite le dessert imposé arrive et là, pour 32 euros une boule de glace caramel ,une mini crème brûlée , une crème citron que l'on trouve sur les tartes et le summum un quart de poire au sirop sauce chocolat ! Bien entendu pas de vin au pichet . Déception totale ah si j'oubliais , le pain était bon et en quantité :) Alors si vous aimez la cuisine généreuse et si vous attendez de la direction qu'elle accepte vos critiques suggestives, passez votre chemin! Par contre si vous voulez manger du foie gras excellent et des menus extra , menu buffet à midi très généreux , avec un accueil parfait , allez au restaurant le Pass plat face à la gare de Montbrison, vous ne serez pas déçu, par contre réservez avant ..."

# # Generate a response
# response = generate_response(review, 1)

# # Print the response
# print(response)


def gen_response(rev_dict: dict[str, str | None], get_full_response: bool = False):  # type: ignore
    rating = rev_dict["rating"]
    if not rev_dict["translated_review"] == None:
        review = rev_dict["translated_review"]
    else:
        review = rev_dict["review"]
    response = openai.Completion.create(  # type: ignore
        model="text-davinci-003",
        prompt=f"This is a restaurant review replier bot. If the customer has any concerns address them but don't ask follow up questions. If the rating is high, don't forget to thank them. \nrating: {rating} star\nreview: {review}\nreply:\n",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if get_full_response:
        return response  # type: ignore
    else:
        return response.choices[0].text  # type: ignore


def process(response_dict: dict[str, str | None]):
    print("Processing response with gpt3...")
    response = gen_response(response_dict)  # type: ignore
    response_dict.update({"response": response})  # type: ignore
    return response_dict


def test():
    rev_dict = {
        "rating": 1,
        "review": "Stopped by this location to get some dinner, the person at the drive thru said \"It will be a minute.\" I waited in the rain trying to keep my window cracked to the car so I can hear when they get back on the speaker. Nothing! Waited, and waited, still nothing. After 5 minutes had to start saying in the speaker \"Hello, anyone there?\" Finally someone took the order. They didn't listen to the order, had to repeat myself multiple times for 3 combo meals, all exactly the same, tried to keep it very basic and easy, but that was still too complicated for the staff member doing the drive-thru. When I got the order, all three combos were shorted on fries. I decided to eat my meal in the parking lot, when I was done I noticed they don't have a garbage can anywhere around. Is Wendy's getting so cheap they can't even put out a garbage can for the customers? Also had to keep the doors locked to my car while eating, all kinds of homeless people wondering around, garbage laying on the ground. Needless to say, I will not be returning to this location ever again. Service Take out Meal type Dinner Price per person $30–40 ",
        "translated_review": None,
    }
    print(process(rev_dict))  # type: ignore


if __name__ == "__main__":
    test()
