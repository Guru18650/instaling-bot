
# Instaling Bot

Python bot made to finish your Instaling in less than 12 seconds



## Installation

Clone project to any directory, open with editor like VSCode

Install dependencies with pip

```bash
  pip install selenium
  pip install webdriver_manager
```
Fill data.json with your translated words (example data is included). Both words and translations need to be 100% accurate or bot will loop and crash. data.json needs to have all possible words. 

## Usage

```python
py bot.py
```
If it's the first time running it, it will ask for Instaling login and password. Later it will save it in login.json. If you want to change those, edit this json or delete it. bot.py will ask for credentials again.

Wait until bot will finish and crash (sadly)

IMPORTANT: the session can't be started before running bot (it searches for "start_session_button" and not "continue_session_button"). You can change it in line 29 of bot.py, but remember to change it back when its done.




## Authors

- [@Guru18650](https://github.com/Guru18650)


## License

[MIT](https://choosealicense.com/licenses/mit/)

