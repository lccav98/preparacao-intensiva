FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PREP_CURSO_DIR=/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY 00_*.md 00_acompanhamento.csv ./
COPY estagio_A ./estagio_A
COPY estagio_B ./estagio_B
COPY estagio_C ./estagio_C
COPY estagio_D ./estagio_D
COPY estagio_E ./estagio_E
COPY estagio_F ./estagio_F
COPY estagio_G ./estagio_G
COPY estagio_H ./estagio_H
COPY automacao_curso ./automacao_curso

# Opcional (Multi-Disciplina MAT121 no mesmo container):
# Se desejar embutir o curso Matrizes e Vetores na imagem Docker, copie-o para ./cursos/matrizes_vetores
# e adicione `COPY cursos ./cursos` ou monte um volume definindo PREP_CURSO_MV_DIR.

EXPOSE 8090

CMD ["python", "automacao_curso/servidor_dashboard.py"]
