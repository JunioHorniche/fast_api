from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='juniohorniche',
        password='secret',
        email='juniohorniche@gmail.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'juniohorniche'))

    assert user.username == 'juniohorniche'
