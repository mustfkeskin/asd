# Welcome to Simple Recommender Sysyem
This project aim to simple recommendation system using Item2Vec approach and BM25 algorithm.

Traditional architecture for recommendation systems consists of the following components:
* candidate generation: Item2Vec and BM25 for my implementation. We use it to reduce search space because there can be millions of products.
* personalization: We dont have any user data. If the person has always drank gluten-free while making a milk recommendation, we should pay attention to this.
* re-ranking: Best selling products and price and brand segmentation


## Item2Vec
Identify word and sentence equivalents from data. Word embeddings can learn sequence of words each sentence. For the model to learn the embedding, we need to get the “word” and “sentence” equivalents from the data. Here it can be imagined that each “product” is a “word”, and products that received similar signals from a user are in the same “sentence”. Specifically, “sentences” are generated with the following process: For each user, generate sessions each session have list of items which added to card by the user. Those lists are the inputs to train the Gensim Word2Vec model.

Item2Vec approach subfield of Collaborative filtering.

![Example Item2Vec Result](Assets/item2vec_example.png)

### Pros
* We dont need the product information. The page order the user navigates is enough for us
* Easily applicable
* If we have millions of product we can use approximate nearest neighbour techniques like PQ, HNSW ... for faster search. Implementations of these algorithms can be found in the [Faiss](https://github.com/facebookresearch/faiss) library.

### Cons
* OOV problem :( 
* Cannot offer recommendations new product or less visited products
* We need to keep our vector database up to date


## BM25



### Pros
* Can recommend new product easily

### Cons
* OOV problem :(
* We need to update our vector database



# Evaluation metrics
Ndcg@10 can be use for evaluation



# Installation

* pip install -r requirements.txt

## Build Docker Container

`docker build -t recomender-system-demo:latest .`

## Run Docker Container

`docker run -d -p 8000:8000 recomender-system-demo`


## Example API Request
When you go to the web browser you use and go to this [link](http://localhost:8000/docs), swagger will open, you can test it from there.


curl -X POST "http://0.0.0.0:8000/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"events\":[{\"event\":\"card\",\"sessionid\":\"0002e53b-1f60-4309-8380-31ca03de51f8\",\"eventtime\":\"2020-06-06 17:51:18.003\",\"price\":5.5,\"productid\":\"HBV00000AX6LV\"}]}"

![Example Recommendation](Assets/example_input.png)
![Example Recommendation](Assets/example_result.png)


## Contact

If you have any question contact with me "mustfkeskin@gmail.com"


## License

This project is released under the MIT License.
