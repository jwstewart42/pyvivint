"""Module that implements the DoorLock class."""
from pyvivint.devices import VivintDevice
from pyvivint.enums import DoorLockAttributes as Attributes


class DoorLock(VivintDevice):
    """Represents a vivint door lock device."""

    @property
    def battery_level(self) -> int:
        """Door lock's battery level."""
        return self.data[Attributes.BatteryLevel]

    @property
    def low_battery(self) -> bool:
        """Returns True if battery level is low."""
        return self.data[Attributes.LowBattery]

    @property
    def is_locked(self) -> bool:
        """Returns True if door lock is locked."""
        return self.data[Attributes.State]

    @property
    def node_online(self) -> bool:
        """Returns True if the node is online."""
        return self.data[Attributes.NodeOnline]

    async def set_state(self, locked: bool) -> None:
        """Set door lock's state."""
        await self.vivintskyapi.set_lock_state(
            self.alarm_panel.id, self.alarm_panel.partition_id, self.id, locked
        )

    async def lock(self) -> None:
        """Lock the door lock."""
        await self.set_state(True)

    async def unlock(self) -> None:
        """Unlock the door lock."""
        await self.set_state(False)
