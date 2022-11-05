
# Instaling Bot

Python bot made to finish your Instaling in less than 12 seconds



## Installation

Clone project to any directory, open with editor like VSCode

Install dependencies with pip

```bash
  pip install selenium
  pip install webdriver_manager
```
YOU NEED CHROME AND CHROMEDRIVER INSTALLED
https://chromedriver.chromium.org/downloads

## Usage

```python
py bot.py
```
If it's the first time running it, it will ask for Instaling login and password. Later it will save it in login.json. If you want to change those, edit this json or delete it. bot.py will ask for credentials again. Data will be learnt by bruteforce, data.json will be generated. There you can find all gathered translations ("your language":"foreign language"). You can see that bot makes mistakes at first few runs, thats because it is learning new words. Later it will be 100% accurate. 



## Authors

- [@Guru18650](https://github.com/Guru18650)


## License

[MIT](https://choosealicense.com/licenses/mit/)

