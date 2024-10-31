# prontuario.py
import json

# Um pequeno dicionário com doenças e seus códigos CID-10
doencas = {
    "A00": "Cólera",
    "A01": "Febre tifóide",
    "A02": "Outras infecções por Salmonella",
    "A03": "Shiguelose",
    "A04": "Outras infecções bacterianas intestinais",
    "A05": "Outras intoxicações alimentares bacterianas",
    "A06": "Amebíase",
    "A07": "Outras doenças intestinais protozoárias",
    "A08": "Infecções intestinais virais e outras especificadas",
    "A09": "Diarréia e gastroenterite de origem infecciosa presumível",
    "B00": "Infecções por herpes vírus [herpes simplex]",
    "B01": "Varicela",
    "B02": "Herpes zoster",
    "B03": "Varíola",
    "B04": "Varíola dos macacos",
    "B05": "Sarampo",
    "B06": "Rubéola [sarampo alemão]",
    "B07": "Verruga viral",
    "B08": "Outras infecções virais especificadas caracterizadas por lesões de pele e mucosas",
    "B09": "Infecção viral não especificada caracterizada por lesões de pele e mucosas",
    "C00": "Neoplasia maligna do lábio",
    "C01": "Neoplasia maligna da base da língua",
    "C02": "Neoplasia maligna de outras partes e partes não especificadas da língua",
    "C03": "Neoplasia maligna da gengiva",
    "C04": "Neoplasia maligna do assoalho da boca",
    "C05": "Neoplasia maligna do palato",
    "C06": "Neoplasia maligna de outras partes e partes não especificadas da boca",
    "C07": "Neoplasia maligna da glândula parótida",
    "C08": "Neoplasia maligna das glândulas salivares maiores",
    "C09": "Neoplasia maligna da amígdala",
    "C10": "Neoplasia maligna da orofaringe",
    "C11": "Neoplasia maligna da nasofaringe",
    "C12": "Neoplasia maligna do seio piriforme",
    "C13": "Neoplasia maligna da hipofaringe",
    "C14": "Neoplasia maligna de outras partes e partes mal definidas da boca",
    "D00": "Carcinoma in situ da cavidade oral, esôfago e estômago",
    "D01": "Carcinoma in situ de outros e dos não especificados órgãos digestivos",
    "D02": "Carcinoma in situ da laringe",
    "D03": "Melanoma in situ",
    "D04": "Carcinoma in situ da pele",
    "D05": "Carcinoma in situ da mama",
    "D06": "Carcinoma in situ do colo do útero",
    "D07": "Carcinoma in situ de outros órgãos genitais",
    "D08": "Carcinoma in situ de outros e dos não especificados órgãos e sistemas",
    "E00": "Síndromes congênitas de deficiência de iodo",
    "E01": "Distúrbios da tireoide relacionados à deficiência de iodo e condições correlatas",
    "E02": "Hipotireoidismo subclínico devido à deficiência de iodo",
    "E03": "Outras formas de hipotireoidismo",
    "E04": "Bócio não-tóxico",
    "E05": "Tireotoxicose [hipertireoidismo]",
    "E06": "Tireoidite",
    "E07": "Outras doenças da tireoide",
}

def buscar_doenca_por_codigo(codigo):
    """Busca o nome da doença a partir do código CID."""
    return doencas.get(codigo, "Código não encontrado.")

def buscar_doenca_por_nome(nome_doenca):
    """Busca o código da doença a partir do nome."""
    for codigo, nome in doencas.items():
        if nome.lower() == nome_doenca.lower():
            return codigo
    return "Doença não encontrada."

def salvar_prontuario(nome_paciente, codigo_doenca, nome_doenca):
    """Salva os dados do paciente e a doença em um arquivo JSON."""
    prontuario = {
        "nome": nome_paciente,
        "doenca": {
            "codigo": codigo_doenca,
            "nome": nome_doenca
        }
    }

        # Salvar prontuário em um arquivo JSON
    with open(f'{nome_paciente}_prontuario.json', 'w') as arquivo_json:
        json.dump(prontuario, arquivo_json, indent=4)
    return f'{nome_paciente}_prontuario.json'
