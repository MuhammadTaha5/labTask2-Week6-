# **Paper Scraping & Search System (Task 1)**

This task involved collecting research paper information from the NeurIPS 2024 papers page, saving the data into MongoDB, and building a simple but intelligent search system.

---

## **1. Scraping the Papers**

The first part of the task was to scrape all the papers from:

```
https://papers.nips.cc/paper_files/paper/2024
```

For every paper on the page, I extracted:

* The **title**
* The **link** to the paper’s abstract
* The **list of authors**

BeautifulSoup was used to read the page and pick each paper entry.
Once extracted, each paper was stored as a structured object so the data could be saved easily into a database.

---

## **2. Saving Data into MongoDB**

After scraping, all papers were inserted into a local MongoDB database.
A database named **nips2024** and a collection called **papers** were created.

Each paper is stored in MongoDB in a simple format:

```
{
  title: "...",
  authors: ["Author 1", "Author 2", ...],
  link: "..."
}
```

This structure makes it easy to search and retrieve the papers later.

---

## **3. Fuzzy & Hybrid Search System**

To make searching easier and more flexible, I implemented a **hybrid fuzzy search**.

### What the search engine does:

* Allows searching by **paper title** or **author name**
* Works even with **typos** or **partial words**
* Ranks results by **relevance**

### How hybrid fuzzy search works:

* It compares the user’s query with the paper title using fuzzy matching
* It also compares the query with all author names
* It adds a small bonus if the keyword appears directly in the title
* All these scores are combined using weights to produce a final score

This hybrid approach makes the search experience more natural, similar to how humans search even when not using exact spelling.

# **Task 2: Reverse Image Search**

This task focused on implementing a reverse image search system.
Two different approaches were used:

1. **Approach 1:** Sir’s provided method (CNN-based embeddings)
2. **Approach 2:** A more advanced Vision Transformer model (BiT/BViT) implemented with help of an AI tool

Both approaches extract image embeddings and compare them to find visually similar images.

---

## **1. Approach 1 – Using the Provided Code (CNN-Based Embeddings)**

In the first method, I followed the exact code and instructions provided by Sir.
The idea was to:

* Use a **pretrained CNN model** to generate image embeddings
* Convert each image into a 1D feature vector
* Store all embeddings
* Compute similarity using **cosine similarity**
* Return the most similar images based on the computed distance

### How it works:

1. Load the pretrained CNN (e.g., ResNet or similar)
2. For each image → generate a feature vector
3. For the query image → generate its embedding
4. Compare the query embedding with the dataset embeddings
5. The images with the smallest distance (or highest similarity) are returned

This method is simpler and fast but depends heavily on the CNN used.

---

## **2. Approach 2 – Using BViT / BiT (Transformer-Based Model)**

The second approach used a more modern model:
**BViT (Big Vision Transformer)** / **BiT (Big Transfer model)**.

This approach was implemented using help from an AI tool to correctly set up the code, load the model, and generate embeddings.

### Why this approach is better:

* Vision Transformers capture **global image features**
* Embeddings are generally more robust
* Performance is usually better for reverse image search
* More accurate similarity results

### Steps followed:

1. Load a pretrained ViT/BiT model
2. Preprocess all images according to the model's requirements
3. Extract embeddings for every image
4. Store the embeddings
5. Compute similarity between query image and dataset images
6. Return the top-K closest matches

This approach gave **more accurate and visually meaningful results** compared to the simple CNN method.

