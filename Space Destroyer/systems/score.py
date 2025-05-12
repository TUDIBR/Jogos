import yaml

def save_score(info: dict):
    with open("data/score.yml", "w") as f:
        yaml.dump(info, f, allow_unicode=True)

def read_score(points: int, seconds: float):
    with open("data/score.yml", "r") as f:
        info = yaml.safe_load(f)

    comparison = [info['score'], info['survival_time_record']]

    if info['score'] < points:
        comparison[0] = points
    if info['survival_time_record'] < seconds:
        comparison[1] = seconds

    return comparison