# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:12:57 2022

@author: jeffa
"""


def pi_imc(gain, time_constant, delay_time, factor):
    # Compute PI gains using IMC method
    Tc = factor*max(0.8*delay_time, 0.1*time_constant)
    Kp = time_constant/(Tc + delay_time)/gain
    Ki = Kp/time_constant
    return Kp, Ki