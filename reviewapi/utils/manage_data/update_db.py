import pymongo
import hashlib

conn_string = (
    "mongodb+srv://raiden:qyjiD1eEdtHCjWxg@saved-reviews.mpjwkj5.mongodb.net/test"
)
client = pymongo.MongoClient(conn_string, serverSelectionTimeoutMS=5000)  # type: ignore
db = client.reviews  # type: ignore
reviews = db.processed_reviews  # type: ignore


# def connect_mongo():
#     """Connect to MongoDB"""
#     conn_string = (
#         "mongodb+srv://raiden:qyjiD1eEdtHCjWxg@saved-reviews.mpjwkj5.mongodb.net/test"
#     )
#     try:
#         client = pymongo.MongoClient(conn_string, serverSelectionTimeoutMS=5000)
#         db = client.reviews
#         reviews = db.processed_reviews
#         return "Connected to MongoDB!"
#     except:
#         return "Failed to connect to MongoDB!"


def hash_review(review: str) -> str:
    return hashlib.md5(review.encode("utf-8")).hexdigest()


# review = "Very gooood      Food: 5        Service: 5        Atmosphere: 5"
# test_review1 = {
#     "hashed_review": f"{hash_review(review)}",
#     "rating": "5",
#     "review": "Very gooood      Food: 5        Service: 5        Atmosphere: 5",
#     "translated_review": None,
#     "response": "This is a response",
# }
# "rating": input_dict["rating"],
# "review": input_dict["review"],
# "translated_review": None,
# "response": "This is a response",
def insert_review(review_d: dict[str, str | None]) -> str:
    """Structure a review into a dictionary"""
    print("Inserting review into database...")
    rating = review_d["rating"]
    review = review_d["review"]
    translated_review = review_d["translated_review"]
    response = review_d["response"]
    hashed_review = hash_review(review)  # type: ignore
    review_dict = {
        "hashed_review": hashed_review,
        "rating": rating,
        "review": review,
        "translated_review": translated_review,
        "response": response,
    }
    # connect_mongo()
    reviews.insert_one(review_dict)  # type: ignore
    return "Review added to database!"


test_review1 = {
    "rating": "5",
    "review": "Food: 5        Service: 5        Atmosphere: 4",
    "translated_review": None,
    "response": "This is a response",
}

if __name__ == "__main__":
    print(structure_review(test_review1))  # type: ignore
