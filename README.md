# Psychro
Psychrometric Functions in Python

# Naming Conventions
The function names consist of two parts separated by an underscore. The first part indicates the output of the function and the second part indicates the inputs. For instance: Phi_Tw(T, Tw, P) calculates the relative humidity - given: Wetbulb temperature, dry bulb temperature and atmospheric pressure. For brevity, drybulb temperature and atmospheric pressure are not included in function names.

# Notations and Units
| Notation  | Parameter           | Unit          |
| --------- |:-------------:      | -----:        |
| T         | Drybulb Temperature | Centigrade (C)|
| Tw        | Wetbulb Tempearture | Centigrade (C)|
| Tdp       | Dewpoint Temperature| Centigrade (C)|
| Phi       | Relative Humidity   | Fraction      |
| W         | Humidity Ratio      | kg/kg         |
| Ws        | Humidity Ratio at Saturation|  kg/kg|
| Pv        | Vapour Pressure     | Pa            |
| Pvs       | Vapour Pressure at Saturation| Pa   |
| H         | Enthalpy            |   J/kg            |
| Hd        | Enthalpy of Dry Air |   J/kg            |
| Hs        | Enthalpy at Saturation| J/kg            |
| D         | Density             |  kg/m^3             |
| Dd        | Density of Dry Air  | kg/m^3              |
| V         | Specific Volume     | m^3/kg              |
| Vd        | Specific Volume of Dry Air|   m^3/kg      |
| P         | Atmospheric Pressure|   Pa            |
| Pz        | Atmospheric Pressure at Elevation| Pa |
