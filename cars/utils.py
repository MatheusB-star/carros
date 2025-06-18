import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)


def gerar_bio_carro(modelo, marca, ano_fabricacao, ano_modelo, valor):
    prompt = (
        f"Crie uma descrição persuasiva, com no máximo 200 characteres, para a venda de um carro com os seguintes dados:\n"
        f"- Marca: {marca}\n"
        f"- Modelo {modelo}\n"
        f"- Ano de fabricação {ano_fabricacao}\n"
        f"- Ano do modelo {ano_modelo}\n"
        f"- Valor R${valor:.2}"
    )

    try:
        model = genai.GenerativeModel("models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as erro:
        return erro
    
    