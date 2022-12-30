import pymongo
import hashlib

conn_string = (
    "mongodb+srv://raiden:qyjiD1eEdtHCjWxg@saved-reviews.mpjwkj5.mongodb.net/test"
)
client = pymongo.MongoClient(conn_string, serverSelectionTimeoutMS=5000)  # type: ignore
db = client.reviews  # type: ignore
reviews = db.processed_reviews  # type: ignore


def hash_review(review: str) -> str:
    return hashlib.md5(review.encode("utf-8")).hexdigest()


def search_review(review_d: dict[str, str | None]) -> dict[str, str | None]:
    hashed_review = hash_review(review_d["review"])  # type: ignore
    review_dict = reviews.find_one({"hashed_review": hashed_review})  # type: ignore
    if review_dict:
        return review_dict  # type: ignore
    else:
        return None  # type: ignore


def test():
    test_review1 = {
        "rating": "5",
        "review": "Food: 5        Service: 5        Atmosphere: 4",
        "translated_review": None,
    }
    print(search_review(test_review1))


if __name__ == "__main__":
    test()
