# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car

Ecu = car.CarParams.Ecu
NetworkLocation = car.CarParams.NetworkLocation
TransmissionType = car.CarParams.TransmissionType
GearShifter = car.CarState.GearShifter

class CarControllerParams:
  HCA_STEP = 2                   # HCA_01 message frequency 50Hz
  LDW_STEP = 10                  # LDW_02 message frequency 10Hz
  GRA_ACC_STEP = 3               # GRA_ACC_01 message frequency 33Hz

  GRA_VBP_STEP = 100             # Send ACC virtual button presses once a second
  GRA_VBP_COUNT = 16             # Send VBP messages for ~0.5s (GRA_ACC_STEP * 16)

  # Observed documented MQB limits: 3.00 Nm max, rate of change 5.00 Nm/sec.
  # Limiting rate-of-change based on real-world testing and Comma's safety
  # requirements for minimum time to lane departure.
  STEER_MAX = 300                # Max heading control assist torque 3.00 Nm
  STEER_DELTA_UP = 4             # Max HCA reached in 1.50s (STEER_MAX / (50Hz * 1.50))
  STEER_DELTA_DOWN = 10          # Min HCA reached in 0.60s (STEER_MAX / (50Hz * 0.60))
  STEER_DRIVER_ALLOWANCE = 80
  STEER_DRIVER_MULTIPLIER = 3    # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1        # from dbc

class CANBUS:
  pt = 0
  cam = 2

BUTTON_STATES = {
  "accelCruise": False,
  "decelCruise": False,
  "cancel": False,
  "setCruise": False,
  "resumeCruise": False,
  "gapAdjustCruise": False
}

MQB_LDW_MESSAGES = {
  "none": 0,                            # Nothing to display
  "laneAssistUnavailChime": 1,          # "Lane Assist currently not available." with chime
  "laneAssistUnavailNoSensorChime": 3,  # "Lane Assist not available. No sensor view." with chime
  "laneAssistTakeOverUrgent": 4,        # "Lane Assist: Please Take Over Steering" with urgent beep
  "emergencyAssistUrgent": 6,           # "Emergency Assist: Please Take Over Steering" with urgent beep
  "laneAssistTakeOverChime": 7,         # "Lane Assist: Please Take Over Steering" with chime
  "laneAssistTakeOverSilent": 8,        # "Lane Assist: Please Take Over Steering" silent
  "emergencyAssistChangingLanes": 9,    # "Emergency Assist: Changing lanes..." with urgent beep
  "laneAssistDeactivated": 10,          # "Lane Assist deactivated." silent with persistent icon afterward
}

# Check the 7th and 8th characters of the VIN before adding a new CAR. If the
# chassis code is already listed below, don't add a new CAR, just add to the
# FW_VERSIONS for that existing CAR.

class CAR:
  GOLF_MK7 = "VOLKSWAGEN GOLF 7TH GEN"        # Chassis 5G/AU/BA/BE, Mk7 VW Golf and variants
  JETTA_MK7 = "VOLKSWAGEN JETTA 7TH GEN"      # Chassis BU, Mk7 Jetta
  PASSAT_MK8 = "VOLKSWAGEN PASSAT 8TH GEN"    # Chassis 3G, Mk8 Passat and variants
  TIGUAN_MK2 = "VOLKSWAGEN TIGUAN 2ND GEN"    # Chassis AD/BW, Mk2 VW Tiguan and variants
  AUDI_A3_MK3 = "AUDI A3 3RD GEN"             # Chassis 8V/FF, Mk3 Audi A3 and variants
  SEAT_ATECA_MK1 = "SEAT ATECA 1ST GEN"       # Chassis 5F, Mk1 SEAT Ateca and CUPRA Ateca
  SKODA_KODIAQ_MK1 = "SKODA KODIAQ 1ST GEN"   # Chassis NS, Mk1 Skoda Kodiaq
  SKODA_SCALA_MK1 = "SKODA SCALA 1ST GEN"     # Chassis NW, Mk1 Skoda Scala and Skoda Kamiq
  SKODA_SUPERB_MK3 = "SKODA SUPERB 3RD GEN"   # Chassis 3V/NP, Mk3 Skoda Superb and variants
  SKODA_OCTAVIA_MK3 = "SKODA OCTAVIA 3RD GEN" # Chassis NE, Mk3 Skoda Octavia and variants

