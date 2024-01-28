import pytest
import isolated


def test_get_args_bind_value_to_filename_property():
    args = isolated.get_args(['fizz'])
    assert args.filename == 'fizz'


def test_get_args_breaks_for_multiple_values():
    with pytest.raises(SystemExit):
        isolated.get_args(['fizz', 'buzz'])


def test_get_file_contents_returns_data_for_existing_file(tmp_path):
    filename = tmp_path / 'my_file.txt'
    with open(filename, 'w') as file:
        file.write('Hello')

    data = isolated.get_file_contents(filename)
    assert data == 'Hello'


def test_main(tmp_path):
    filename = tmp_path / 'hello_world.txt'
    with open(filename, 'w') as file:
        file.write('Hello')

    args = [str(filename)]
    
    isolated.main(args=args)
