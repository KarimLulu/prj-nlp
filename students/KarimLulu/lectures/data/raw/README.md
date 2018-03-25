# API Documentation

### Pie
* info: get fund/portfolio structure
* endpoint: /api/v1/stats/pie/
* method: GET
* return data: list of


### Share Price
* info: get price of share
* endpoint: /api/v1/stats/share_price/
* method: GET
* return data:

### Share Price Dynamic
* info: share price in time
* endpoint: /api/v1/stats/share_price_dynamic/
* method: GET
* return data: list of


### Investors Stat
* info: stats for investors
* endpoint: /api/v1/stats/investors_stat/
* method: GET
* return data: list of



### Users Stat
* info: get statistics for all investors for current manager
* endpoint: /api/v1/stats/users_stat/
* method: GET
* return data: list of



### Share Operations
* info: investments/withdrawals into fund
* endpoint: /api/v1/stats/share_ops/
* method: GET
* return data: list of



### Trade Operations
* info: buys/sells of coins or tokens into fund
* endpoint: /api/v1/stats/trade_ops/
* method: GET
* return data: list of

### User Wallet
* info: get wallet for current user
* endpoint: /api/v1/user/wallet/
* method: GET
* return data:

### Add Trade
* info: add info about trades, manager required
* endpoint: /api/v1/stats/add_trade/
* method: POST
* parameters

### Add Trade Confirmation
* info: When manager adds trade, two links (confirmation and cancellation) are sent to manager. Form of the link: `example.com/api/v1/stats/confirm/<token>`, where `<token>` is either confirmation or cancellation token.
* endpoint: /api/v1/stats/confirm/<token>
* method: GET
* parameters:

### Add Share
* info: add shares for user, managare required
* endpoint: /api/v1/user/add_share/
* method: POST
* parameters:

### Withdraw Share
* info: withdraw shares, manager required
* endpoint: /api/v1/user/withdraw/
* method: POST
* parameters:

### User Action Confirmation
* info: When manager changes user balance (adds shares to user, withdraws shares from user),
two links (confirmation and cancellation) are sent to manager. Form of the link: `example.com/api/v1/user/confirm/<token>`, where `<token>` is either confirmation or cancellation token.
* endpoint: /api/v1/user/confirm/<token>
* method: GET
