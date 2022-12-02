# Psychro
Psychrometric Functions in Python
A simple psyscrometric chart coded in TKinter and uses the library is also included.

# Naming Conventions
The function names consist of two parts separated by an underscore. The first part indicates the output of the function and the second part indicates the inputs. For instance: Phi_Tw(T, Tw, P) calculates the relative humidity - given: Wetbulb temperature, dry bulb temperature and atmospheric pressure. For brevity, drybulb temperature and atmospheric pressure are not included in function names.

# Notations and Units
| Notation  | Parameter           | Unit          |
| --------- |:-------------:      | -----:        |
| T         | Drybulb Temperature | Celsius (&deg;C)|
| Tw        | Wetbulb Temperature | Celsius (&deg;C)|
| Tdp       | Dewpoint Temperature| Celsius (&deg;C)|
| Phi       | Relative Humidity   | Fraction      |
| W         | Humidity Ratio      | kg/kg         |
| Ws        | Humidity Ratio at Saturation|  kg/kg|
| Pv        | Vapour Pressure     | Pa            |
| Pvs       | Vapour Pressure at Saturation| Pa   |
| H         | Enthalpy            |   J/kg            |
| Hd        | Enthalpy of Dry Air |   J/kg            |
| Hs        | Enthalpy at Saturation| J/kg            |
| D         | Density             |  kg/m<sup>3</sup>             |
| Dd        | Density of Dry Air  | kg/m<sup>3</sup>              |
| V         | Specific Volume     | m<sup>3</sup>/kg              |
| Vd        | Specific Volume of Dry Air|   m<sup>3</sup>/kg      |
| P         | Atmospheric Pressure|   Pa            |
| Pz        | Atmospheric Pressure at Elevation| Pa |

# Functions
Note: Relative Humidity is calculated as fraction - not percent. Multiply by 100 to obtain %. Where RH is input, use, fracrtion - devide percent by 100.
| Function          | Calculates  | Given|
|--------------------|-------------|---------|
| Tw_Tdp(T, Tdp, P) | Wet Bulb          | T, Tdp, P|
| Tw_Phi(T, Phi, P) |Wet Bulb           |T, Phi, P|
| Phi_Tdp(T, Tdp)  | RH (fraction) | T, Tdp|
| Phi_Tw(T, Tw, P)| RH (fraction) | T, Tw, P|
| Tdp_Phi(T, Phi)| Dew Point | T, Phi|
| Tdp_Tw(T, Tw, P)| Dew Point | T, Tw, P|
| Pv_Phi(T, Phi)| Vaour Pressure | T, Phi|
| Phi_Pv(T, Pv)|RH (fraction) | T, Pv|

| Tdp_Pv(T, Pv)|
| Pv_Tdp(Tdp)|
| Tw_W(T, W, P)|
| W_Tw(T, Tw, P)|
| W_Phi(T, Phi, P)|
| Phi_W(T, W, P)|
| W_Tdp(Tdp, P)|
| Tdp_W(T, W, P)|
| W_Pv(Pv, P)|
| Pv_W(W, P)|
| Hd_T(T)|
| Dd_T(T, P)|
| Vd_T(T, P)|
| Pvs_T(T)|
| Ws_T(T, P)|
| Hs_T(T, P)|
| Pvdef(T, W, P)|
| Sw_W(T, W, P)|
| H_W(T, W)|
| V_W(T, W, P)|
| D_W(T, W, P)|
| P_z(z)|
| T_z(z)
| Pz_P(T, z, P)|
| P_Pz(T, z, P0)|
| CTOK(T)|
| T_TwW(Tw, W, P)|
| T_HW(H, W)|
| Ts_H(H, P)|
| Ts_V(V, P)|
| T_VW(V, W, P)|
| Tsat_W(W, P)|

