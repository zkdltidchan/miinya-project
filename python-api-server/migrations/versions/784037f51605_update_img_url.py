"""update img url

Revision ID: 784037f51605
Revises: d7f93d896329
Create Date: 2023-04-28 13:29:11.179591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784037f51605'
down_revision = 'd7f93d896329'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('image_url', sa.String(length=150), nullable=True))
    op.drop_column('todos', 'img_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('img_url', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_column('todos', 'image_url')
    # ### end Alembic commands ###