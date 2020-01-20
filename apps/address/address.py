"""Address AppDaemon app."""
# pylint: disable=attribute-defined-outside-init, unused-argument, too-many-arguments
import appdaemon.plugins.hass.hassapi as hass
#
# Address App
# requires: "geopy" https://pypi.org/project/geopy/
#
#
# Args:
#   entity: entity_id of an device_tracker entity, example "device_tracker.my_entity"
#

class Address(hass.Hass):
    """Address class."""

    def initialize(self):
        """initialize Address."""
        self.log("App started.")
        entity_config = self.args["entity"]

        if isinstance(entity_config, str):
            entities = []
            entities.append(entity_config)
        else:
            entities = entity_config

        for entity in entities:
            self.listen_state(self.get_address, entity)
            self.log("State listener for {} started.".format(entity))

    def get_address(self, entity, attribute, old, new, kwargs):
        """Set the state + attributes of a defined device_tracker entity."""
        from geopy.geocoders import Nominatim
        geo = Nominatim(user_agent="AppDaemon")
        lat = self.get_state(entity, attribute="latitude")
        long = self.get_state(entity, attribute="longitude")
        state = self.get_state(entity)

        if lat is None or long is None:
            self.log("{} does not have lat/long attributes.".format(entity))
            return

        lat_long = "{}, {}".format(lat, long)

        data = geo.reverse(lat_long)
        raw = data.raw["address"]
        attributes = self.get_state(entity, attribute="all")["attributes"]

        for attr in raw:
            attributes[attr] = raw[attr]

        self.log("Updating state for {}".format(entity))
        self.set_state(entity, state = state, attributes=attributes)
