import pytest

from strmquiz.codage.ieee754 import float_point


class TestFloatPoint:
    @pytest.fixture
    def float_point_instance(self):
        return float_point()

    def test_vf_question(self, float_point_instance):
        # Test that vf_question returns a float within the expected range
        result = float_point_instance.vf_question()
        assert isinstance(result, float)
        assert -256 <= result <= 256

    def test_decimal_converter(self, float_point_instance):
        # Test decimal_converter for various inputs
        test_set = [
            (1234, 0.1234),
            (1, 1),
            (0.5, 0.5),
            (0, 0.0),
        ]
        for x, y in test_set:
            res = float_point_instance.decimal_converter(x)
            assert (
                res == y
            ), f"Error in testing decimal converter {x} => {res} must be {y}"

    def test_float_bin(self, float_point_instance):
        # Test float_bin for various float inputs
        test_set = [
            (5.125, "101.001"),
            (-3.75, "-0b11.110"),
            (0.5, ".100"),
        ]
        for x, y in test_set:
            res = float_point_instance.float_bin(x, places=3)
            assert (
                res == y
            ), f"Error in testing float_bin converter {x} => {res} must be {y}"

    def test_ieee754_components(self, float_point_instance):
        # Test ieee754_components for a positive number
        result = float_point_instance.ieee754_components(263.3)
        assert result["number"] == 263.3
        assert result["sign"] == 0
        assert result["exponent"] == 8  # Adjust based on expected exponent
        assert (
            result["mantissa"] == "00000111010011001100110"
        )  # Adjust based on expected mantissa
        assert (
            result["hex"] == "4383A666"
        )  # Adjust based on expected hex representation

        # Test ieee754_components for a negative number
        result = float_point_instance.ieee754_components(-263.3)
        assert result["number"] == -263.3
        assert result["sign"] == 1
        assert result["exponent"] == 8  # Adjust based on expected exponent
        assert (
            result["mantissa"] == "00000111010011001100110"
        )  # Adjust based on expected mantissa
        assert (
            result["hex"] == "C383A666"
        )  # Adjust based on expected hex representation


if __name__ == "__main__":
    pytest.main()
