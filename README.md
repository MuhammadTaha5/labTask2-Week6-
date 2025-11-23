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

Here is a **short, clean, submission-ready README** exactly as you asked:

---

# **Task 2: Reverse Image Search**

For this task, I implemented **two approaches**:

## **1. Sir’s Given Approach (Baseline)**

* Used the provided starter code.
* Extracted embeddings using **ResNet50** (ImageNet) with a fallback **HSV color histogram**.
* Stored results in a **parquet file**.
* Performed similarity search using **NumPy cosine similarity**.
* Displayed the query image and **Top-K similar images** in a grid.
* This method gives decent matches and is good for understanding the pipeline.

## **2. BViT / ViT Approach (My Second Method)**

* Implemented a **Vision Transformer (BViT / ViT)**–based encoder with help from an AI tool.
* Extracted stronger transformer-based embeddings.
* Performed the same cosine similarity search.
* This approach gives **much better semantic similarity** than ResNet50 or histograms.
