
## Output Screenshot
![App Screenshot](https://user-images.githubusercontent.com/69301816/189028578-d1d27a3c-2fa3-4bb5-ac7e-63e49c2e28b4.png)
## Objectives 🎯

The goal of this project is to scrap customer reviews from amazon

# Problem Statement ❓

- You can use this data to analyze the product
- Discover insights into consumer reviews
# Programming Language 🐍
Python



## Python Libraries 📀


- Splash
- BeautifulSoup
- Requests
- Pandas
## Domain 🏥

Python Development

# Tools 🛠
- Visual Studio Code


## Steps

- Splash is a lightweight browser, has a HTTP API built in where we can send our request and it returns the information 

- Install docker
`sudo apt install docker*`

- Install Splash
`sudo docker pull scrapinghub/splash`

- Start Splah service in docker
`sudo docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash`

- Import Python Libraries
```bash
import requests
from bs4 import BeautifulSoup
import pandas as pd
```
![Parse Data](https://user-images.githubusercontent.com/69301816/189036150-8561b1d0-1505-4a1e-b49b-30bbeb4da306.jpg)
![Review Function](https://user-images.githubusercontent.com/69301816/189039113-ff2a5085-2458-42f4-8462-02c5c2fdbd4f.jpg)
![Loop](https://user-images.githubusercontent.com/69301816/189040209-4c24d942-e415-429a-9b39-484da03e7302.jpg)

- Save the data into DataFrame 
```bash
df = pd.DataFrame(reviewlist)
df.to_excel('Maono AU-MH601 Professional.xlsx', index=False)
```
