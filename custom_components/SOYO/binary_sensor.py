import logging
import voluptuous as vol
from homeassistant.components.binary_sensor import PLATFORM_SCHEMA, BinarySensorEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config[CONF_NAME]
    add_entities([MyBinarySensor(name)])

class MyBinarySensor(BinarySensorEntity):
    def __init__(self, name):
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state

    def update(self):
        # Hier die Logik zum Abrufen der Sensordaten implementieren
        self._state = False  # Beispielwert
