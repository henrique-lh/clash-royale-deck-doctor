# Clash Roayle Doctor Deck

This is a web application for analyze Clash Royale decks, matchups and provide useful feedback through LLM.

## Prerequisites – Running locally

You must have installed
1. Docker
2. Node.js
3. UV

Create an account in [Clash Royale API](https://developer.clashroyale.com). You must generate an API key and copy it.

Create an account in [Hugging Face](https://huggingface.co/). You must request an API key to use the Ollama model.
In this example, I am using the `meta-llama/Llama-3.3-70B-Instruct` model, however, you can choose your own from Hugging Face
website. Generate an API key and copy it.

Create a `.env` and paste the copied APIs key in the file in the root directory with the following content:
- `CLASH_API_KEY=<YOU_KEY>`
- `OLLAMA_API_KEY=<YOUR_KEY>`

> [!NOTE]
> If you don't use OLlama and wish to change the name of the key, you can change it in `app/infrastructure/external/ollama/ollama_settings.py`.
> If you do it, you must also change the variable `MODEL` in `app/infrastructure/external/ollama/ollama_client.py`.

Finally, it will be necessary to have a clash roayle player tag to test it.

## Setup

Before you get started, you'll need to setup the redis container:

```bash
# Setup the redis
docker compose up -d
```

Install dependencies for the front and back end

```bash
# To install python dependencies
uv sync

# To install frontend dependencies
cd deck-doctor-frontend
npm install
cd ../
```

## Run

Run the backend
```bash
uv run uvicorn app.main:app --reload
```

Run the frontend
```bash
cd deck-doctor-frontend
npm run dev
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
