from pathlib import Path
import re
import json
from langdetect import detect
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

PATT = ".md"
ROOT_DIR = Path(__file__).resolve().parents[0]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA = DATA_DIR / "raw"
RE = r"[\s]*?#"

mapping = {"header": 1, "text": 0}

def init_dir(folder):
    Path.mkdir(folder, parents=True, exist_ok=True)

def is_lang(text, lang="en"):
    if detect(text) == lang:
        return True
    return False

def annotate_files():
    output = []
    num_t = 0
    num_h = 0
    for file in RAW_DATA.glob(f"*{PATT}"):
        with file.open() as f:
            data = f.read()
            if not is_lang(data):
                continue
            lines = data.splitlines()
            start = 0
            for line in lines:
                if line.strip("\r\n\t "):
                    end = start + len(line)
                    if re.match(RE, line):
                        label = "header"
                        num_h += 1
                    else:
                        label = "text"
                        num_t += 1
                    output.append({"text": data,
                                   "start": start,
                                   "end": end,
                                   "file": str(file),
                                   "label": label})
                    start += len(line)
    with (DATA_DIR / "data.json").open("w+") as f:
        f.write(json.dumps(output, indent=4))
    logger.info(f"Texts: {num_t}, Headers: {num_h}")
    return output

def split_data(data=None, train_size=0.8):
    if data is None:
        with (DATA_DIR / "data.json").open() as f:
            data = json.load(f)
    train, test = train_test_split(data, stratify=[el["label"] for el in data],
                                   train_size=train_size)
    return train, test

def baseline(data, value="text"):
    y_pred = [mapping[value]] * len(data)
    return y_pred, [mapping[el["label"]] for el in data]

def rule_1():
    pass

def apply_rules():
    pass

def estimate_metric():
    pass

def main():
    #data = annotate_files()
    train, test = split_data()
    y_pred, y_true = baseline(test)
    print(y_true)
    precision = precision_score(y_true, y_pred, "weighted")
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    logger.info(f"Precision: {precision}, Recall: {recall}, F1: {f1}")


if __name__ == "__main__":
    rez = main()