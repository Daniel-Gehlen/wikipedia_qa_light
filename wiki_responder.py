import os
import sys
import wikipedia
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

# Configurações iniciais
wikipedia.set_lang('pt')
wikipedia.set_user_agent("MeuAplicativo/1.0 (meuemail@dominio.com)")

def buscar_titulo_pergunta(pergunta):
    print(f'Buscando título para a pergunta: {pergunta}')
    """Busca automaticamente o título do artigo mais relevante com base na pergunta."""
    resultados = wikipedia.search(pergunta, results=1)
    return resultados[0] if resultados else None

def buscar_artigo(titulo):
    print(f'Buscando artigo: {titulo}')
    try:
        pagina = wikipedia.page(titulo)
        return pagina.content, pagina.url
    except wikipedia.exceptions.PageError:
        return None, None

def buscar_referencias_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    referencias = soup.find('ol', {'class': 'references'})
    citacoes = []
    if referencias:
        for ref in referencias.find_all('li'):
            citacao = ref.get_text()
            citacoes.append(citacao)
    return citacoes

def responder_pergunta_basico(pergunta):
    print(f'Processando pergunta: {pergunta}')
    titulo_artigo = buscar_titulo_pergunta(pergunta)
    if not titulo_artigo:
        return "Não foi possível encontrar um artigo relevante.", None
    
    texto, url = buscar_artigo(titulo_artigo)
    if not texto:
        return "Artigo não encontrado.", None
    
    resposta = ""
    for linha in texto.split('. '):
        if pergunta.lower() in linha.lower():
            resposta = linha.strip()
            break
    
    if not resposta:
        resposta = "Não foi possível encontrar uma resposta precisa no artigo."
    
    referencias = buscar_referencias_wikipedia(url)
    resposta_final = f"# Resposta para: {pergunta}\n\n**Resposta:** {resposta}.\n\n**Fonte:** [{url}]({url})\n\n**Referências Citadas:**\n"
    for ref in referencias[:5]:
        resposta_final += f"- {ref}\n"
    
    return resposta_final

class WikipediaQAApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Wikipedia QA')
        layout = QVBoxLayout()
        self.questionLabel = QLabel('Pergunta:')
        self.questionInput = QLineEdit(self)
        self.searchButton = QPushButton('Buscar', self)
        self.searchButton.clicked.connect(self.search_wikipedia)
        self.resultText = QTextEdit(self)
        self.resultText.setReadOnly(True)
        layout.addWidget(self.questionLabel)
        layout.addWidget(self.questionInput)
        layout.addWidget(self.searchButton)
        layout.addWidget(self.resultText)
        self.setLayout(layout)

    def search_wikipedia(self):
        print('Botão Buscar clicado!')
        pergunta = self.questionInput.text()
        if not pergunta:
            QMessageBox.warning(self, 'Aviso', 'Por favor, insira uma pergunta.')
            return
        resposta_completa = responder_pergunta_basico(pergunta)
        self.resultText.setPlainText(resposta_completa)

def main():
    app = QApplication(sys.argv)
    ex = WikipediaQAApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

