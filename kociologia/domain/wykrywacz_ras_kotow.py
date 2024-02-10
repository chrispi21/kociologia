from openai import OpenAI


def wykrywacz_ras_kotow(rasa_kota="ragdoll") -> bool:
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Rozpoznaj czy podano prawidłową nazwę rasy kota. Jeśli nazwa jest poprawna, zwróć TAK, jeśli niepoprawna NIE. Nazwy z literówkami traktuj jako poprawne."},
            {"role": "user", "content": f"{rasa_kota}"}
        ]
    )

    response = completion.choices[0].message.content

    return response == "TAK"
