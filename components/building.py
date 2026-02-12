from __future__ import annotations

from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Entity


class Building(BaseComponent):
    """A building component that provides interaction functionality."""
    
    parent: Entity
    
    def __init__(self, building_type: str = "shop", description: str = "A building"):
        self.building_type = building_type
        self.description = description
        self.used = False
    
    def interact(self, actor: Actor) -> None:
        """Interact with the building."""
        if self.used:
            self.engine.message_log.add_message(
                f"The {self.building_type} has already been used.",
                color.white
            )
            return
        
        if self.building_type == "shop":
            self._shop_interaction(actor)
        elif self.building_type == "altar":
            self._altar_interaction(actor)
        elif self.building_type == "fountain":
            self._fountain_interaction(actor)
    
    def _shop_interaction(self, actor: Actor) -> None:
        """Shop interaction - restore HP for gold (not implemented, just heal)."""
        # In a full implementation, this would open a shop interface
        # For now, just provide a simple heal
        if actor.fighter.hp < actor.fighter.max_hp:
            heal_amount = min(10, actor.fighter.max_hp - actor.fighter.hp)
            actor.fighter.hp += heal_amount
            self.engine.message_log.add_message(
                f"The shopkeeper tends to your wounds. You heal {heal_amount} HP.",
                color.health_recovered
            )
        else:
            self.engine.message_log.add_message(
                "The shopkeeper has nothing to offer you right now.",
                color.white
            )
    
    def _altar_interaction(self, actor: Actor) -> None:
        """Altar interaction - restore HP fully."""
        if actor.fighter.hp < actor.fighter.max_hp:
            heal_amount = actor.fighter.max_hp - actor.fighter.hp
            actor.fighter.hp = actor.fighter.max_hp
            self.used = True
            self.engine.message_log.add_message(
                f"You pray at the altar and are healed for {heal_amount} HP!",
                color.health_recovered
            )
            # Change appearance after used
            self.parent.color = (100, 100, 100)
        else:
            self.engine.message_log.add_message(
                "The altar's power has already been used.",
                color.white
            )
    
    def _fountain_interaction(self, actor: Actor) -> None:
        """Fountain interaction - minor heal, can be used multiple times."""
        if actor.fighter.hp < actor.fighter.max_hp:
            heal_amount = min(5, actor.fighter.max_hp - actor.fighter.hp)
            actor.fighter.hp += heal_amount
            self.engine.message_log.add_message(
                f"You drink from the fountain and heal {heal_amount} HP.",
                color.health_recovered
            )
        else:
            self.engine.message_log.add_message(
                "The fountain's water is refreshing, but you are already at full health.",
                color.white
            )
