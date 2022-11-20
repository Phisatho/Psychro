#-------------------------------------------------------------------------------
# Name:        Psyfunc.py
# Purpose:
#
# Author:      Shibu
#
# Created:     16/06/2012
# Copyright:   (c) Shibu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import print_function
from math import nan, log, exp
#from decimal import *


Rgas = 8.314472
Mair = 0.028966
KILO = 1000.0
ZEROC = 273.15
INVALID = nan


def Tw_Tdp(T, Tdp, P):
    """
    Calculates Wet Bulb from dewpoint
    
    Args:
        T(C),
        Tdp(C)
        P(Pa)
    
    Returns:
        Tdb(C)
    """
    if Tdp <= T:
        W = W_Tdp(Tdp, P)
        return Tw_W(T, W, P)
    else:
        return INVALID

def Tw_Phi(T, Phi, P):
    """
    Calculate wetbulb from RH
    Parameters
    ----------
    T : float
        Drybulb (C).
    Phi : float
        RH (fraction).
    P : float
        Pressure (Pa).

    Returns
    -------
    float
        Tw (C).

    """
    if (Phi >= 0 and Phi <= 1):
       W = W_Phi(T, Phi, P)
       return Tw_W(T, W, P)
    else:
         return INVALID

def Phi_Tdp(T, Tdp):
    """
    Calculate RH from dewpoint

    Parameters
    ----------
    T : float
        drybulb (C).
    Tdp : float
        Dewpoint (C).

    Returns
    -------
    float
        RH (Fraction).

    """
    if (Tdp <= T):
       Pv = Pvs_T(Tdp)
       Pvs = Pvs_T(T)
       return Pv / Pvs
    else:
         return INVALID

def Phi_Tw(T, Tw, P):
    """
    Calculate RH from Wetbulb

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Tw : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Tw <= T):
       W = W_Tw(T, Tw, P)
       return Phi_W(T, W, P)
    else:
         return INVALID

def Tdp_Phi(T, Phi):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Phi : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Phi >= 0 and Phi <= 1):
       Pv = Pv_Phi(T, Phi)
       return Tdp_Pv(T, Pv)
    else:
         return INVALID

def Tdp_Tw(T, Tw, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Tw : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Tw <= T):
       W = W_Tw(T, Tw, P)
       return Tdp_W(T, W, P)
    else:
         return INVALID

def Pv_Phi(T, Phi):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Phi : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Phi >= 0 and Phi <= 1):
       return Phi * Pvs_T(T)
    else:
         return INVALID

def Phi_Pv(T, Pv):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Pv : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Pv >= 0):
       return Pv / Pvs_T(T)
    else:
         return INVALID

def Tdp_Pv(T, Pv):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Pv : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if Pv >= 0:
       VP = float(Pv) / KILO
       alpha = log(VP)
       if (T >= 0 and T <= 93):
          Tdp = 6.54 + 14.526 * alpha + 0.7389 * alpha * alpha + \
          0.09486 * pow(alpha, 3) + 0.4569 * pow(VP, 0.1984)
       elif (T < 0):
            Tdp = 6.09 + 12.608 * alpha + 0.4959 * alpha * alpha
       else:
            Tdp = INVALID
       return min(Tdp, T)
    else:
         return INVALID

def Pv_Tdp(Tdp):
    """
    

    Parameters
    ----------
    Tdp : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return Pvs_T(Tdp)

