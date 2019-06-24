## Requirements

This app requires [`geopy`](https://pypi.org/project/geopy/) to be installed.

This appends address information attributes based on the lat/long from a device tracker entity.

![example](https://raw.githubusercontent.com/ludeeus/ad-address/master/example.png)

## App configuration

```yaml
address:
  module: address
  class: Address
  entity: device_tracker.my_entity
```

```yaml
address:
  module: address
  class: Address
  entity:
    - device_tracker.my_entity1
    - device_tracker.my_entity2
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`entity` | False | list/string | | entity_id of an device_tracker entity.
