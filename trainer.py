import getting_stat
import json


def train(text: str, model_file: str):
    new_statistics = getting_stat.get_stat(text)
    with open(model_file, "w") as f:
        json.dump(new_statistics, f)
