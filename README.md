# Doré Vision
Gustave Doré Divine Comedy illustrations with accompanying excerpts from the original work and the H. F. Cary English translation (1909). A script for automated generation of the anthology is provided.

For automated generation, the repository should at minimum initially contain the following files in the structure shown below:

```text
dore_vision/
├── document/
│   ├── illustrations/
│   │   ├── book_folder/
│   │   │   ├── image_file.jpg
│   │   │   └── ...
│   │   └── ...
│   └── References.bib
├── Dore_vision_starter.tex
├── Dore_vision_text.csv
├── generator.py
└── requirements.txt
```

installation:

```bash
pip install -r requirements.txt
```

usage:

```bash
python generator.py
```

![example image](figure.jpg)

### References

1. Alighieri, D. (1966–1967). La Commedia secondo l'antica vulgata (G. Petrocchi, Ed.). Mondadori.
1. Alighieri, D. (1909). The divine comedy (H. F. Cary, Trans.). P.F. Collier & Son.