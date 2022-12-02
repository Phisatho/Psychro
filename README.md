# Psychro
Psychrometric Functions in Python
A simple psyscrometric chart coded in TKinter and uses the library is included.

# Naming Conventions
The function names consist of two parts separated by an underscore. The first part indicates the output of the function and the second part indicates the inputs. For instance: Phi_Tw(T, Tw, P) calculates the relative humidity - given: Wetbulb temperature, dry bulb temperature and atmospheric pressure. For brevity, drybulb temperature and atmospheric pressure are not included in function names.

# Notations and Units
| Notation  | Parameter           | Unit          | Notes |
| --------- |:-------------:      | -----:        | -----: |
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
Humidity Ratio is unitless (kg/kg) - not g/kg.
| Function          | Calculates  | Given| Notes |
|--------------------|-------------|---------|------|
| Tw_Tdp(T, Tdp, P) | Wet Bulb Temperature  | T, Tdp, P|
| Tw_Phi(T, Phi, P) |Wet Bulb  Temperature       |T, Phi, P|
| Phi_Tdp(T, Tdp)  | Relative Humidity | T, Tdp| Fraction |
| Phi_Tw(T, Tw, P)| Relative Humidity | T, Tw, P| Fraction |
| Tdp_Phi(T, Phi)| Dew Point Temperature | T, Phi|
| Tdp_Tw(T, Tw, P)| Dew Point Temperature | T, Tw, P|
| Pv_Phi(T, Phi)| Water Vapour Pressure | T, Phi|
| Phi_Pv(T, Pv)|Relative Humidity | T, Pv| Fraction |
| Tdp_Pv(T, Pv)| Dew Point Temperature | T, Pv |
| Pv_Tdp(Tdp)| Water Vapour Pressure | Tdp |
| Tw_W(T, W, P)| Wet Bulb Temperature | T, W, P |
| W_Tw(T, Tw, P)| Humidity Ratio | T, Tw, P |
| W_Phi(T, Phi, P)| Humidity Ratio | T, Phi, P |
| Phi_W(T, W, P)| Relative Humidity | T, W, P |
| W_Tdp(Tdp, P)| Humidity Ratio | Tdp, P |
| Tdp_W(T, W, P)| Dew Point Temperature | T, W, P |
| W_Pv(Pv, P)|Humidity Ratio | Pv, P |
| Pv_W(W, P)|Water Vapour Pressure | W, P |
| Hd_T(T)| Enthalpy of dry air | T |
| Dd_T(T, P)| Density of dry air | T, P |
| Vd_T(T, P)| Specific volume of dry air | T, P |
| Pvs_T(T)|Vapour pressure at saturation | T |
| Ws_T(T, P)| Humidity Ratio at saturation | T, P |
| Hs_T(T, P)| Enthalpy at saturation | T, P |
| Pvdef(T, W, P)|Vapour Pressure deficiency | T, W, P |
| Sw_W(T, W, P)|
| H_W(T, W)| Enthalpy | T, W |
| V_W(T, W, P)| Specific Volume | T, W, P |
| D_W(T, W, P)| Density | TY, W, P |
| P_z(z)|
| T_z(z)
| Pz_P(T, z, P)|
| P_Pz(T, z, P0)|
| CTOK(T)| Convert Celsius to Kelvin | T&deg;C |
| T_TwW(Tw, W, P)| Dry Bulb Temperature | Tw, W, P | Useful for drawing wetbulb lines. |
| T_HW(H, W)| Dry Bulb Temperature | H, W | Useful for drawing enthalpy lines. |
| Ts_H(H, P)|
| Ts_V(V, P)|
| T_VW(V, W, P)|
| Tsat_W(W, P)|

