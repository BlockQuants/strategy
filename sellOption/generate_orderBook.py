# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
import pandas as pd

class orderBook_generator:
    prime_rate = 0.03
    year2mature = 50/250.0
    est_vol = 0.12
    temp_price = 5867.0
    max_GrowthRate = 0.2
    tick1 = 1.0
    K = 5900
    amount = 50
    option_type = 'put'

    def BS_delta(self,S,strike,option_type):
        d1 = (np.log(S/strike) + (self.prime_rate + self.est_vol**2/2)*self.year2mature)/(self.est_vol*np.sqrt(self.year2mature))
        if option_type == 'call':
            delta = stats.norm.cdf(d1,0,1)
        elif option_type  == 'put':
            delta = stats.norm.cdf(d1,0,1) - 1
        else:
            delta = None
        return delta

    def cal_delta(self,S):
        delta_now = -self.amount * self.BS_delta(S,self.K,self.option_type)
        return delta_now

    def cal_original_table(self):
        p_floor = np.floor(self.temp_price*(1-self.max_GrowthRate)/self.tick1) * self.tick1
        p_ceil = np.ceil(self.temp_price*(1+self.max_GrowthRate)/self.tick1) * self.tick1
        p_arr0 = np.array(np.arange(p_floor,p_ceil,self.tick1))
        delta_list = []
        for p_temp in p_arr0:
            delta_temp = self.cal_delta(p_temp)
            delta_list.append(delta_temp)
        delta_int_arr = np.floor(np.array(delta_list))
        index_change = delta_int_arr[1:] != delta_int_arr[:-1]
        delta_arr = delta_int_arr[:-1][index_change]
        p_arr = p_arr0[:-1][index_change]
        max_p = np.max(p_arr)
        min_p = np.min(p_arr)
        index_temp = (p_arr<max_p)&(p_arr>min_p)
        delta_arr1 = delta_arr[index_temp]
        p_arr1 = p_arr[index_temp]
        p_u = np.array([np.min(p_arr[p_arr>s]) for s in p_arr1])
        p_d = np.array([np.max(p_arr[p_arr<s]) for s in p_arr1])
        p_d_amount = np.array([sum(p_d[:i+1]==p_d[i]) for i in range(p_d.shape[0])])
        p_u_amount = np.array([sum(p_u[i:]==p_u[i]) for i in range(p_u.shape[0])])
        self.delta_ref = delta_arr1
        self.p_u = p_u
        self.p_d = p_d
        self.p_u_amount = p_u_amount
        self.p_d_amount = p_d_amount
        df = pd.DataFrame()
        df['delta_ref'] = self.delta_ref
        df['p_u'] = self.p_u
        df['p_d'] = self.p_d
        df['p_d_amount'] = self.p_d_amount
        df['p_u_amount'] = self.p_u_amount
        
        return df