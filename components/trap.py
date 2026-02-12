from __future__ import annotations

from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Entity


class Trap(BaseComponent):
    """A trap component that triggers when stepped on."""
    
    parent: Entity
    
    def __init__(self, damage: int, trap_type: str = "spike"):
        self.damage = damage
        self.trap_type = trap_type
        self.triggered = False
    
    def trigger(self, actor: Actor) -> None:
        """Trigger the trap on the given actor."""
        if self.triggered:
            return
            
        self.triggered = True
        
        # Apply damage to the actor
        actor.fighter.hp -= self.damage
        
        # Log the trap trigger
        trap_name = f"{self.trap_type} trap"
        self.engine.message_log.add_message(
            f"{actor.name} triggered a {trap_name} for {self.damage} damage!",
            color.enemy_atk if actor is self.engine.player else color.white
        )
        
        # Change appearance after triggered
        self.parent.char = "^"
        self.parent.color = (100, 100, 100)
