import requests

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
headers = {"Authorization": "Bearer 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"}


def query(payload: dict[str, str]):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


review = "Alors pourquoi une étoile Menu choisi à 32 euros ( Le plus cher) Escalopes de foie gras et bonbon de cailles ( cuisses de cailles ) Jusque là ça été, classique Ensuite bouillabaisse , un petit filet de poisson, 2 crevettes, une noix de saint jacques et en guise de légumes un quart de Christophine, soit la valeur d'une grosse frite , légumes absents, lorsque j'ai demandé ,on m'a dit que la sauce à la tomates et la Christophine étaient les légumes ! la serveuse au demeurant sympathique ne m'a rien proposé, juste lorsque j'ai fait la remarque, elle m'a dit texto : en 8 ans c'est la première fois qu'on me dit ça ! ensuite le dessert imposé arrive et là, pour 32 euros une boule de glace caramel ,une mini crème brûlée , une crème citron que l'on trouve sur les tartes et le summum un quart de poire au sirop sauce chocolat ! Bien entendu pas de vin au pichet . Déception totale ah si j'oubliais , le pain était bon et en quantité :) Alors si vous aimez la cuisine généreuse et si vous attendez de la direction qu'elle accepte vos critiques suggestives, passez votre chemin! Par contre si vous voulez manger du foie gras excellent et des menus extra , menu buffet à midi très généreux , avec un accueil parfait , allez au restaurant le Pass plat face à la gare de Montbrison, vous ne serez pas déçu, par contre réservez avant ..."

prompt = f"'This Bot does not ask follow up questions, just generate appropriate responses'\n\nBot: We are sorry to hear that you had a negative experience at our restaurant. Could you please tell us more about what went wrong during your visit?\nCustomer: {review}"
output = query(
    {
        "inputs": prompt,
    }
)
print(output)
