## Requirements

This app requires [`geopy`](https://pypi.org/project/geopy/) to be installed.

## App configuration

```yaml
address:
  module: address
  class: Address
  entity: device_tracker.my_entity
  name: sensor.my_device_address
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`entity` | False | string | `device_tracker.my_entity`| entity_id of an device_tracker entity.
`name` | False | string | `sensor.my_device_address`| entity_id of the new sensor.