FINGERPRINTS = {
  CAR.GOLF_MK7: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 264: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 385: 8, 418: 8, 427: 8, 668: 8, 679: 8, 681: 8, 695: 8, 779: 8, 780: 8, 783: 8, 792: 8, 795: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 870: 8, 896: 8, 897: 8, 898: 8, 901: 8, 917: 8, 919: 8, 927: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1120: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1529: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8
  }],
  CAR.JETTA_MK7: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 264: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 376: 8, 418: 8, 427: 8, 679: 8, 681: 8, 695: 8, 779: 8, 780: 8, 783: 8, 792: 8, 795: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 828: 8, 870: 8, 879: 8, 884: 8, 888: 8, 891: 8, 901: 8, 913: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1156: 8, 1157: 8, 1158: 8, 1162: 8, 1312: 8, 1343: 8, 1385: 8, 1413: 8, 1440: 5, 1471: 4, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1635: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8
  }],
  CAR.PASSAT_MK8: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 264: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 295: 8, 299: 8, 302: 8, 346: 8, 385: 8, 391: 8, 427: 8, 668: 8, 679: 8, 681: 8, 695: 8, 779: 8, 780: 8, 783: 8, 787: 8, 788: 8, 789: 8, 791: 8, 792: 8, 799: 8, 802: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 828: 8, 838: 8, 839: 8, 840: 8, 841: 8, 842: 8, 843: 8, 844: 8, 845: 8, 870: 8, 896: 8, 897: 8, 898: 8, 901: 8, 917: 8, 919: 8, 927: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1120: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1438: 8, 1440: 5, 1461: 8, 1514: 8, 1515: 8, 1520: 8, 1529: 8, 1600: 8, 1601: 8, 1603: 8, 1624: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8
  }],
  CAR.TIGUAN_MK2: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 376: 8, 418: 8, 427: 8, 573: 8, 679: 8, 681: 8, 684: 8, 695: 8, 779: 8, 780: 8, 783: 8, 787: 8, 788: 8, 789: 8, 792: 8, 795: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 828: 8, 870: 8, 879: 8, 884: 8, 888: 8, 891: 8, 896: 8, 897: 8, 898: 8, 901: 8, 913: 8, 917: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1156: 8, 1157: 8, 1158: 8, 1162: 8, 1175: 8, 1312: 8, 1343: 8, 1385: 8, 1413: 8, 1440: 5, 1471: 4, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1635: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8
  }],
  CAR.AUDI_A3_MK3: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 278: 8, 279: 8, 283: 8, 285: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 295: 8, 299: 8, 302: 8, 346: 8, 418: 8, 427: 8, 506: 8, 679: 8, 681: 8, 695: 8, 779: 8, 780: 8, 783: 8, 787: 8, 788: 8, 789: 8, 792: 8, 802: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 846: 8, 847: 8, 870: 8, 896: 8, 897: 8, 898: 8, 901: 8, 917: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1624: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8, 1792: 8, 1872: 8, 1976: 8, 1977: 8, 1982: 8, 1985: 8
  }],
  CAR.SEAT_ATECA_MK1: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 385: 8, 418: 8, 427: 8, 668: 8, 679: 8, 681: 8, 684: 8, 779: 8, 780: 8, 792: 8, 795: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 870: 8, 901: 8, 917: 8, 919: 8, 927: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1120: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8
  }],
  CAR.SKODA_KODIAQ_MK1: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 385: 8, 418: 8, 427: 8, 573: 8, 668: 8, 679: 8, 681: 8, 684: 8, 695: 8, 779: 8, 780: 8, 783: 8, 787: 8, 788: 8, 789: 8, 792: 8, 795: 8, 802: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 828: 8, 870: 8, 896: 8, 897: 8, 898: 8, 901: 8, 917: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1120: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1529: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8, 1792: 8, 1871: 8, 1872: 8, 1879: 8, 1909: 8, 1976: 8, 1977: 8, 1985: 8
  }],
  CAR.SKODA_SCALA_MK1: [{
    64: 8, 134: 8, 159: 8, 173: 8, 178: 8, 253: 8, 257: 8, 262: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 299: 8, 302: 8, 346: 8, 418: 8, 427: 8, 506: 8, 568: 8, 569: 8, 572: 8, 573: 8, 679: 8, 681: 8, 684: 8, 695: 8, 779: 8, 780: 8, 783: 8, 787: 8, 788: 8, 789: 8, 792: 8, 795: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 826: 8, 827: 8, 828: 8, 870: 8, 879: 8, 884: 8, 888: 8, 891: 8, 901: 8, 913: 8, 917: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1122: 8, 1123: 8, 1124: 8, 1153: 8, 1156: 8, 1157: 8, 1158: 8, 1162: 8, 1175: 8, 1312: 8, 1343: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1605: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1635: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1721: 8, 1792: 8, 1872: 8, 1879: 8, 1976: 8, 1977: 8, 1982: 8, 1985: 8
  }],
  CAR.SKODA_SUPERB_MK3: [{
    64: 8, 134: 8, 159: 8, 178: 8, 253: 8, 257: 8, 260: 8, 262: 8, 278: 8, 279: 8, 283: 8, 286: 8, 288: 8, 289: 8, 290: 8, 294: 8, 295: 8, 299: 8, 302: 8, 346: 8, 418: 8, 427: 8, 679: 8, 681: 8, 695: 8, 779: 8, 780: 8, 783: 8, 791: 8, 792: 8, 795: 8, 799: 8, 804: 8, 806: 8, 807: 8, 808: 8, 809: 8, 838: 8, 839: 8, 840: 8, 841: 8, 842: 8, 843: 8, 844: 8, 845: 8, 870: 8, 896: 8, 897: 8, 898: 8, 901: 8, 917: 8, 919: 8, 949: 8, 958: 8, 960: 4, 981: 8, 987: 8, 988: 8, 991: 8, 997: 8, 1000: 8, 1019: 8, 1153: 8, 1162: 8, 1175: 8, 1312: 8, 1385: 8, 1413: 8, 1440: 5, 1514: 8, 1515: 8, 1520: 8, 1600: 8, 1601: 8, 1603: 8, 1624: 8, 1626: 8, 1629: 8, 1631: 8, 1646: 8, 1648: 8, 1712: 6, 1714: 8, 1716: 8, 1717: 8, 1719: 8, 1720: 8, 1792: 8, 1872: 8, 1879: 8, 1976: 8, 1977: 8, 1985: 8, 2017: 8
  }],
}

