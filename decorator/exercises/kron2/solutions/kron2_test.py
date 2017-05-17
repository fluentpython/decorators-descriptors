from kron2 import command, commands

def test_command_default_option():
    def alpha():
        pass

    alpha = command()(alpha)
    assert 'a' in commands
    assert commands['a'] is alpha


def test_command_specific_option():
    def omega():
        pass

    omega = command('z')(omega)
    assert 'z' in commands
    assert commands['z'] is omega
