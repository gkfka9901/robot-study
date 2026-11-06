import numpy as np


def summarize(scan):


    valid = scan[np.isfinite(scan)]

    print(len(scan) - len(valid))
    print(valid.min(), valid.argmin())

    front = np.concatenate([scan[:30], scan[330:]])
    new_valid = front[np.isfinite(front)]
    print(new_valid.min())

    mask = valid < 0.5
    print(mask.sum())


if __name__ == "__main__":
    scan = np.linspace(0.3, 3.0, 360)   # 0.3~3.0m까지 360개
    scan[100] = np.inf                   # 측정 실패 구간 흉내
    scan[200] = np.inf
    summarize(scan)