IGNORED_FINGERPRINTS = [CAR.JETTA_MK7, CAR.PASSAT_MK8, CAR.TIGUAN_MK2, CAR.AUDI_A3_MK3, CAR.SEAT_ATECA_MK1, CAR.SKODA_KODIAQ_MK1, CAR.SKODA_SCALA_MK1, CAR.SKODA_SUPERB_MK3]

FW_VERSIONS = {
  CAR.GOLF_MK7: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906016A \xf1\x897697',
      b'\xf1\x8704E906016AD\xf1\x895758',
      b'\xf1\x8704E906023AG\xf1\x891726',
      b'\xf1\x8704E906023BN\xf1\x894518',
      b'\xf1\x8704E906027GR\xf1\x892394',
      b'\xf1\x8704L906026NF\xf1\x899528',
      b'\xf1\x8704L906056HE\xf1\x893758',
      b'\xf1\x870EA906016A \xf1\x898343',
      b'\xf1\x870EA906016S \xf1\x897207',
      b'\xf1\x875G0906259  \xf1\x890007',
      b'\xf1\x875G0906259J \xf1\x890002',
      b'\xf1\x875G0906259L \xf1\x890002',
      b'\xf1\x875G0906259Q \xf1\x890002',
      b'\xf1\x875G0906259Q \xf1\x892313',
      b'\xf1\x878V0906259P \xf1\x890001',
      b'\xf1\x878V0906259Q \xf1\x890002',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300045  \xf1\x894531',
      b'\xf1\x870D9300040S \xf1\x894311',
      b'\xf1\x870CW300047D \xf1\x895261',
      b'\xf1\x870D9300012  \xf1\x894913',
      b'\xf1\x870CW300042F \xf1\x891604',
      b'\xf1\x870DD300046F \xf1\x891601',
      b'\xf1\x870D9300020S \xf1\x895201',
      b'\xf1\x870GC300012A \xf1\x891403',
      b'\xf1\x870GC300043T \xf1\x899999',
      b'\xf1\x870GC300020G \xf1\x892403',
      b'\xf1\x870GC300020G \xf1\x892404',
      b'\xf1\x870GC300014B \xf1\x892405',
      b'\xf1\x870DD300045K \xf1\x891120',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023271212111312--071104171838103891131211',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\x13272512111312--07110417182C102C91131211',
      b'\xf1\x875Q0959655M \xf1\x890361\xf1\x82\0211413001112120041114115121611169112',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02324230011211200621143171724112491132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02315120011211200621143171717111791132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\x1315120011211200061104171717101791132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02324230011211200061104171724102491132111',
      b'\xf1\x875Q0959655AA\xf1\x890386\xf1\x82\0211413001113120053114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890386\xf1\x82\0211413001113120043114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890388\xf1\x82\0211413001113120053114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890388\xf1\x82\0211413001113120043114417121411149113',
      b'\xf1\x875Q0959655BH\xf1\x890336\xf1\x82\02314160011123300314211012230229333463100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x873Q0909144F \xf1\x895043\xf1\x82\00561A01612A0',
      b'\xf1\x873Q0909144H \xf1\x895061\xf1\x82\00566A0J612A1',
      b'\xf1\x873Q0909144L \xf1\x895081\xf1\x82\x0571A0JA15A1',
      b'\xf1\x873Q0909144M \xf1\x895082\xf1\x82\00571A0JA16A1',
      b'\xf1\x875Q0909143K \xf1\x892033\xf1\x820519A9040203',
      b'\xf1\x875Q0909144L \xf1\x891021\xf1\x82\00522A00402A0',
      b'\xf1\x875Q0909144P \xf1\x891043\xf1\x82\00511A00403A0',
      b'\xf1\x875Q0909144S \xf1\x891063\xf1\x82\00516A07A02A1',
      b'\xf1\x875Q0909144AA\xf1\x891081\xf1\x82\00521A00441A1',
      b'\xf1\x875Q0909144AA\xf1\x891081\xf1\x82\x0521A00641A1',
      b'\xf1\x875Q0909144AB\xf1\x891082\xf1\x82\00521A00642A1',
      b'\xf1\x875Q0909144AB\xf1\x891082\xf1\x82\00521A07B05A1',
      b'\xf1\x875QN909144A \xf1\x895081\xf1\x82\x0571A01A17A1',
      b'\xf1\x875QN909144A \xf1\x895081\xf1\x82\00571A01A18A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572A \xf1\x890141\xf1\x82\00101',
      b'\xf1\x875Q0907572B \xf1\x890200\xf1\x82\00101',
      b'\xf1\x875Q0907572C \xf1\x890210\xf1\x82\00101',
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\00101',
      b'\xf1\x875Q0907572F \xf1\x890400\xf1\x82\00101',
      b'\xf1\x875Q0907572H \xf1\x890620',
      b'\xf1\x875Q0907572J \xf1\x890654',
      b'\xf1\x875Q0907572P \xf1\x890682',
    ],
  },
  CAR.JETTA_MK7: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906024B \xf1\x895594',
      b'\xf1\x8704E906024L \xf1\x895595',
      b'\xf1\x8704E906024AK\xf1\x899937',
      b'\xf1\x875G0906259T \xf1\x890003',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709S927158R \xf1\x893552',
      b'\xf1\x8709S927158R \xf1\x893587',
      b'\xf1\x870GC300020N \xf1\x892803',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655AG\xf1\x890336\xf1\x82\02314171231313500314611011630169333463100',
      b'\xf1\x875Q0959655BR\xf1\x890403\xf1\x82\02311170031313300314240011150119333433100',
      b'\xf1\x875Q0959655BM\xf1\x890403\xf1\x82\02314171231313500314643011650169333463100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875QM909144B \xf1\x891081\xf1\x82\00521A10A01A1',
      b'\xf1\x875QM909144B \xf1\x891081\xf1\x82\x0521B00404A1',
      b'\xf1\x875QM909144C \xf1\x891082\xf1\x82\00521A10A01A1',
      b'\xf1\x875QN909144B \xf1\x895082\xf1\x82\00571A10A11A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572N \xf1\x890681',
      b'\xf1\x875Q0907572R \xf1\x890771',
    ],
  },
  CAR.PASSAT_MK8: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906023AH\xf1\x893379',
      b'\xf1\x8704L906026GA\xf1\x892013',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870DD300045T \xf1\x891601',
      b'\xf1\x870D9300014L \xf1\x895002',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02315120011111200631145171716121691132111',
      b'\xf1\x873Q0959655AN\xf1\x890306\xf1\x82\r58160058140013036914110311',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909143M \xf1\x892041\xf1\x820522B0080803',
      b'\xf1\x875Q0909144T \xf1\x891072\xf1\x82\00521B00703A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572R \xf1\x890771',
      b'\xf1\x873Q0907572C \xf1\x890195',
    ],
  },
  CAR.TIGUAN_MK2: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8783A907115B \xf1\x890005',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709G927158DT\xf1\x893698',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655BM\xf1\x890403\xf1\x82\02316143231313500314641011750179333423100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875QM909144C \xf1\x891082\xf1\x82\00521A60804A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
    ],
  },
  CAR.AUDI_A3_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x878V0906264B \xf1\x890003',
      b'\xf1\x875G0906259L \xf1\x890002',
      b'\xf1\x8704E906023AN\xf1\x893695',
      b'\xf1\x8704E906023BL\xf1\x895190',
      b'\xf1\x8704L997022N \xf1\x899459',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300048  \xf1\x895201',
      b'\xf1\x870D9300013B \xf1\x894931',
      b'\xf1\x870D9300041N \xf1\x894512',
      b'\xf1\x870DD300046A \xf1\x891602',
      b'\xf1\x870DD300046G \xf1\x891601',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655N \xf1\x890361\xf1\x82\0211212001112111104110411111521159114',
      b'\xf1\x875Q0959655J \xf1\x890825\xf1\x82\023111112111111--171115141112221291163221',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023121111111211--261117141112231291163221',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\x13121111111111--341117141212231291163221',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909144P \xf1\x891043\xf1\x82\00503G00803A0',
      b'\xf1\x875Q0909144T \xf1\x891072\xf1\x82\00521G00807A1',
      b'\xf1\x875Q0909144R \xf1\x891061\xf1\x82\00516G00804A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\00101',
      b'\xf1\x875Q0907572G \xf1\x890571',
    ],
  },
  CAR.SEAT_ATECA_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906027KA\xf1\x893749',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300014S \xf1\x895202',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655BH\xf1\x890703\xf1\x82\0161212001211001305121211052900',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x873Q0909144L \xf1\x895081\xf1\x82\00571N60511A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572M \xf1\x890233',
    ],
  },
  CAR.SKODA_KODIAQ_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906027DD\xf1\x893123',
      b'\xf1\x875NA907115E \xf1\x890003',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300043  \xf1\x895202',
      b'\xf1\x870DL300012M \xf1\x892107',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655BJ\xf1\x890703\xf1\x82\0161213001211001205212111052100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909143P \xf1\x892051\xf1\x820527T6050405',
      b'\xf1\x875Q0909143P \xf1\x892051\xf1\x820527T6060405',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
    ],
  },
  CAR.SKODA_OCTAVIA_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704L906021DT\xf1\x898127',  # 2015 Skoda Octavia (CKFC)
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300041P \xf1\x894507',  # 2015 Skoda Octavia (DQ250)
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655AC\xf1\x890200\xf1\x82\r11120011100010022212110200',  # 2015 Skoda Octavia
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909144R \xf1\x891061\xf1\x82\x0516A00604A1',  # 2015 Skoda Octavia
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\x0101',  # 2015 Skoda Octavia
    ],
  },
  CAR.SKODA_SCALA_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704C906025AK\xf1\x897053',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300050  \xf1\x891709',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x872Q0959655AM\xf1\x890351\xf1\x82\022111104111104112104040404111111112H14',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x872Q1909144M \xf1\x896041',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
    ],
  },
  CAR.SKODA_SUPERB_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704L906026KB\xf1\x894071',
    ],
    # Only onboarded Superb so far is a manual (Ecu.transmission, 0x7e1, None): [],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655BH\xf1\x890336\xf1\x82\02331310031313100313131013141319331413100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0910143B \xf1\x892201\xf1\x82\00563UZ060700',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x873Q0907572C \xf1\x890195',
    ],
  },
}

DBC = {
  CAR.GOLF_MK7: dbc_dict('vw_mqb_2010', None),
  CAR.JETTA_MK7: dbc_dict('vw_mqb_2010', None),
  CAR.PASSAT_MK8: dbc_dict('vw_mqb_2010', None),
  CAR.TIGUAN_MK2: dbc_dict('vw_mqb_2010', None),
  CAR.AUDI_A3_MK3: dbc_dict('vw_mqb_2010', None),
  CAR.SEAT_ATECA_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_KODIAQ_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_OCTAVIA_MK3: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_SCALA_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_SUPERB_MK3: dbc_dict('vw_mqb_2010', None),
}
