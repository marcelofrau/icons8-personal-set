# Icons8 Personal Icon Set

Biblioteca pessoal de ícones Icons8 nos estilos **3d-fluency** e **fluency**, com variações em múltiplos tamanhos e formato `.ico` para Windows.

## Estrutura

```
├── 50x50/            PNGs fonte (tamanho pequeno)
├── 100x100/          PNGs fonte (tamanho grande)
├── 16x16/            Redimensionado para 16×16
├── 32x32/            Redimensionado para 32×32
├── 48x48/            Redimensionado para 48×48
├── 128x128/          Redimensionado para 128×128
├── 256x256/          Redimensionado para 256×256
├── ico/              .ico multi-resolução (16, 32, 48, 128, 256)
├── processa-icones.py    Pipeline de geração automática
├── icones-faltantes.md   Lista de ícones disponíveis por categoria
└── README-processo.md    Documentação técnica do pipeline
```

## Nomenclatura

- `icons8-<nome>-3d-<tamanho>.png` — ícone 3d-fluency
- `icons8-<nome>-2d-<tamanho>.png` — ícone fluency
- `icons8-<nome>-<tamanho>.png` — ícone legado (273 originais)
- `icons8-<nome>-3d.ico` / `icons8-<nome>-2d.ico` — .ico multi-resolução

## Requisitos

- ImageMagick 7 (`magick` no PATH)
- optipng (`optipng` no PATH)

## Pipeline

```bash
python processa-icones.py --workers 16
```

O script detecta PNGs novos em `50x50/` e `100x100/`, gera todos os tamanhos derivados, otimiza com optipng e cria os `.ico`.

## Licença

MIT
