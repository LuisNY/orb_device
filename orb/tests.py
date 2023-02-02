import unittest
import orb
import config


class TestOrbDevice(unittest.TestCase):

    def setUp(self):
        self.orb_device = orb.VirtualOrb()

    def test_update_cpu_values(self):
        assert self.orb_device.cpu_temp == 20
        assert self.orb_device.cpu_usage == 0

        self.orb_device.update_cpu_values(usage=30, temperature=10)
        assert self.orb_device.cpu_temp == 30
        assert self.orb_device.cpu_usage == 30

        self.orb_device.update_cpu_values(reset=True)
        assert self.orb_device.cpu_temp == 20
        assert self.orb_device.cpu_usage == 0

    def test_update_battery(self):
        assert self.orb_device.battery == 100

        self.orb_device.update_battery(delta=-10)
        assert self.orb_device.battery == 90

        self.orb_device.update_battery(reset=True)
        assert self.orb_device.battery == 100

    def test_update_disk_space(self):
        assert self.orb_device.disk_space == 100

        self.orb_device.update_disk_space(delta=-40)
        assert self.orb_device.disk_space == 60

        self.orb_device.update_disk_space(reset=True)
        assert self.orb_device.disk_space == 100

    def test_simulate_orb_usage(self):
        self.orb_device.update_cpu_values(usage=50, temperature=-14)
        self.orb_device.update_battery(delta=-50)
        self.orb_device.update_disk_space(delta=-50)
        assert self.orb_device.cpu_temp == 6
        assert self.orb_device.cpu_usage == 50
        assert self.orb_device.battery == 50
        assert self.orb_device.disk_space == 50

        self.orb_device.simulate_orb_usage()
        assert self.orb_device.cpu_temp == 7
        assert self.orb_device.cpu_usage == 52
        assert self.orb_device.battery == 48
        assert self.orb_device.disk_space == 48

    def test_simulate_device_reset(self):
        self.orb_device.update_cpu_values(usage=50, temperature=-14)
        self.orb_device.update_battery(delta=-50)
        self.orb_device.update_disk_space(delta=-50)
        assert self.orb_device.cpu_temp == 6
        assert self.orb_device.cpu_usage == 50
        assert self.orb_device.battery == 50
        assert self.orb_device.disk_space == 50

        self.orb_device.simulate_orb_device_reset()
        assert self.orb_device.cpu_temp == config.CPU_TEMP_RESET_VALUE
        assert self.orb_device.cpu_usage == config.CPU_USAGE_RESET_VALUE
        assert self.orb_device.battery == config.BATTERY_RESET_VALUE
        assert self.orb_device.disk_space == config.DISK_SPACE_RESET_VALUE

    def test_simulate_orb_full_recharge(self):
        self.orb_device.update_battery(delta=-80)
        assert self.orb_device.battery == 20

        self.orb_device.simulate_orb_full_recharge()
        assert self.orb_device.battery == config.BATTERY_RESET_VALUE


if __name__ == '__main__':
    unittest.main()
