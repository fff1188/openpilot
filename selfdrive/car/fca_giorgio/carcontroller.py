from opendbc.can.packer import CANPacker
from openpilot.selfdrive.car import apply_driver_steer_torque_limits
from openpilot.selfdrive.car.interfaces import CarControllerBase

from openpilot.selfdrive.car.fca_giorgio import fca_giorgiocan
from openpilot.selfdrive.car.fca_giorgio.values import CANBUS, CarControllerParams


class CarController(CarControllerBase):
  def __init__(self, dbc_name, CP, VM):
    self.CP = CP
    self.CCP = CarControllerParams(CP)
    self.packer_pt = CANPacker(dbc_name)

    self.apply_steer_last = 0
    self.frame = 0

  def update(self, CC, CS, now_nanos):
    actuators = CC.actuators
    can_sends = []

    # **** Steering Controls ************************************************ #

    if self.frame % self.CCP.STEER_STEP == 0:
      if CC.latActive:
        new_steer = int(round(actuators.steer * self.CCP.STEER_MAX))
        apply_steer = apply_driver_steer_torque_limits(new_steer, self.apply_steer_last, CS.out.steeringTorque, self.CCP)
      else:
        apply_steer = 0

      self.apply_steer_last = apply_steer
      can_sends.append(fca_giorgiocan.create_steering_control(self.packer_pt, CANBUS.pt, apply_steer, CC.latActive))

    # **** Acceleration Controls ******************************************** #

    # **** HUD Controls ***************************************************** #

    # **** Stock ACC Button Controls **************************************** #

    new_actuators = actuators.copy()

    self.frame += 1
    return new_actuators, can_sends
