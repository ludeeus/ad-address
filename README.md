# ad-address [![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

_Address app for [AppDaemon](https://appdaemon.readthedocs.io/en/latest/)._

## Installation

Download the `address` directory from inside the `apps` directory here to your local `apps` directory, then add the configuration to enable the `address` module.

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
