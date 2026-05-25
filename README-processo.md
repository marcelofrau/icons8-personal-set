# Processo de Geração de Ícones Icons8

## Estrutura do Projeto

```
C:\Users\fraumar\Apps\_downloads\icons8\
├── 50x50\          ← Fonte (tamanhos pequenos)
├── 100x100\        ← Fonte (tamanhos grandes)
├── 16x16\          ← Gerado
├── 32x32\          ← Gerado
├── 48x48\          ← Gerado
├── 128x128\        ← Gerado
├── 256x256\        ← Gerado
├── ico\            ← .ico multi-resolução
├── processa-icones.py   ← Pipeline automatizado
├── icones-faltantes.md
└── README-processo.md
```

## Pipeline Automatizado (recomendado)

```bash
python processa-icones.py            # 8 workers (default)
python processa-icones.py --workers 16   # mais rapido em CPUs muitos nucleos
```

O script:
1. Varre `50x50/` e `100x100/` em busca de PNGs novos
2. Gera tamanhos derivados em paralelo (16, 32, 48, 128, 256)
3. Otimiza com optipng -o7
4. Gera .ico multi-resolução

## Nomenclatura

- **3D (3d-fluency):** `icons8-<nome>-3d-<tamanho>.png` (ex: `icons8-pdf-3d-50.png`)
- **2D (fluency):** `icons8-<nome>-2d-<tamanho>.png` (ex: `icons8-zip-2d-50.png`)
- **Legados (273 originais):** `icons8-<nome>-<tamanho>.png` (ex: `icons8-about-50.png`)
- **.ico:** segue o mesmo padrão sem tamanho: `icons8-<nome>-3d.ico`, `icons8-<nome>.ico`

## Como adicionar NOVOS ícones manualmente

### Passo 1: Baixar do Icons8

Tentar **3d-fluency** primeiro; se 404, usar **fluency**:

```
https://img.icons8.com/3d-fluency/50/<nome>.png
https://img.icons8.com/3d-fluency/100/<nome>.png
```

Salvar como:
```
50x50/icons8-<nome>-3d-50.png        # se 3d-fluency
50x50/icons8-<nome>-2d-50.png        # se fluency
```

### Passo 2: Rodar o pipeline

```bash
python processa-icones.py --workers 16
```

Isso gera todos os tamanhos, otimiza e cria .ico automaticamente.

## Resumo do workflow

```
Download Icons8 (3d-fluency → fluency) → 50x50/ + 100x100/
  ↓
python processa-icones.py --workers N   →  todos os tamanhos + optipng + .ico
```
