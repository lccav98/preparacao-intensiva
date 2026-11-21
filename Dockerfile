FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PREP_CURSO_DIR=/app \
    PREP_CURSO_MV_DIR=/app/cursos/matrizes_vetores

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY 00_*.md ./
COPY estagio_A ./estagio_A
COPY estagio_B ./estagio_B
COPY estagio_C ./estagio_C
COPY estagio_D ./estagio_D
COPY estagio_E ./estagio_E
COPY estagio_F ./estagio_F
COPY estagio_G ./estagio_G
COPY estagio_H ./estagio_H
COPY cursos ./cursos
COPY automacao_curso ./automacao_curso

EXPOSE 8090

CMD ["python", "automacao_curso/servidor_dashboard.py"]
