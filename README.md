# Welcome to Simple Recommender Sysyem

This project aim to simple recommendation system using Item2Vec approach and BM25 algorithm


## Installation

* pip install -r requirements.txt

### Build Docker Container

`docker build -t recomender-system-demo:latest .`

### Run Docker Container

`docker run -d -p 8000:8000 recomender-system-demo`


## Example Request

curl -X POST "http://0.0.0.0:8000/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"events\":[{\"event\":\"card\",\"sessionid\":\"0002e53b-1f60-4309-8380-31ca03de51f8\",\"eventtime\":\"2020-06-06 17:51:18.003\",\"price\":5.5,\"productid\":\"HBV00000AX6LV\"}]}"

![Example Recommendation](Assets/example_input.png)
![Example Recommendation](Assets/example_result.png)


## Contact

If you have any question contact with me "mustfkeskin@gmail.com"

## License

This project is released under the MIT License.
