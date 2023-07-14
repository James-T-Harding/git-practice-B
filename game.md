## Customer
| Field | Data Type |
| --- | --- |
| id | INT |
| name | Varchar(40) |

## Supplier
| Field | Data Type |
| --- | --- |
| id | INT |
| name | Varchar(40) |


## Game
| Field | Data Type |
| --- | --- |
| id | INT |
| name | Varchar(40) |
| price | INT |

## Inventory item
  - id
  - game_id
  - supply_id
  - purchase_id
## Purchases
  - id
  - time
  - customer_id
## Deliveries
  - id
  - time
  - supplier_id