import pandas as pd
import numpy as np


chat_id = 42877418

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.02
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    se = np.sqrt(p1 * (1 - p1) / x_cnt + p2 * (1 - p2) / y_cnt)
    
    t_stat = (p1 - p2) / se
    dof = x_cnt + y_cnt - 2
    t_crit = t.ppf(alpha / 2, dof)
    
    return abs(t_stat) > t_crit
    
   
