CREATE TABLE clean_stock_data as SELECT
symbol,datetime::date AS date,
cast(open AS FLOAT) as open_price,
cast(high AS FLOAT) as high_price,
cast(low AS FLOAT) as low_price,
cast(close AS FLOAT) as close_price,
cast(volume AS BIGINT) as volume,
from raw_stock_data
where volume IS NOT NULL
AND open IS NOT NULL
AND close IS NOT NULL;

CREATE TABLE analytics_stock_data AS
SELECT
    symbol,
    date,
    open_price,
    close_price,

    (close_price - open_price) / open_price AS daily_return,

    AVG(close_price) OVER (
        PARTITION BY symbol 
        ORDER BY date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d,

    AVG(close_price) OVER (
        PARTITION BY symbol
        ORDER BY date
        ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
    ) AS moving_avg_30d,

    LAG(close_price, 1) OVER (
        PARTITION BY symbol
        ORDER BY date
    ) AS prev_close,

    close_price - LAG(close_price, 1) OVER (
        PARTITION BY symbol
        ORDER BY date
    ) AS price_change

FROM clean_stock_data;

