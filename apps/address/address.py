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
#   name: entity_id of the new sensor, example "sensor.my_device_address"
#

class Address(hass.Hass):
    """Address class."""

    def initialize(self):
        """initialize Address."""
        self.log("App started.")
        self.listen_state(self.get_address, self.args["entity"])
        self.log("State listener for {} started.".format(self.args["entity"]))

    def get_address(self, entity, attribute, old, new, kwargs):
        """Set the state + attributes of a defined sensor."""
        from geopy.geocoders import Nominatim
        geo = Nominatim(user_agent="AppDaemon")
        lat = self.get_state(entity=self.args["entity"], attribute="latitude")
        long = self.get_state(entity=self.args["entity"], attribute="longitude")

        if lat is None or long is None:
            self.log("{} does not have lat/long attributes.".format(self.args["entity"]))
            return

        lat_long = "{}, {}".format(lat, long)

        data = geo.reverse(lat_long)
        address = data.address
        raw = data.raw["address"]

        self.log("Updating state for {}".format(self.args["name"]))
        self.set_state(self.args["name"], state=address, attributes=raw)
