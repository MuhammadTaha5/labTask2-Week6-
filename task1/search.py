from pymongo import MongoClient
from rapidfuzz import fuzz


client = MongoClient("mongodb://localhost:27017/")
db = client["nips2024"]
papers_collection = db["papers"]

def hybrid_fuzzy_search(query, threshold=50):
    results = []

    for paper in papers_collection.find({}):
        title = paper["title"]
        authors = " ".join(paper["authors"])

        
        title_score = fuzz.partial_ratio(query.lower(), title.lower())
        author_score = fuzz.partial_ratio(query.lower(), authors.lower())
        keyword_score = 100 if query.lower() in title.lower() else 0

        
        final_score = (0.6 * title_score) + (0.3 * author_score) + (0.1 * keyword_score)

        if final_score >= threshold:
            paper["score"] = round(final_score, 2)
            results.append(paper)

    
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

query = "deep lerning"
results = hybrid_fuzzy_search(query)

for paper in results[:10]:
    print(f"Score: {paper['score']}")
    print("Title:", paper["title"])
    print("Authors:", ", ".join(paper["authors"]))
    print("Link:", paper["link"])
    print("-" * 50)