def Tw_W(T, W, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       Tdp = Tdp_W(T, W, P)
       Twtemp1 = float(T)
       Twtemp2 = float(Tdp)
       Tw = (Twtemp1 + Twtemp2) / 2
       while((Twtemp1 - Twtemp2) > 0.001):
                      Wstar = W_Tw(T, Tw, P)
                      if (Wstar > W):
                         Twtemp1 = Tw
                      else:
                           Twtemp2 = Tw
                      Tw = (Twtemp1 + Twtemp2) / 2
       return Tw
    else:
         return INVALID

def W_Tw(T, Tw, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    Tw : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    if (Tw <= T):
        if (T>= 0):
            Wsstar = Ws_T(Tw, P)
            return ((2501.0 - 2.326 * Tw) * Wsstar - 1.006 * (T - Tw)) / (2501.0 + 1.86 * T - 4.186 * Tw)
        else:
            Wsstar = Ws_T(Tw, P)
            return ((2830.0 - 2.4 * Tw) * Wsstar - 1.006 * (T - Tw)) / (2830.0 + 1.86 * T - 2.1 * Tw)
    
    else:
         return INVALID

def W_Phi(T, Phi, P):
    """
    

    Parameters
    ----------
    T : Float
        Drybulb (C)
    Phi : Float
        RH as fraction
    P : Float
        Pressure (Pa).

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if (Phi >= 0 and Phi <= 1):
       Pv = Pv_Phi(T, Phi)
       return W_Pv(Pv, P)
    else:
         return INVALID

def Phi_W(T, W, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       Pv = Pv_W(W, P)
       return Phi_Pv(T, Pv)
    else:
         return INVALID

def W_Tdp(Tdp, P):
    """
    

    Parameters
    ----------
    Tdp : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    Pv = Pvs_T(Tdp)
    return W_Pv(Pv, P)

def Tdp_W(T, W, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       Pv = Pv_W(W, P)
       return Tdp_Pv(T, Pv)
    else:
         return INVALID

def W_Pv(Pv, P):
    """
    

    Parameters
    ----------
    Pv : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if Pv >= 0:
        return 0.621945 * Pv / (P - Pv)
    else:
        return INVALID

def Pv_W(W, P):
    """
    

    Parameters
    ----------
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       return P * W / (0.621945 + W)

def Hd_T(T):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return 1.006 * T * KILO

def Dd_T(T, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return (P / KILO) * Mair / (Rgas * CTOK(T))

def Vd_T(T, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return Rgas * CTOK(T) / ((P / KILO) * Mair)

def Pvs_T(T):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if T >= -100 and T <= 200:
      Tk = CTOK(T)
      if (T >= -100 and T <= 0):
            LnPws = (-5.6745359e3/Tk + 6.3924247 - 9.677843e-3 * Tk +
                    6.2215701e-7 * Tk *Tk + 2.0747825e-9 * pow(Tk, 3) -
                    9.484024E-13*pow(T, 4) + 4.1635019 * log(Tk))
                    
##                    LnPws = (-5.6745359E+03/T + 6.3925247 - 9.677843E-03*T + 6.2215701E-07*T*T
##        + 2.0747825E-09*pow(T, 3) - 9.484024E-13*pow(T, 4) + 4.1635019*log(T));
##                    
                    
                    
      elif (T >0 and T <= 200):
           LnPws = (-5.8002206e3/Tk + 1.3914993 - 4.8640239e-2 * Tk + 
                   4.1764768e-5 * Tk * Tk - 1.4452093e-8 * pow(Tk, 3) + 6.5459673 * log(Tk))
      else:
           return INVALID
      return exp(LnPws)
    else:
         return INVALID

def Ws_T(T, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    Pvs = Pvs_T(T)
    return 0.621945 * Pvs / (P - Pvs)
    
def Hs_T(T, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return H_W(T, Ws_T(T, P))

def Pvdef(T, W, P):
    """
    #Vapor Pressure Deficit

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       Phi = Phi_W(T, W, P)
       return Pvs_T(T) * (1.0 - Phi)
    else:
        return INVALID 

def Sw_W(T, W, P):
    """
    #Degree of Saturation

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       return W / Ws_T(T, P)
    else:
         return INVALID    

def H_W(T, W):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       return (1.006 * T + W * (2501.0 + 1.86 * T)) * KILO
    else:
         return INVALID

def V_W(T, W, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >= 0:
       return 0.287042 * CTOK(T) * (1.0 + 1.607858 * W) / (P / KILO)
    else:
         return INVALID

def D_W(T, W, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if W >=0:
       return (1.0 + W) / V_W(T, W, P)
    else:
         return INVALID

def P_z(z):
    """
    

    Parameters
    ----------
    z : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return 101325.0 * pow(1.0 - 2.25577e-5 * z, 5.2559)

def T_z(z):
    """
    

    Parameters
    ----------
    z : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return 15 - 0.0065 * z

def Pz_P(T, z, P):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    z : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    Tcolumn = T + 0.0065 * z / 2
    HtScale = 287.055 * CTOK(Tcolumn) / 9.807
    return P * exp(z/HtScale)

def P_Pz(T, z, P0):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.
    z : TYPE
        DESCRIPTION.
    P0 : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return P0/Pz_P(T, z, 1.0)

def CTOK(T):
    """
    

    Parameters
    ----------
    T : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return T + ZEROC


def T_TwW(Tw, W, P):
    """
    

    Parameters
    ----------
    Tw : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = Tw
    while W_Tw(Ttemp, Tw, P) > W:
       #print(Ttemp)
       Ttemp += 0.01
    return Ttemp

def T_HW(H, W):
    """
    

    Parameters
    ----------
    H : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = 0
    while H_W(Ttemp, W) < H:
          Ttemp += 0.01
    return Ttemp
    
def Ts_H(H, P):
    """
    

    Parameters
    ----------
    H : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = -100
    while Hs_T(Ttemp, P) < H:
          Ttemp += 0.01
    return Ttemp

def Ts_V(V, P):
    """
    

    Parameters
    ----------
    V : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = 0
    Ws = Ws_T(Ttemp, P)
    while V_W(Ttemp, Ws_T(Ttemp, P), P) < V:
          Ttemp += 0.01
    return Ttemp


def T_VW(V, W, P):
    """
    

    Parameters
    ----------
    V : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = 0
    while V_W(Ttemp, W, P) < V:
          Ttemp += 0.01
    return Ttemp

def Tsat_W(W, P):
    """
    

    Parameters
    ----------
    W : TYPE
        DESCRIPTION.
    P : TYPE
        DESCRIPTION.

    Returns
    -------
    Ttemp : TYPE
        DESCRIPTION.

    """
    Ttemp = -100.0
    
    while W_Phi(Ttemp, 1.0, P) < W:
        
        Ttemp += 0.01
    return Ttemp


def main():
#    print('\n')
#    print '               Psychrometric Functions in Python'
##    print '1)  Phi_Tw(23.0, 16.0, 101325)*100      = ', 100 * Phi_Tw(23.0, 16.0, 101325)
#    print '2)  W_Tw(23, 16, 101325)                = ', W_Tw(23, 16, 101325)
#    print '3)  Pvs_T(23)                           = ', Pvs_T(23)
#    print '7)  Tw_Phi(23,0.484, 101325)            = ', Tw_Phi(23,0.484, 101325)
#    print '8)  Phi_Tdp(23, 11.577)                 = ', Phi_Tdp(23, 11.577)
#    print '9)  Tdp_Phi(23, 0.484)                  = ', Tdp_Phi(23, 0.484)
#    print '10) Tdp_Tw(23,16, 101325)               = ', Tdp_Tw(23,16, 101325)
#    print '11) Pv_Phi(23, 0.484)                   = ', Pv_Phi(23, 0.484)
#    print '12) Phi_Pv(23, 1363)*100                = ', 100*Phi_Pv(23, 1363)
#    print '13) Tdp_Pv(23,1360)                     = ', Tdp_Pv(23,1360)
#    print '14) Pv_Tdp(11.54)                       = ', Pv_Tdp(11.54)
#    print '15) Tw_W(23, 0.00846284, 101325)        = ', Tw_W(23, 0.00846284, 101325)
#    print '16) W_Tw(23, 16, 101325)                = ', W_Tw(23, 16, 101325)
#    print '17) W_Phi(23, 0.484,101325)             = ', W_Phi(23, 0.484,101325)
#    print '18) Phi_W(23, 0.008463, 101325) *100    = ', 100*Phi_W(23, 0.008463, 101325)
#    print '19) W_Tdp(11.56, 101325)                = ', W_Tdp(11.56, 101325)
#    print '20) Tdp_W(23, 0.008463, 101325)         = ', Tdp_W(23, 0.008463, 101325)
#    print '21) W_Pv(1360, 101325)                  = ', W_Pv(1360, 101325)
#    print '22) Pv_W(0.008463, 101325)              = ', Pv_W(0.008463, 101325)
#    print '23) Hd_T(23)                            = ', Hd_T(23)
 #   print '24) Dd_T(23, 101325)                    = ', Dd_T(23, 101325)
#    print '25) Vd_T(23, 101325)                    = ', Vd_T(23, 101325)
#    print '26) Pvs_T(23)                           = ', Pvs_T(23)
#    print '27) Ws_T(23, 101325)                    = ', Ws_T(23, 101325)
#    print '28) Hs_T(23, 101325)                    = ', Hs_T(23, 101325)
 #   print '29) Pvdef(23, 0.00846284, 101325)       = ', Pvdef(23, 0.00846284, 101325)
#    print '30) Sw_W(23, 0.00846284, 101325)        = ', Sw_W(23, 0.00846284, 101325)
#    print '31) H_W(23, 0.00846284)                 = ', H_W(23, 0.00846284)
#    print'32) V_W(23, 0.00846284, 101325)          = ', V_W(23, 0.00846284, 101325)
#    print '33) D_W(23, 0.00846284, 101325)         = ', D_W(23, 0.00846284, 101325)
#    print '34) P_z(10000)                          = ', P_z(10000)
#    print '35) T_z(10000)                          = ', T_z(10000)
#    print '36) Pz_P(-51.378, 10000, 26436)         = ', Pz_P(-51.378, 10000, 26436)
#    print '37) P_Pz(-51.378, 10000, 101325)        = ', P_Pz(-51.378, 10000, 101325)
#    print '38) T_TwW(16.0, 0.00846284, 101325)     = ', T_TwW(16., 0.00846284, 101325)
#    print '39) T_TwW(0, 0.000000, 101325)          = ', T_TwW(0, 0.000000, 101325)
#    print '40) Tw_W(23, 0.0084766284, 101325)      = ', Tw_W(23, 0.0084766284, 101325)
#    print '41) T_HW(H, W)(44665, 0.00847661629046) = ', T_HW(44665, 0.00847661629046)
#    print '42) Ts_H(H, P)(44665, 101325)           = ', Ts_H(44665, 101325)
#    print '43) Ts_V(V, P)(0.850374429, 101325)     = ', Ts_V(0.850374429, 101325)
#    print '44) T_VW(V, W, P)(0.85, 0.00846, 101325)= ', T_VW(0.85, 0.00846, 101325)
	
    print('\n')
    print ('               Psychrometric Functions in Python')
    print('\n')
    print ("1)  Phi_Tw(23.0, 16.0, 101325)*100      = ", round(100 * Phi_Tw(23.0, 16.0, 101325), 2))
    print ('2)  W_Tw(23, 16, 101325)                = ', round(W_Tw(23, 16, 101325), 6))
    print ('3)  Pvs_T(23)                           = ', round(Pvs_T(23), 2))
    print ('4)  Tdp_Tw(23, 16, 101325)              = ', round(Tdp_Tw(23, 16, 101325), 2))  
    print ('5)  Tw_Tdp(23, 11.57686419342, 101325)  = ', round(Tw_Tdp(23, 11.57686419342, 101325), 2))  
    print ('6)  W_Tdp(11.576, 101325)               = ', round(W_Tdp(11.576, 101325), 6))
    print ('7)  Tw_Phi(23,0.484, 101325)            = ', round(Tw_Phi(23,0.484, 101325), 2))
    print ('8)  Phi_Tdp(23, 11.577)*100             = ', round(100*Phi_Tdp(23, 11.577), 2))
    print ('9)  Tdp_Phi(23, 0.484)                  = ', round(Tdp_Phi(23, 0.484), 2))
    print ('10) Tdp_Tw(23,16, 101325)               = ', round(Tdp_Tw(23,16, 101325), 2))
    print ('11) Pv_Phi(23, 0.484)                   = ', round(Pv_Phi(23, 0.484), 2))
    print ('12) Phi_Pv(23, 1363)*100                = ', round(100*Phi_Pv(23, 1363), 2))
    print ('13) Tdp_Pv(23,1360)                     = ', round(Tdp_Pv(23,1360), 2))
    print ('14) Pv_Tdp(11.54)                       = ', round(Pv_Tdp(11.54), 2))
    print ('15) Tw_W(23, 0.00846284, 101325)        = ', round(Tw_W(23, 0.00846284, 101325), 4))
    print ('16) W_Tw(23, 16, 101325)                = ', round(W_Tw(23, 16, 101325), 4))
    print ('17) W_Phi(23, 0.484,101325)             = ', round(W_Phi(23, 0.484,101325), 4))
    print ('18) Phi_W(23, 0.008463, 101325) *100    = ', round(100*Phi_W(23, 0.008463, 101325), 2))
    print ('19) W_Tdp(11.56, 101325)                = ', round(W_Tdp(11.56, 101325), 4))
    print ('20) Tdp_W(23, 0.008463, 101325)         = ', round(Tdp_W(23, 0.008463, 101325), 2))
    print ('21) W_Pv(1360, 101325)                  = ', round(W_Pv(1360, 101325), 4))
    print ('22) Pv_W(0.008463, 101325)              = ', round(Pv_W(0.008463, 101325), 2))
    print ('23) Hd_T(23)                            = ', round(Hd_T(23), 4))
    print ('24) Dd_T(23, 101325)                    = ', round(Dd_T(23, 101325), 4))
    print ('25) Vd_T(23, 101325)                    = ', round(Vd_T(23, 101325), 4))
    print ('26) Pvs_T(23)                           = ', round(Pvs_T(23), 2))
    print ('27) Ws_T(23, 101325)                    = ', round(Ws_T(23, 101325), 4))
    print ('28) Hs_T(23, 101325)                    = ', round(Hs_T(23, 101325), 2))
    print ('29) Pvdef(23, 0.00846284, 101325)       = ', round(Pvdef(23, 0.00846284, 101325), 2))
    print ('30) Sw_W(23, 0.00846284, 101325)        = ', round(Sw_W(23, 0.00846284, 101325), 4))
    print ('31) H_W(23, 0.00846284)                 = ', round(H_W(23, 0.00846284), 2))
    print ('32) V_W(23, 0.00846284, 101325)         = ', round(V_W(23, 0.00846284, 101325), 2))
    print ('33) D_W(23, 0.00846284, 101325)         = ', round(D_W(23, 0.00846284, 101325), 2))
    print ('34) P_z(10000)                          = ', round(P_z(10000), 2))
    print ('35) T_z(10000)                          = ', round(T_z(10000), 4))
    print ('36) Pz_P(-51.378, 10000, 26436)         = ', round(Pz_P(-51.378, 10000, 26436), 1))
    print ('37) P_Pz(-51.378, 10000, 101325)        = ', round(P_Pz(-51.378, 10000, 101325), 2))
    print ('38) T_TwW(16.0, 0.00846284, 101325)     = ', round(T_TwW(16., 0.00846284, 101325), 4))
    print ('39) T_TwW(0, 0.000000, 101325)          = ', round(T_TwW(0, 0.000000, 101325), 4))
    print ('40) Tw_W(23, 0.0084766284, 101325)      = ', round(Tw_W(23, 0.0084766284, 101325), 2))
    print ('41) T_HW(H, W)(44665, 0.00847661629046) = ', round(T_HW(44665, 0.00847661629046), 4))
    print ('42) Ts_H(H, P)(44665, 101325)           = ', round(Ts_H(44665, 101325), 4))
    print ('43) Ts_V(V, P)(0.850374429, 101325)     = ', round(Ts_V(0.850374429, 101325), 4))
    print ('44) T_VW(V, W, P)(0.85, 0.00846, 101325)= ', round(T_VW(0.85, 0.00846, 101325), 4))
    print ('45) Tsat_W(.0085, 101325)                    = ', round(Tsat_W(.03, 101325), 2))
    print ('46) W_Phi(0, 1.0, 101325)                 = ', round(W_Phi(-50, 1.0, 101325), 6))
    print(Phi_W(20, 0.02, 101325))

if __name__ == '__main__':
    main()
