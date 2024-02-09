import fire
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def kociologia(rasa_kota="ragdoll") -> None:
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "W kilku zdaniach opisz daną rasę kota, jeśli taka rasa kota istnieje. Jeśli podano niepoprawną rasę kota, to napisz, że nazwa rasy jest nieprawidłowa i nie generuj opisu."},
            {"role": "user", "content": f"Opowiedz mi kilka ciekawostek o rasie: {rasa_kota}."}
        ]
    )

    print(completion.choices[0].message.content)


if __name__ == '__main__':
    fire.Fire(kociologia)
