from openai import OpenAI


def wygeneruj_obraz_kota(rasa_kota: str) -> str:
    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"zdjęcie kota rasy {rasa_kota}",
        size="800x800",
        quality="standard",
        n=1,
    )

    return response.data[0].url
