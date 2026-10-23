import numpy as np
from dynamics.earth_magnetic_field import earth_magnetic_field
from maths.earth_frame_conversions import eci_to_geodetic
from maths.quaternion import Quaternion


def magnetorquer_torque(satellite: Satellite, dt: float):

    if np.linalg.norm(satellite.angular_velocity) > 0.09 or True:
        # print("sat position ", satellite.position)
        lat, lon, alt_km = eci_to_geodetic(satellite.position, satellite.time)

        alt_km 

        # B_eci = earth_magnetic_field(lat, lon, alt_km, satellite.time)
        #
        #
        # B_body_frame = satellite.Quaternion.rotate_vector(B_eci)

        B_body_frame = satellite.magnetic_field_history[-1]

        m_max = 0.2  #A-m^2 Calculated from experimental values

        w_cross = np.cross(np.eye(3) * -1, np.asarray(satellite.angular_velocity))

        B_dot = w_cross @ B_body_frame

        # print(satellite.magnetic_field_history[-1])
        # print(B_body_frame)
        B_dot_norm = np.linalg.norm(B_dot)
        # print(B_dot)


        if B_dot_norm < 1e-10 or dt == 0.0:


            print("Bdot negligible")
            return np.zeros(3)

        m = - m_max * (B_dot / B_dot_norm)

        Torque = np.cross(m, B_body_frame)
        satellite.prev_Torque = Torque

        satellite.time_list.append(satellite.time)
        # print("w",satellite.angular_velocity)
        # print("Torque",Torque)
        # print("angular velocity",np.linalg.norm(satellite.angular_velocity))
        # print("quaternion",satellite.quaternion)



        return Torque

    print("Nothing")
    satellite.prev_Torque = np.zeros(3)
    return np.zeros(3)