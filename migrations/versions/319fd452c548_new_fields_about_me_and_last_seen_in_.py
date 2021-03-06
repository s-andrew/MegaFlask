"""new fields 'about_me' and 'last_seen' in user model

Revision ID: 319fd452c548
Revises: 7edcb02693eb
Create Date: 2018-09-12 17:05:20.416920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '319fd452c548'
down_revision = '7edcb02693eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
