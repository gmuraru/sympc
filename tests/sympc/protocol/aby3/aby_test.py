import torch

from sympc.session import Session
from sympc.session import SessionManager
from sympc.tensor import MPCTensor

from sympc.protocol import ABY3


def test_private_compare(get_clients) -> None:
    clients = get_clients(2)
    session = Session(parties=clients)
    SessionManager.setup_mpc(session)

    x_secret = torch.Tensor([1, -2])
    x = MPCTensor(secret=x_secret, session=session)

    x_binary = ABY3.A2B(x)
    print(x_binary)
    assert(False)
