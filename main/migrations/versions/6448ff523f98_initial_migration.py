"""Initial migration.

Revision ID: 6448ff523f98
Revises: 
Create Date: 2021-10-13 11:48:16.800443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6448ff523f98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('all_tickers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=20), nullable=False),
    sa.Column('recommendatsion', sa.String(length=50), nullable=True),
    sa.Column('recommendatsion_all_day', sa.String(length=50), nullable=True),
    sa.Column('all_pairs_info', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticker')
    )
    op.create_table('alltickerupdatetime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alltickers_table_time_upd', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset', sa.String(length=50), nullable=False),
    sa.Column('free', sa.Float(), nullable=True),
    sa.Column('locked', sa.Float(), nullable=True),
    sa.Column('total_usd', sa.Float(), nullable=True),
    sa.Column('total_eur', sa.Float(), nullable=True),
    sa.Column('recommendatsion', sa.String(length=50), nullable=True),
    sa.Column('recommendatsion_d1', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('update_time', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coinInfotrades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=50), nullable=True),
    sa.Column('baseAsset', sa.String(length=50), nullable=True),
    sa.Column('quoteAsset', sa.String(length=50), nullable=True),
    sa.Column('current_price', sa.Float(), nullable=True),
    sa.Column('binance_id', sa.Integer(), nullable=True),
    sa.Column('orderId', sa.Integer(), nullable=True),
    sa.Column('time_last_trades', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('qty', sa.Float(), nullable=True),
    sa.Column('quote_qty', sa.Float(), nullable=True),
    sa.Column('commis', sa.Float(), nullable=True),
    sa.Column('commisAsset', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('binance_id')
    )
    op.create_table('dbupdatetime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assets_table_time_upd', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mytrades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=50), nullable=True),
    sa.Column('binance_id', sa.Integer(), nullable=True),
    sa.Column('orderId', sa.Integer(), nullable=True),
    sa.Column('time_last_trades', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('qty', sa.Float(), nullable=True),
    sa.Column('quote_qty', sa.Float(), nullable=True),
    sa.Column('commis', sa.Float(), nullable=True),
    sa.Column('commisAsset', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('binance_id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('origQty', sa.Float(), nullable=True),
    sa.Column('executedQty', sa.Float(), nullable=True),
    sa.Column('order_type', sa.String(length=50), nullable=True),
    sa.Column('side', sa.String(length=50), nullable=True),
    sa.Column('stopPrice', sa.Float(), nullable=True),
    sa.Column('time', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pairsinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=50), nullable=False),
    sa.Column('baseAsset', sa.String(length=50), nullable=True),
    sa.Column('quoteAsset', sa.String(length=50), nullable=True),
    sa.Column('orderTypes', sa.String(length=500), nullable=True),
    sa.Column('permissions', sa.String(length=500), nullable=True),
    sa.Column('test', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tickerinfoupdatetime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tickers_info_table_time_upd', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usdt_tickers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ticker')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usdt_tickers')
    op.drop_table('tickerinfoupdatetime')
    op.drop_table('pairsinfo')
    op.drop_table('orders')
    op.drop_table('mytrades')
    op.drop_table('dbupdatetime')
    op.drop_table('coinInfotrades')
    op.drop_table('assets')
    op.drop_table('alltickerupdatetime')
    op.drop_table('all_tickers')
    # ### end Alembic commands ###
