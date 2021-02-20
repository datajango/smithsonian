# keep_api_key_secret.md

- Add .env to .gitignore, so it does not get added to the git repo.

- add python-dotenv to requirements.txt

- conda activate smith

- pip install -r requirements.txt

- create a .env file

- add your Smithsonian Open Access API Key to the .env file

	```
    API_KEY=Your API keyy goes here
  ```
- Add code to fetch the API key at runtime

	```
	from dotenv import load_dotenv

	load_dotenv()

	API_KEY = os.getenv("API_KEY")
	```
