import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 347782959 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    scale = 27
    sum_2 = np.sum(x**2)
    q1 = chi2.ppf(1 - alpha / 2, df = len(x) * 2)
    q2 = chi2.ppf(alpha / 2, df = len(x) * 2)
    return np.sqrt(sum_2 / (q1 * scale)), np.sqrt(sum_2 / (q2 * scale))
