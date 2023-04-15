from TankComponents.DirectShootingComponent import DirectShootingComponent
from Tanks.Tank import Tank
from Aliases import positionTuple
from Aliases import jsonDict
import Tanks.Settings as Settings

class AT_SPG(Tank):
    __slots__ = ()

    def __init__(self, spawnPosition: positionTuple, position: positionTuple, currentHealth: int = None) -> None:
        super().__init__(spawnPosition, position, Settings.AT_SPG, currentHealth)
  
    def _initializeShooting(self, settings: jsonDict) -> None:
        """
        Overrides initialization of the shooting component for the AT-SPG tank.

        :param settings: A dictionary containing the settings of the tank.
            - "maxAttackDistance": An integer representing the maximum attack distance of the direct shot.
            - "damage": An integer representing the damage dealt by the tank's attacks.
        """
        self._setComponent("shooting", DirectShootingComponent(settings["maxAttackDistance"], settings["damage"]))