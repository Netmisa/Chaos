"""empty message

Revision ID: 99f668ee548
Revises: 23a41b087b24
Create Date: 2014-07-07 13:13:00.175075

"""

# revision identifiers, used by Alembic.
revision = '99f668ee548'
down_revision = '23a41b087b24'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application_periods',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('impact_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['impact_id'], [u'impact.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application_periods')
    ### end Alembic commands ###
