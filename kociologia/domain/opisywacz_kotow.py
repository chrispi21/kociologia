from openai import OpenAI


def opisywacz_kotow(rasa_kota="ragdoll") -> str:
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "W kilku zdaniach opisz daną rasę kota. Popraw literówki w nazwie rasy kota."},
            {"role": "user", "content": f"Opowiedz mi kilka ciekawostek o rasie: {rasa_kota}."}
        ]
    )

    return completion.choices[0].message.content
