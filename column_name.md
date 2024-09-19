# Column Name Overview

## Oil
- **date**: Date of the observation.
- **dcoilwtico**: Oil price on the given date.

## Holidays
- **date**: Date of the holiday/event.
- **type**: Indicates if it's a holiday or an event.
- **locale**: Specifies if it's a national, regional, or local holiday/event.
- **locale_name**: Tracks the location where the event is taking place.
- **description**: Name of the holiday/event.
- **transferred**: Indicates if the holiday/event was moved to the next weekday.

## Stores
- **store_nbr**: Assigned store number.
- **city**: City where the store is located.
- **state**: State where the store is located.
- **type**: Type of store.
- **cluster**: Store cluster.

## Train
- **id**: ID of the observation.
- **date**: Date of the observation.
- **store_nbr**: Store number (same as in `data_stores`).
- **family**: Item family.
- **sales**: Sales for that particular item family on that date at that store.
- **onpromotion**: Number of items on promotion at that store.

## Transactions
- **date**: Date of the observation.
- **store_nbr**: Store number (same as in `data_stores` and `data_train`).
- **transactions**: Number of transactions on that date at that store.
