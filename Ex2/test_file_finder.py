import pytest, os
import file_finder

class TestFileFinder:

    @pytest.mark.parametrize(
        "file_path, expected",
        [
            (os.getcwd(), "file_finder.py")
        ]
    )
    def test_find_first_expected_file_multivalues(self, file_path, expected):
        """The first file with expected requirements should be itself, if no more files are contained in the current folder"""
        result = file_finder.find_first_expected_file(file_path)
        assert result == expected
        assert type(result) is str
        
    def test_file_is_executable(self):
        """The file itself should be executable and so return a 'True'"""
        result = file_finder.file_is_executable("test_file_finder.py")
        assert result == True