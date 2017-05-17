from kron import command, commands

def test_command_default_option():
    def alpha():
        pass

    alpha = command(alpha)
    assert 'a' in commands
    assert commands['a'] is alpha
