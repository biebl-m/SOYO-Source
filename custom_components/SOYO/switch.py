import logging
import voluptuous as vol
from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config[CONF_NAME]
    add_entities([MySwitch(name)])

class MySwitch(SwitchEntity):
    def __init__(self, name):
        self._name = name
        self._state = False

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        self._state = False
        self.schedule_update_ha_state()
