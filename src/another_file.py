"""I'm a module
"""


class A:
    """Hello world

    Raises
    ------
    ValueError
        because why not
    """

    def f(self, a: int) -> int:
        """Some function f

        Parameters
        ----------
        a : int
            Hello

        Returns
        -------
        int
        """
        return a * 2

    @property
    def h(self) -> str:
        """I'm a property

        Returns
        -------
        str
            Property tax
        """
        return "hello"


def somefunction(h: str) -> int:
    """yes

    Parameters
    ----------
    h : str
        no

    Returns
    -------
    int
        maybe
    """
    return 6
